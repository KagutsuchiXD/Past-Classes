CS3100 - Module 1 - Lecture 07 - Wed Sep 11

# Announcements

## FSLC InstallFest

As usual, we'll be meeting in ESLC 053 at 6PM tonight.

Bring a laptop & a flash drive, we'll be helping you install Linux on your
laptop or on one of our machines!

If you're installing onto your own machine remember to *back up your data*
first!


# Call on 2 designated questioners


# Topics:
*   2.1 Operating-System Services
*   2.3 System Calls
*   Fun facts about Interrupts and Traps


----------------------------------------------------------------------------
# 2.1 Operating-System Services

A computer system consists of:

1. Hardware 
2. Software
    *   Operating system kernel
    *   Drivers
    *   System services
    *   Application software

On your mud cards write 2 things that your applications *can't* do, and 2 things they *can* do

## Things I can't do:

* Anything I/O related - including files
* Opening a network socket
* Allocate memory
* *Real* multithreading (actually using more than 1 CPU per process)
* Bootstrap process

## Things I can do:

* Manipulate data in variables and memory that I've already allocated
    * Arithmetic operations
    * Logic operation


The OS exists to support Application Software.  It provides these services to
you and your programs:

*   User Interface
*   Program Execution 
*   Input/Output
*   File-system
*   Communications
*   Error detection 
*   Resource allocation
*   Accounting
*   Security




----------------------------------------------------------------------------
# 2.3 System Calls

Modern CPUs support "dual-mode" operation to protect the integrity of the system

#### Dual/Multi-Mode Operation
Separation of ordinary instructions from privileged instructions

#### Privileged instructions
Instructions which might endanger the stability of the system

#### User mode
CPU mode in which fewer capabilities are available; certain CPU instructions are disallowed

#### Kernel/supervisor/system/privileged mode
CPU mode in which privileged instructions are allowed to execute


Examples of privileged instructions:
*   Reboot the CPU
*   Access (read/write) hardware, a.k.a. perform I/O
*   Change the value of the CPU's timer(s)
*   Transition from user to system mode

Examples of non-privileged instructions:
* Read the value of the CPU timer
* Read the value of CPU registers
* Arithmetic (`+`, `-`, `*`, `/`)
* Branching (if/else, loops)



#### System calls
A application programmer's interface to the services made available by an OS to applications


#### Application Programming Interface (API)
1.  A buzzword to impress people who don't know how to use computers
2.  Library of functions, data types and values which make tasks 
    convenient to the application developer

Many APIs have been created to do all kinds of tasks on a computer.  In
this course we're interested in the APIs which let your code work with the Operating System.

Some System APIs that you may have heard of:

*   POSIX
    Portable Operating Sytem Interface X; describes Unix systems
*   WIN32
    Microsoft's API for their "Operating System"
*   Android
    Google's OS for mobile devices
*   Java Virtual Machine (JVM)
    An idealized computer which exists only in software. The JVM must be
    re-written every time you want to put it on a new kind of computer, but
    once it exists, all that Java code will automagically work there, too.


#### System-call interface
1.  The interface which dictates how data is passed from your application into
    the kernel
2.  Libraries written in your programming language which directly deal with the
    OS, so you don't have to

System calls form the boundary between 'user mode' and 'kernel mode'.  Crossing
this boundary is called a 'context switch'.  When the OS is in kernel mode it
also puts the CPU into its privileged mode, and is able to execute privileged
CPU instructions


#### Context Switch 
When your process makes a system call which causes kernel code to run, and the
CPU changes from user mode into the kernel mode


--------------------------------------------------------------------------------
#   Fun facts about Interrupts and Traps

*   Software may also interrupt the CPU.  This is called a "trap" or a "system
    call"

*   For many computers interrupts are disabled while handling another interrupt
    to avoid "Interrupt-ception".  ISR's should be short segments of code which
    finish their jobs quickly and without causing an interrupt of their own.
    Some computers can handle "nested" interrupts, but only for so many levels
    of nesting.

*   Generally speaking, Operating Systems are Interrupt Driven; they respond to
    external events.


## Watching interrupts happen in real time on Linux

The Linux kernel counts how many times each type of interrupt has happened.
You can view this table in the `/proc/interrupts` file.

    $ watch -n 0.1 -d cat /proc/interrupts


Which interrupts are triggered when I do the following?

*   Move the mouse
*   Press a key on my external keyboard
*   Press a key on my integrated keyboard
*   `sync` my hard disks
*   Use the internet


## Observing system calls taken by programs

Ordinary software programs may interrupt the operating system when they
need the OS's help to do something related to hardware, or to avail themselves
of a service that the OS provides.

We can view which system calls an ordinary program issues with the `strace`
program:

    $ strace true
    $ strace echo hello world
    $ strace ls

As you can see, many system calls occur to load and execute even a trivial
program such as `/bin/true`:

    // this is literally it you guise
    int main(void) {
        return 0;
    }

