# Makefile for the U.S. Bureau of Labor Statistics analysis tool

# Define compiler options
CXXFLAGS = -Wall -Wextra -g3 -std=c++17

# Compile all sources into object files
CPP_SRCS = $(wildcard *.cpp)
OBJECTS  = ${CPP_SRCS:.cpp=.o}


# Link object files together into an executable
main: CC=$(CXX)
main: $(OBJECTS)


# Clean up build artifacts
clean:
	rm -f *.o main *.core
