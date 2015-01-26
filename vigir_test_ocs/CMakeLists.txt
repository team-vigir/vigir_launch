cmake_minimum_required(VERSION 2.8.3)

project(vigir_test_ocs)

find_package(catkin REQUIRED)

catkin_package(
)

#install the launch files.
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "*~" EXCLUDE  
)

#install the rviz files.
install(DIRECTORY rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "*~" EXCLUDE  
)
