#!/bin/bash

# Build script for the U.S. Bureau of Labor Statistics analysis tool

# Define compiler options
CXXFLAGS="-Wall -Wextra -g3 -std=c++17"

case $1 in
    # Clean up build artifacts
    clean)
        rm -f *.o main *.core
        ;;

    *)
        # Compile all sources into object files
        for CPP in *.cpp ; do
            echo g++ $CXXFLAGS -c $CPP
            g++ $CXXFLAGS -c $CPP
        done

        # Link object files together into an executable
        echo g++ *.o -o main
        g++ *.o -o main
    ;;

esac
