cmake_minimum_required (VERSION 3.0)
project (Report)

if (CMAKE_COMPILER_IS_GNUCXX)
    set(CMAKE_CXX_FLAGS "-Wall -Wextra -g3 -std=c++14 ${CMAKE_CXX_FLAGS}")
endif()

add_executable(Report Area.cpp Database.cpp Employment.cpp Loop.cpp main.cpp
    Report.cpp Sort.cpp Stats.cpp)
