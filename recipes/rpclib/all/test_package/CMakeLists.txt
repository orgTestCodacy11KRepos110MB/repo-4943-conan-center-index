cmake_minimum_required(VERSION 3.1.3)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(rpclib CONFIG REQUIRED)

add_executable(example example.cpp)
set_target_properties(example PROPERTIES CXX_STANDARD 14)
target_link_libraries(example rpclib::rpc)
