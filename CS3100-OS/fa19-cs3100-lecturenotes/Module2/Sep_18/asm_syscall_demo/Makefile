UNAME_M := $(shell uname -m)

ifeq ($(findstring x86,$(UNAME_M)),x86)
test: hello_x86 hello_c_x86
	@echo
	@./hello_x86
	@echo
	@./hello_c_x86

hello_c_x86:: hello_c.c
	@echo; echo --== Compiling $@ ==--
	@$(CC) $(CFLAGS) -### -o $@ $^ 2>&1 | sed -n -e '/^ /p'
	@$(CC) $(CFLAGS) -o $@ $^


else
test: hello_arm hello_c_arm
	@echo
	@./hello_arm
	@echo
	@./hello_c_arm

hello_c_arm:: hello_c.c
	@echo; echo --== Compiling $@ ==--
	@$(CC) $(CFLAGS) -### -o $@ $^ 2>&1 | sed -n -e '/^ /p'
	@$(CC) $(CFLAGS) -o $@ $^

endif


%: %.s
	@echo; echo --== Assembling $@ ==--
	$(AS) $(ASFLAGS) -o $@.o $^
	$(LD) $(LDFLAGS) -o $@ $@.o


clean:
	-rm -f hello_x86 hello_arm hello_c_* hello_c *.o *.i hello_c.s


.PHONY: clean
