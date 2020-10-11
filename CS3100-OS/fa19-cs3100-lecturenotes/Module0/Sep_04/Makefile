run: Args.class
	java Args 1 2 3 4 5
	java Args -add 1 2 3 4 5
	java Args -mul 1 2 3 4 5

Args.class: Args.java
	javac $^

clean:
	-rm -f Args.class

.PHONY: clean run
