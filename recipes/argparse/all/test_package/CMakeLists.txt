cmake_minimum_required(VERSION 3.8)
project(test_package)

find_package(argparse REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE argparse::argparse)
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_17)
