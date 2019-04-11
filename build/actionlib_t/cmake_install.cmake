# Install script for directory: /home/khaled/baymax_ws2/src/actionlib_t

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/khaled/baymax_ws2/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t/action" TYPE FILE FILES "/home/khaled/baymax_ws2/src/actionlib_t/action/Fibonacci.action")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t/msg" TYPE FILE FILES
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciAction.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciActionGoal.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciActionResult.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciActionFeedback.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciGoal.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciResult.msg"
    "/home/khaled/baymax_ws2/devel/share/actionlib_t/msg/FibonacciFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t/cmake" TYPE FILE FILES "/home/khaled/baymax_ws2/build/actionlib_t/catkin_generated/installspace/actionlib_t-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/khaled/baymax_ws2/devel/include/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/khaled/baymax_ws2/devel/share/roseus/ros/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/khaled/baymax_ws2/devel/share/common-lisp/ros/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/khaled/baymax_ws2/devel/share/gennodejs/ros/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/khaled/baymax_ws2/devel/lib/python2.7/dist-packages/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/khaled/baymax_ws2/devel/lib/python2.7/dist-packages/actionlib_t")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/khaled/baymax_ws2/build/actionlib_t/catkin_generated/installspace/actionlib_t.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t/cmake" TYPE FILE FILES "/home/khaled/baymax_ws2/build/actionlib_t/catkin_generated/installspace/actionlib_t-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t/cmake" TYPE FILE FILES
    "/home/khaled/baymax_ws2/build/actionlib_t/catkin_generated/installspace/actionlib_tConfig.cmake"
    "/home/khaled/baymax_ws2/build/actionlib_t/catkin_generated/installspace/actionlib_tConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/actionlib_t" TYPE FILE FILES "/home/khaled/baymax_ws2/src/actionlib_t/package.xml")
endif()

