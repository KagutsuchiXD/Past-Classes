PROG = deadlock
CXXFLAGS = -O0 -g3 -std=c++14 -pthread

$(PROG):

run: $(PROG)
	./$(PROG)

clean:
	-rm -f $(PROG) core *.o

.PHONY: run clean
