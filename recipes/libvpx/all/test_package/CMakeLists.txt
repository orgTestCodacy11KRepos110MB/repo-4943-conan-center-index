cmake_minimum_required(VERSION 3.8)

project(test_package C)

find_package(libvpx REQUIRED CONFIG)

add_executable(${PROJECT_NAME} test_package.c)
target_link_libraries(${PROJECT_NAME} PRIVATE libvpx::libvpx)
