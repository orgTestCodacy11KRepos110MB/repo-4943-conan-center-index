cmake_minimum_required(VERSION 3.8)
project(test_package LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(avcpp REQUIRED CONFIG)

add_executable(${PROJECT_NAME} ../test_package/test_package.cpp)
if (TARGET avcpp::avcpp)
    target_link_libraries(${PROJECT_NAME} PRIVATE avcpp::avcpp)
else()
    target_link_libraries(${PROJECT_NAME} PRIVATE avcpp::avcpp-static)
endif()
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_17)
