#ifndef MOTOR_H
#define MOTOR_H

#include <Servo.h>
#include <Arduino.h>

class Controller
{
    public:
        enum driver {L298};
        Controller(driver motor_driver, int pwm_pin, int motor_pinA);
        void spin(int pwm);

    private:

        driver motor_driver_;
        int pwm_pin_;
        int motor_pinA_;

};

#endif
