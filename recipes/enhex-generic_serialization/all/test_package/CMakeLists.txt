cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(enhex-generic_serialization CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example enhex-generic_serialization::enhex-generic_serialization)
set_target_properties(example PROPERTIES CXX_STANDARD 17)
