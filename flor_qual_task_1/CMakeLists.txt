cmake_minimum_required(VERSION 2.8.3)

project(flor_qual_task_1)

find_package(catkin REQUIRED)

catkin_package(
)

#install the launch files.
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "*~" EXCLUDE  
)