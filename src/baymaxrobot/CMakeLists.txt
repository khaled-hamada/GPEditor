cmake_minimum_required(VERSION 2.8.3)
project(baymaxrobot)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  actionlib	
  baymax_msgs
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  std_msgs
  tf2
  tf2_ros
  tf 
  move_base_msgs
)


catkin_package(
  #INCLUDE_DIRS include
  LIBRARIES baymaxrobot
  CATKIN_DEPENDS roscpp rospy tf2 tf2_ros nav_msgs baymax_msgs geometry_msgs sensor_msgs std_msgs tf  actionlib move_base_msgs
  DEPENDS system_lib
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)


add_executable(baymax_base_node src/baymax_base_node.cpp   )
add_executable(send_goal src/go_to_goal.cpp)

target_link_libraries(baymax_base_node   ${catkin_LIBRARIES})
target_link_libraries(send_goal ${catkin_LIBRARIES}  )

#############
## Install ##
#############

# Future work

#############
## Testing ##
#############

# Future work
