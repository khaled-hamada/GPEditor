cmake_minimum_required(VERSION 2.8.3)
project(actionlib_t)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  actionlib_msgs
  actionlib
  message_generation
)




## Generate actions in the 'action' folder
add_action_files(
  DIRECTORY action
  FILES Fibonacci.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs  # Or other packages containing msgs
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs actionlib
)
#############
## Install ##

