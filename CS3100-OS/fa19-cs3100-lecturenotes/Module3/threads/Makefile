CXXFLAGS = -O0 -g3 -Wall -Wextra -std=c++17
LDLIBS = -pthread


# These variables may need to be changed to match your system
CYTHON_INCLUDE = /usr/include/python3.7m
CYTHON_LIBS = -lpython3.7m -lpython3

# Helper macro to search $PATH for an executable
which = $(firstword $(wildcard $(addsuffix /$(1),$(subst :, ,$(PATH)))))

# Only build those targets for which the compiler exists
TARGETS = 
$(if $(call which,g++), $(eval TARGETS += threads))
$(if $(call which,javac), $(eval TARGETS += threads.class))
$(if $(call which,cython3), $(eval TARGETS += threads_py))
$(if $(call which,csc), $(eval TARGETS += threads_scm))


all: $(TARGETS)

threads:

threads_scm: threads.scm
	csc $^ -o $@

threads_py.c: threads_py.py
	cython3 --embed $^

threads_py: threads_py.c
	$(CC) threads_py.c -I$(CYTHON_INCLUDE) $(CYTHON_LIBS) -o $@

threads.class: threads.java
	javac $^

.PHONY: clean all

clean:
	-rm -f *.o *core threads threads_py.c threads_py threads_scm *.pyc std_thread *.class
