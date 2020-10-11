CS3100 - Module 1 - Lecture 06 - Mon Sep 09

# Announcements

## FSLC InstallFest

As usual, we'll be meeting in ESLC 053 at 6PM this Wednesday night.

Bring a laptop & a flash drive, we'll be helping you install Linux on your
laptop or on one of our machines!

If you're installing onto your own machine remember to *back up your data*
first!

# Topics:
*   1.1 What Operating Systems Do
*   1.2 Computer-System Organization
*   1.3 Computer-System Architecture
*   1.4 Operating System Structure


----------------------------------------------------------------------------
# 1.1 What Operating Systems Do



<details>
<summary>What is an Operating System?</summary>

> A program that acts as an intermediary between a user of a computer and the
> computer hardware

> "The one program running at all times on the computer" - the *kernel*


#### Kernel

Core of the exeutive software for the system; the "boss" process.  The kernel
supports the applications which the user actually cares to run.

If the kernel program crashes, you have to restart the whole system.

</details>


There are two viewpoints from which we can consider an operating system:

## 1.1.1 User View


<details>
<summary>What is the goal of the system from this perspective?</summary>

+ Make users more productive by providing helpful services
    + Give user information or feed back about the state of the system
+ Be stable (unlike some OSes we know...)
    + Make efficient use of the hardware

</details>


## 1.1.2 System View

<details>
<summary>What is the goal of the system from this perspective?</summary>

+ Make efficient use of the hardware
+ Provide a secure environment for users to interact
+ Make it easy to use the system

</details>


<details>
<summary>What resources could the OS be in charge of?</summary>

*   Hardware resources
    *   CPU
    *   RAM
    *   Storage
    *   I/O

*   Software resources
    *   Services
    *   Network access
    *   Drivers
    *   Access to other processes
    *   File system
    *   Protection from malware


</details>

----------------------------------------------------------------------------
# 1.2 Computer-System Organization

We've discussed the question "what is a computer?" from a metaphyiscal
standpoint.  Now it's time to define what a computer is from the pragmatic
standpoint.

>  A modern general-purpose computer system consists of one or more CPUs and a
>  number of devices connected through a common bus

#### Bus

Circuitry pathway which carries signals between components of a system.

## 1.2.1 Interrupts

Your CPU gets interrupted all the time.  Why does this happen?

* A CPU can do only one thing at a time
* the CPU is outnumbered by I/O devices which compete for its attention
* The I/O devices and the CPU operate simultaneously
* Device controllers inform the CPU of external events by an *interrupt*
* Each device controller has a local buffer (even if it is a few bytes) to hold
  data until the CPU can service it
* The CPU moves data from/to device controllers
* The device controller signals it is finished via an interrupt


#### Interrupt Vector (IV):

An array (vector) of addresses which point to code that the CPU runs to handle
hardware requests



#### Interrupt Service Routine (ISR):

The code which the IV points to.

Each location in the IV points to some snippet of code which is useful in that
circumstance.  A machine can be defined in terms of the Interrupts it is
capable of responding to.

The ideal ISR executes quickly and allows the CPU to return to its regular task.


## 1.2.2 Storage Heirarchy

<details>
<summary>What is the difference between Volatile and Non-Volatile storage devices?</summary>

Volatile storage:

* RAM
* Cache
* REgisters on the CPU

Secondary (non-volatile) storage:

* Hard drives
* SSD's
* CDROM / DVDROM / Blue Ray
* Cloud storage (by dint of their being SSD's)

</details>

#### Storage is a trade-off between speed, size and cost

Storage devices *decrease* in speed/cost and *increase* in capacity as you go down
this list:

1. CPU registers
2. CPU cache
3. Main memory (RAM)
4. Solid-State Disk (SSD)
5. Magnetic Disk (Hard Disk)
6. Optical Disk (DVD, CDROM, etc.)
7. Magnetic Tapes



----------------------------------------------------------------------------
# 1.3 Computer-System Architecture

*   Simple systems use a single CPU
*   Modern consumer-grade computers feature multiple CPUs (Multiprocessor systems) 
    *   Also known as parallel systems, tightly-coupled systems
*   Multiprocessor Advantages include:
    *   Increased throughput
    *   Economy of scale
    *   Increased reliability – graceful degradation or fault tolerance


## Two types of Multiprocessor systems

1. Asymmetric Multiprocessing
    *   Each processor core is assigned a specific task
    *   One core runs the kernel
    *   Other cores run user processes
2. Symmetric Multiprocessing (SMP)
    *   Each processor can perform any task
    *   The kernel process "floats" among the available cores



----------------------------------------------------------------------------
# 1.4 Operating System Structure

## 1.4.1 Multiprogramming and Multitasking

### Multiprogramming

Tries to make the best use of the CPU by arranging its work so that the CPU
is never left idle.  A queue of jobs is kept so that as soon as one job is done
the next is started.


#### Jobs (a.k.a. tasks)

All the stuff a computer needs to do:

* Programs or data which the CPU needs to process
* You may see these in a process viewer tool (i.e. htop, Process Explorer on
  Windows, etc.)



### Timesharing (a.k.a. multitasking)

This is multiprogramming done by splitting up individual tasks into little
"timeslices", doing a little bit of work, then switching to the next task and
doing a little bit of work on it... etc.  Instead of finishing one process
before switching to the next, all processes take little turns.

This gives the illusion that the OS is simultaneously making progress on all
tasks. 


#### Parallelism
Working on more than one thing simultaneously

<details>
<summary>Q: How many CPUs do you need in a computer to achieve parallelism?</summary>

A: More than 1

</details>


#### Concurrency
Splitting up a large task into smaller pieces which you work on a piece at a time.

A.K.A. "Dollar Store parallelism"

