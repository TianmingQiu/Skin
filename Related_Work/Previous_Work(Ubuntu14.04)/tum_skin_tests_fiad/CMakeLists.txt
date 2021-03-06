cmake_minimum_required(VERSION 2.8.3)
project(tum_skin_tests_fiad)

SET(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
catkin_package()
find_package(catkin REQUIRED COMPONENTS
    roscpp
    tum_skin_msgs_fiad
    tum_skin_bridge_fiad
    sensor_msgs
    std_msgs
    geometry_msgs
    tf
    tf_conversions
    visualization_msgs
    interactive_markers
)

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES tum_skin_tests_fiad
    CATKIN_DEPENDS roscpp tum_skin_bridge_fiad tum_skin_msgs_fiad sensor_msgs std_msgs tf tf_conversions visualization_msgs interactive_markers
    DEPENDS system_lib libqt4-dev
)

find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIR})
add_definitions(${EIGEN_DEFINITIONS})
message(STATUS "EIGEN3_INCLUDE_DIR " ${EIGEN3_INCLUDE_DIR})


find_package(Qt4 COMPONENTS QtCore QtGui QtOpenGL REQUIRED)

# add Qt Modules
set(QT_USE_QTNETWORK TRUE)

include(${QT_USE_FILE})

# DON'T USE (enforces Q_SIGNAL etc. macros)
# use here because of boost problems in tf etc.
ADD_DEFINITIONS(-DQT_NO_KEYWORDS)

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${roscpp_INCLUDE_DIRS}
)


# needed for Qt generated files
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_BINARY_DIR}
)

add_subdirectory(src/Applications)


set(HEADERS
#    include/tum_skin_tests_fiad/InteractiveTf.h
)

set(SOURCES
#    src/InteractiveTf.cpp
)


#add executables
#add_library(tum_skin_tests_fiad ${SOURCES} ${HEADERS} ${HEADERS_MOC} ${FORMS_UI} ${RESOURCES_RC})

# link target against libs
#target_link_libraries(tum_skin_tests_fiad
#    ${catkin_LIBRARIES}
#    ${roscpp_LIBRARIES}
#    ${QT_LIBRARIES}
#)




#install(DIRECTORY include/${PROJECT_NAME}/
#  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

