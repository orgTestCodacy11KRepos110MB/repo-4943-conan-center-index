cmake_minimum_required(VERSION 3.4)
project(cmake_wrapper LANGUAGES C)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(source_subfolder)
