cmake_minimum_required(VERSION 3.4)
project(test_package LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(source_location CONFIG REQUIRED)
add_executable(${PROJECT_NAME} src/test.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE source_location::source_location)

set_target_properties(${PROJECT_NAME}
    PROPERTIES
    	CXX_STANDARD 11
    	CXX_STANDARD_REQUIRED ON
    	CXX_EXTENSIONS OFF
)
