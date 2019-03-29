#include "Motor.h"

Controller::Controller(driver motor_driver, int pwm_pin, int motor_pinA):
    motor_driver_(motor_driver),
    pwm_pin_(pwm_pin),
    motor_pinA_(motor_pinA)

{
    
    pinMode(pwm_pin_, OUTPUT);
    pinMode(motor_pinA_, OUTPUT);


    //ensure that the motor is in neutral state during bootup
    analogWrite(pwm_pin_, abs(0));
}

void Controller::spin(int pwm){
	if( pwm > 0 ){
   		 digitalWrite(motor_pinA_, HIGH);
	}

	else if(pwm <0) {
	
   		pwm *= -1;
    		digitalWrite(motor_pinA_, LOW);
  	}
        analogWrite(pwm_pin_, abs(pwm));

}
