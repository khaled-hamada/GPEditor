#ifndef BAYMAX_BASE_CONFIG_H
#define BAYMAX_BASE_CONFIG_H

//the  baymax base
#define BAYMAX_BASE DIFFERENTIAL_DRIVE

//the motor driver
#define USE_L298_DRIVER


//IMU

#define USE_MPU6050_IMU

// for debugging data to ros from rosserial node
#define DEBUG 1

#define K_P 1.0 // P constant
#define K_I 0.2 // I constant
#define K_D 0.1 // D constant

//define your robot' specs here
#define MAX_RPM 110            // motor's maximum RPM
#define COUNTS_PER_REV 240       // wheel encoder's no of ticks per rev
#define WHEEL_DIAMETER 0.12       // wheel's diameter in meters
#define PWM_BITS 8                // PWM Resolution of the microcontroller
#define LR_WHEELS_DISTANCE 0.40  // distance between left and right wheels


/// ENCODER PINS
#define MOTOR1_ENCODER_A 3
#define MOTOR1_ENCODER_B 2

#define MOTOR2_ENCODER_A 18
#define MOTOR2_ENCODER_B 19

//MOTOR PINS
#ifdef USE_L298_DRIVER
  #define MOTOR_DRIVER L298

  #define MOTOR1_PWM 9
  #define MOTOR1_IN_A 52


  #define MOTOR2_PWM 8
  #define MOTOR2_IN_A  53


  #define PWM_MAX pow(2, PWM_BITS) - 1
  #define PWM_MIN  -PWM_MAX
#endif



#endif
