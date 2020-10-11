# Assembly language syscall demo

This directory contains two version of the "Hello World" program
written in assembly language.

* `hello_arm.s` - Hello world in ARM assembly
* `hello_x86.s` - Hello world in Intel x86 assembly
* `hello_c.c`   - Hello world in portable C


This program demonstrates that even a very trivial program such as Hello World
differs between two CPU architectures even when the Operating System and the
Assembler are the same.

Compare the length and complexity of the ASM source code to the version written
in portable C.  The same C program compiles without modification on both ARM
and Intel Linux systems.

Compare the size of the binaries produced by the C compiler to those created
directly by the Assembler and Linker.
