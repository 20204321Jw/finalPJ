cmake_minimum_required(VERSION 3.0.2)
project(self_drive)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  sensor_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy sensor_msgs std_msgs
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

