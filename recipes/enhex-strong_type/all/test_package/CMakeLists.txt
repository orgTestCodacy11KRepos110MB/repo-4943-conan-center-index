cmake_minimum_required(VERSION 3.1)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(enhex-strong_type CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example enhex-strong_type::enhex-strong_type)
set_target_properties(example PROPERTIES CXX_STANDARD 17)
