cmake_minimum_required(VERSION 3.26)
project(Cryptography)

set(CMAKE_CXX_STANDARD 14)

set(BOOST_INCLUDE_DIR    C:\\MinGW\\include\\boost)
set(BOOST_LIBRARY_DIR    C:\\MinGW\\include\\boost)
set(BOOST_ROOT          C:\\MinGW\\include\\boost)

find_package(Boost 1.71.0)

if(Boost_FOUND)

    message(STATUS "Boost_INCLUDE_DIRS: ${BOOST_INCLUDE_DIR}")
    message(STATUS "Boost_LIBRARIES: ${BOOST_LIBRARY_DIR}")
    message(STATUS "Boost_VERSION: ${Boost_VERSION}")

    include_directories(${Boost_INCLUDE_DIRS})

endif()

add_executable(Cryptography
        Lab_3/Lab_3.cpp)
