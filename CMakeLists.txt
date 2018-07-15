#
# Policies
#
if(POLICY CMP0048)
    cmake_policy(SET CMP0048 NEW)
endif()

#
# Project
#
CMAKE_MINIMUM_REQUIRED(VERSION 3.5)
PROJECT(libxmldiff
    VERSION 0.2.8
    )

#
# Use Conan.io
#
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
conan_define_targets()

#
# Requirements
#
find_package(libxml2 REQUIRED)

#
# Subdirs
#
ADD_SUBDIRECTORY(src)

#
# Export
#
include(CMakePackageConfigHelpers)

write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
    )

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/LibraryConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    @ONLY
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        . # Root Directory
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        share/cmake/${PROJECT_NAME}/
    )

install(EXPORT Targets
    FILE ${PROJECT_NAME}Targets.cmake
    DESTINATION share/cmake/${PROJECT_NAME}
    )
