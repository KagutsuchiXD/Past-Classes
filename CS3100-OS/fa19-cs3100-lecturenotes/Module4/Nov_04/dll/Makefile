CXXFLAGS = -Wall -Wextra -O0 -g3 -fPIC -std=c++17
LDLIBS = -ldl
SO = $(patsubst %.cpp, %.so, $(wildcard lib*.cpp))


all: $(SO) main

libdemo%.so: libdemo%.cpp
	$(CXX) $(CXXFLAGS) -shared $^ -o $@

clean:
	-rm -f main *.o *.so

.PHONY: clean all
