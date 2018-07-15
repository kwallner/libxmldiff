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
find_package(libiconv REQUIRED)
find_package(libxml2 REQUIRED)

#
# Subdirs
#
ADD_SUBDIRECTORY(src)
