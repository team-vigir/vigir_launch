cmake_minimum_required(VERSION 2.8.3)
project(vigir_common_launch)


find_package(catkin REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES vigir_common_launch
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

#install the launch files.
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "*~" EXCLUDE  
)


