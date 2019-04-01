#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <baymax_msgs/Velocities.h>
#include <baymax_msgs/baymaxPose.h>
#include <sensor_msgs/Imu.h>
#include <math.h>
#define    PI  3.141592

double g_vel_x = 0.0;
double g_vel_y = 0.0;

double g_vel_dt = 0.0;
double g_imu_dt = 0.0;
double g_imu_z = 0.0;

ros::Time g_last_loop_time(0.0);
ros::Time g_last_vel_time(0.0);
ros::Time g_last_imu_time(0.0);

void velCallback( const baymax_msgs::Velocities& vel) {
    //callback every time the robot's linear velocity is received
    ros::Time current_time = ros::Time::now();

    g_vel_x = vel.linear_x;
    g_vel_y = vel.linear_y;
   // g_imu_z = vel.angular_z;

    g_vel_dt = (current_time - g_last_vel_time).toSec();
    g_last_vel_time = current_time;
}

void IMUCallback( const sensor_msgs::Imu& imu){
    //callback every time the robot's angular velocity is received
    ros::Time current_time = ros::Time::now();
    //this block is to filter out imu noise
    if(imu.angular_velocity.z > -0.03  &&  imu.angular_velocity.z < 0.03)
    {
     	  g_imu_z = 0.00;
    }
    else{
    
        g_imu_z = imu.angular_velocity.z;
    }
    // reject noise above 1.0 or -1.0 
   /* if(g_imu_z > 1.0)
	g_imu_z = 1.0;
    else if(g_imu_z < -1.0)
	g_imu_z = -1.0; */

    g_imu_dt = (current_time - g_last_imu_time).toSec();
    g_last_imu_time = current_time;
}

int main(int argc, char** argv){
    ros::init(argc, argv, "base_controller");
    ros::NodeHandle n;
    ros::NodeHandle nh_private_("~");
    ros::Subscriber sub = n.subscribe("raw_vel", 50, velCallback);
    ros::Subscriber imu_sub = n.subscribe("imu/data", 50, IMUCallback);
    ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
    ros::Publisher bayPose = n.advertise<baymax_msgs::baymaxPose>("baymax/pose",50);
    tf::TransformBroadcaster odom_broadcaster;
    // return it again to 10 hz i made it = 1hz just for debugging 
    double rate = 20;
    double x_pos = 0.0;
    double y_pos = 0.0;
    double theta = 0.0;
    // just for deugging 
    double last_theta = 0.0;
    double delta_x = 0;
    double delta_y = 0;

    ros::Rate r(rate);
    while(n.ok()){
        ros::spinOnce();
        ros::Time current_time = ros::Time::now();

        //linear velocity is the linear velocity published from the arduino board in x axis
        double linear_velocity_x = g_vel_x;

        //linear velocity is the linear velocity published from the arduino board in y axis
        double linear_velocity_y = g_vel_y;

        //angular velocity is the rotation in Z from imu_filter_madgwick's output
        double angular_velocity = g_imu_z;

        //calculate angular displacement  θ = ω * t
        double delta_theta = angular_velocity * g_imu_dt; //radians
	
	
        if( (fabs(theta) > (.45 * PI) && fabs(theta) < (.55 * PI))  || 
		(fabs(theta) > (1.45 * PI) && fabs(theta) < (1.55 * PI)))
		 delta_x = 0;
	else
		 delta_x = (linear_velocity_x * cos(theta) ) * g_vel_dt; //m
	if( (fabs(theta) < .15) || (fabs(theta)  > (2 * PI - .1) ) )
       		 delta_y = 0; //m
	else 
		 delta_y = (linear_velocity_x * sin(theta) ) * g_vel_dt; //m

        //calculate current position of the robot
        x_pos += delta_x;
        y_pos += delta_y;
        theta += delta_theta ;
	/*if (fabs(delta_theta) > 0.125){
		theta  = ( theta / 6.85) * (2 * PI);
		//theta = std::fmod(theta , 2 * M_PI);
	}*/

	// the drift is .55 for each 2 Pi so we will subtract it as  .55/2*PI
	if (fabs(theta - last_theta) > 0.2){
		if(fabs(last_theta - theta ) >= 2.5){
			theta = theta - ((.075 * theta) );
			
		}
		else{
			theta = theta - ((.075 * (theta - last_theta))  );
			
		}
		/*theta = theta - fabs( (.0875 * (theta - last_theta)) );
		last_theta = theta ; */
		//theta  = ( theta / 6.85) * (2 * PI);
		//theta = std::fmod(theta , 2 * M_PI);
		//theta = fmod((theta + PI), (2 * PI)) - PI;
		last_theta = theta ;

	}
	//there is always an offset between .3 to .55 
	/*if( fabs(theta) >= (2 * PI + 0.55)){
		//theta = std::fmod(theta , 2 * M_PI);
		theta  = 0.0;
	}*/
	if( fabs(theta) >= (2 * PI)){
		//theta = std::fmod(theta , 2 * M_PI);
		theta  = 0.0;
	}
	//ROS_INFO("g_IMU_Z %f  \n",g_imu_z);	
	baymax_msgs::baymaxPose bPose;
	bPose.x = x_pos;
	bPose.y = y_pos;
	bPose.theta = theta;
	bayPose.publish(bPose);	

        //calculate robot's heading in quarternion angle
        //ROS has a function to calculate yaw in quaternion angle
        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(theta);

        geometry_msgs::TransformStamped odom_trans;
        odom_trans.header.frame_id = "odom";
        odom_trans.child_frame_id = "base_footprint";
        //robot's position in x,y, and z
        odom_trans.transform.translation.x = x_pos;
        odom_trans.transform.translation.y = y_pos;
        odom_trans.transform.translation.z = 0.0;
        //robot's heading in quaternion
        odom_trans.transform.rotation = odom_quat;
        odom_trans.header.stamp = current_time;
        //publish robot's tf using odom_trans object
        odom_broadcaster.sendTransform(odom_trans);

        nav_msgs::Odometry odom;
        odom.header.stamp = current_time;
        odom.header.frame_id = "odom";
        //robot's position in x,y, and z
        odom.pose.pose.position.x = x_pos;
        odom.pose.pose.position.y = y_pos;
        odom.pose.pose.position.z = 0.0;
        //robot's heading in quaternion
        odom.pose.pose.orientation = odom_quat;

        odom.child_frame_id = "base_footprint";
        //linear speed from encoders
        odom.twist.twist.linear.x = linear_velocity_x;
        odom.twist.twist.linear.y = linear_velocity_y;
        odom.twist.twist.linear.z = 0.0;

        odom.twist.twist.angular.x = 0.0;
        odom.twist.twist.angular.y = 0.0;
        //angular speed from IMU
        odom.twist.twist.angular.z = g_imu_z;

        //TODO: include covariance matrix here

        odom_pub.publish(odom);

        g_last_loop_time = current_time;
        r.sleep();
    }
}
