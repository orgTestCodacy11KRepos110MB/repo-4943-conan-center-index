cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(thrust CONFIG REQUIRED)

add_executable(test_package test_package.cpp)
target_link_libraries(test_package thrust::thrust)
set_target_properties(test_package PROPERTIES CXX_STANDARD 11)
