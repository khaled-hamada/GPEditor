#!/usr/bin/env python 


import os 
#os.system("gnome-terminal  -x   rosrun  chefbot_bringup simple_navig_goals.py 10.0 3.14  ")
os.system("rosrun  chefbot_bringup simple_navig_goals.py 10.0 3.14 & ")
#os.system('rosrun  chefbot_bringup simple_navig_goals.py 10.0 3.14 ') 
#os.system('
os.system('rosrun  chefbot_bringup robot_gui.py &')
#os.system('roslaunch baymaxrobot minimal.launch &')

