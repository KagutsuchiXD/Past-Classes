

Lecture 1: Module0\Aug_26\README.md
================================================================

CS3100 - Module 0 - Lecture 01 - Mon Aug 26


# Topics:
* Get to know your professor
* What can I expect from this course?
* "What is a computer?" mud card activity
* "Get to know you" mud card activity



----------------------------------------------------------------------------
# Get to know your professor

Hi, I'm Erik Falor, and I'll be your professor this semester.

I graduated with a Master's degree from USU in 2017 and have been teaching here
ever since.  Before that I worked as a software engineer for 13 years.

## I don't like
* Desktop Environments
* Windows (TM)
* QWERTY
* Squishy keyboards
* Bic pens
* Rap music
* Country music


## I do like
* Window managers
* Linux
* My custom keyboard layout
* Mechanical keyboards
* Fountain pens
* Long walks in the woods
* Every other genre of music ever, without exception



----------------------------------------------------------------------------
# What can I expect from this course?

* Course module structure 
    * Course rules & Syllabus quiz
    * [Course Rules](https://gitlab.cs.usu.edu/erik.falor/fa19-cs3100-lecturenotes/blob/master/Course_Rules.md)
* Course outline
    * Chapters 1-10 of textbook
    * Most assignments are written in Java
* Assignments
    * Design & brainstorm with study buddies
    * Write code individually
    * Submit to GitLab only; nothing to do on Canvas
    * Tutor Room Hours
        * Mon - Fri: 10AM to 9PM
        * Sat: 12PM to 9PM
* Examinations
    * **Two** exams in this class
    * Schedule a spot in the Testing Center now
* Class participation
    * In-class activities & lecture attendance
    * Designated questioner


----------------------------------------------------------------------------
# "What is a computer?" mud card activity

I'll often ask you to turn in a "mud card" at the end of class.  The name comes
from "muddiest point".  You will reflect upon what was discussed in a lecture
and write a brief note explaining what you did not understand or a new question
raised by what you learned.

This serves the following purposes:

1. Provides a quick head-count of who attended today
2. Putting into writing what you learned in a day improves recall
3. Lets me know which topics were well received, and which need another approach
4. Gives another opportunity for you to ask a question in a non-intimidating way


At the top of your mud card please legibly write your name and A#.


### 1. Is this a computer?
![Is this a computer?](images/abacus.jpg)

### 2. How about this?
![How about this?](images/sliderule.jpg)

### 3. Or this?
![Or this?](images/difference_engine.jpg)

### 4. If that was a computer, then this is definitely a computer
![If that was a computer, then this is definitely a computer](images/tinker_toy_cpu.jpg)


### 5. This, then, certainly is a computer
![This, then, certainly is a computer](images/ENIAC.jpg)

### 6. How many computers are captured in this photo?
![How many computers are captured in this photo?](images/Mary_Jackson.jpg)



----------------------------------------------------------------------------
# "Get to know you" mud card activity

On the other side of your mud card please write the following:

1.  What is your class (Sophomore, Junior, etc.) and major degree?
2.  Why are you enrolled in this course?
3.  What is your favorite meme?
4.  What type of music do you like the best?
5.  What do you like to do for fun?
6.  What is a good way for you to send pictures of mud cards to me?
7.  Should I spend a lecture on "how to use git", or move on to something else?
8.  Names of at least 3 of your neighbors and something unique or interesting about them
9. Who are your study buddies in this class?


Lecture 2: Module0\Aug_28\README.md
================================================================

CS3100 - Module 0 - Lecture 02 - Wed Aug 28

# Announcements

## USU Network outage yesterday

If you couldn't connect to the GitLab server, try again today.



## GitLab Confirmation Emails

Many students weren't receiving their confirmation emails from GitLab at their
aggiemail.usu.edu addresses.  Many students did.

Why this happened is a mystery that I asked USU IT to look into.  I hope they
didn't break the network while they were looking into it!

I have suspended confirmation emails for the time being.

Contact me if you still can't get into your account.



Call on 2 designated questioners
============================================================================



# Topics:

* Introduce Assignment #0
* Mud card followup: What is a computer?
* The command line interface
* How do I use Git to submit my homework?



----------------------------------------------------------------------------
# Introduce Assignment #0

The purpose of this assignment is to get you familiarized with working in a command line environment by compiling and running a Java program from the command line.

https://usu.instructure.com/courses/547959/assignments/2699281


----------------------------------------------------------------------------
# Mud card followup: What is a computer?

https://gitlab.cs.usu.edu/erik.falor/fa19-cs3100-lecturenotes/blob/master/Module0/Aug_26/README.md#what-is-a-computer-mud-card-activity

### What do these devices have in common?
1. Slide rule
2. Abacus
3. Tinker-toy contraption
4. Difference Engine


1. They store data
2. They have states
3. Embody algorithms or "programs", but a user has to interpret it



### What are their differences?
1. Some do the computation on their own without a human making choices
2. Some need a human to move them, and interpret their state


* Some of them are electric, others are analog
* Some of these devices require continual human interaction to operate:
    * cranking the gears
    * moving the beads
    * sliding the rule and cursor about
    * pull moths out of the relays



#### Definition of a computer (from Wikipedia)

> A computer is a device that can be instructed to carry out sequences of
> arithmetic or logical operations automatically via computer programming.

The important part is *automatically*

Once the device is set up and turned on, it follows its instructions, including
making any decisions, automatically without further human intervention.



----------------------------------------------------------------------------
# How do I use Git to submit my homework?

These eight fundamental git commands are enough to succeed in my class:

1.  git status
2.  git init
3.  git add
4.  git config
5.  git commit
6.  ~~git remote~~
7.  ~~git push~~
8.  git log

If you are already comfortable with these commands, you are free to go

We'll discuss `git remote` and `git push` on Friday.

* [Git repository set up instructions](https://gitlab.cs.usu.edu/erik.falor/fa19-cs3100-lecturenotes/blob/master/Module0/Git_Repository_Setup.md)

* [Git Howto](../Git_HOWTO.md)


Lecture 3: Module0\Aug_30\README.md
================================================================

CS3100 - Module 0 - Lecture 03 - Fri Aug 30

# Announcements

## Assignment due dates have been adjusted

As explained in a previous lecture, a correction has been applied to the due
dates of assignments in Canvas, shifting most due dates up by one week.


## Labor Day Holiday
* No class on Monday, Sept 2
* We'll resume on Wednesday, Sept 4


## Free software and Linux Club
* Opening meeting
* Get acquainted with Linux and Open Source Software
* Wednesday, Sept 4 6pm @ ESLC 053



# Topics:
* Mud card followup
* Assignment #0 pointers
* How do I use Git to submit my homework?


----------------------------------------------------------------------------
# Mud card followup

*   Before our discussion about this on Wednesday, many of you agreed with the
    definition of **computer** as found on Wikipedia, insofar as automation is
    concerned.  What did you think of that electronic slide rule?
    [The Electric Slide Rule](https://www.youtube.com/watch?v=MEyIppEOQTw)

*   Electronic mud card submissions will be done by email
    ![Electronic mud card submission](mudcards.png)

*   Participation points will begin to show up after the add/drop date passes
    next week.


----------------------------------------------------------------------------
# Assignment #0 pointers

*   I added links to the official Java documentation for the `BigInteger` and
    `BigDecimal` classes to the assignment on Canvas.
*   You *don't* actually need five git commits in this assignment's repository;
    I misspoke about that.
*   If you don't know how to compute the value of `e` with *iterations*,
    re-read the assignment description for a hint.
*   Don't type the characters `[`, `]` in the shell; it will misinterpret them.
*   `-fac` for very large values will take a *long* time to compute.  On my PC
    `java Assign1 -fac 20000` took 0.6 seconds and `java Assign1 -fac 200000`
    took nearly 30 seconds to complete.  My trial of `-fac 2147483647` is still
    running, and likely won't finish before the assignment is due.  Remember,
    this assignment is about compiling and running Java programs from the
    command line, and passing arguments from the CLI to `main()`.  It is *not*
    about algorithms.  Don't go down the optimization rabbit hole.



----------------------------------------------------------------------------
# How do I use Git to submit my homework?

I amended this document to include detailed instructions about setting up
your first git repository:

* [Git repository set up instructions](../Git_Repository_Setup.md)

These eight fundamental git commands are enough to succeed in my class:

1.  ~~git status~~
2.  ~~git init~~
3.  ~~git add~~
4.  ~~git config~~
5.  ~~git commit~~
6.  git remote
7.  git push
8.  ~~git log~~

On Wednesday we covered the ~~struck through~~ commands; today I'll show you
how to use the remaining commands.




Lecture 4: Module0\Sep_04\README.md
================================================================

CS3100 - Module 0 - Lecture 04 - Wed Sep 04

# Announcements

## Free software and Linux Club
*   Opening meeting tonight - 6pm @ ESLC 053
*   Get acquainted with Linux and Open Source Software


## [DC435](https://dc435.org): DefCon 2019 lessons learned
*   7pm Thursday, Sept 5th
*   Bridgerland Technical College @ 1301 N 600 W - Room 840

DC435 is our local chapter of the DefCon computer security conference scene.
It is a friendly place to dip your toes into the world of cybersecurity.

DC435 meets at 7:00pm every First Thursday of every month.



# Call on 2 designated questioners

# Topics:
* Interfacing with the Operating System via the command line
* Linux command line guide
* Using command line arguments in your code


----------------------------------------------------------------------------
# Interfacing with the Operating System via the command line

There are many ways to interact with a computer.  Human Computer Interaction
(HCI) researchers recognize four [1]:

<details>
<summary>1. Instructing</summary>

Telling the computer what to do through shortcut keys, buttons, typing strings
of characters. Quick and prompt feedback.

</details>


<details>
<summary>2. Conversing</summary>

Holding a back-and-forth dialog with a computer
* Wizards
* Pop-up dialog boxes
* Context-sensitive menu systems
* Prompts

</details>


<details>
<summary>3. Manipulating</summary>

Leverage users' knowledge of the "real-world" through analogs to familiar
concepts:

* Desktop
* Icons
* Files
* Folders
* Trash bin
* Point-and-click
* Drag-and-drop

Characterized by continuous representation of the interface (the desktop is
always present), use of direct physical actions as opposed to abstract textual
instructions.

</details>

<details>
<summary>4. Exploring</summary>

Moving through virtual or physical environments.

* Virtual reality
* Augmented reality
* "It's a UNIX system, I know this!"

</details>

[1] Interaction Design: Beyond Human-Computer Interaction (4e). Preece, Rogers,
Sharp; Wiley, 2015. pp 47-54


## Discuss with your study buddies:

* What categories do you think a Command Line Interface (CLI) fall into?
* What categories do you think a Graphical User Interface (GUI) fall into?
* Into which categories would you place a voice-activated assistant?
* How about an Augmented Reality (AR) interface?
* These four categories don't have to be the end-all-be-all of ways humans may
  interact with computers.
  * What other categories might you propose?
  * How would your scheme re-arrange things?




----------------------------------------------------------------------------
# [Unix command line guide](../Unix_CLI.md)


----------------------------------------------------------------------------
# Using command line arguments in your code

Let's write a simple Java class called `Args` that inspects its own
command-line arguments which are passed in as an array of String objects to the
`main()` method.

This program can be built using this command (remember that the '$' represents
your shell's prompt):

    $ javac Args.java

And may be run with zero arguments:

	$ java Args 


Or many arguments:

	$ java Args 1 2 3 4 5


Special arguments called *switches* or *options* may be given which instruct
the program to perform special actions.  

	$ java Args -add 1 2 3 4 5

	$ java Args -mul 1 2 3 4 5


The meaning of a switch is entirely up to each program.  Different programs can
interpret a switch like `-r` in totally different ways.


Lecture 5: Module1\Sep_06\README.md
================================================================

CS3100 - Module 1 - Lecture 05 - Fri Sep 06

# Call on 2 designated questioners


# Topics:
* Mud Card review
* Assignment #1 Overview
* Build Systems
* Java Build Systems Shootout


----------------------------------------------------------------------------
# Mud Card review

There were a lot of remarks regarding the Human-Computer Interaction
implications of an Iron Man style UI; with respect to both the immersive,
holographic display and the Jarvis/F.R.I.D.A.Y. AI assistant.

Y'all are a bunch of nerds.

Some choice remarks:

> Command line interface would probably include instructing and conversing.  It
> is generally difficult to explore a command line interface unless they have
> really good feedback or a --help menu.

A new category of UI based upon body gestures:

> Something for interacting with objects in a 3D projected reality.  Iron Man
> interface style, or the gloves that replace keyboards. Perhaps that still
> fits in "manipulating", but I feel it's a big difference going from the mouse
> to using my own body movements. I also think having a headset/goggles/glasses
> is different than when it's projected in front of you.

> I feel like every operating system needs to allow all four categories.  It
> would be a bad OS if you couldn't communicate or manipulate data.  There's
> always some help function or file structure to explore, and of course, the
> computer has to converse.


----------------------------------------------------------------------------
# Assignment #1 Overview

https://usu.instructure.com/courses/547959/assignments/2699282



----------------------------------------------------------------------------
# Build Systems

Real-world software systems are too large for a single person to develop alone,
much less comprehend or even build.  A typical end-user application consists of
millions of lines of code written in many different languages.

For example, as of last night the source code for the LibreOffice.org office
software consists of 14,601 files written in as many as 16 different languages,
totalling over 4.5 million lines of code.

	SLOCCount, Copyright (C) 2001-2004 David A. Wheeler
    ===================================================

	Totals grouped by language (dominant language first):
	cpp:      4,116,554 (90.27%)
	java:       276,446 (6.06%)
	python:      61,443 (1.35%)
	C:           36,805 (0.81%)
	perl:        32,075 (0.70%)
	sh:          12,550 (0.28%)
	yacc:        10,832 (0.24%)
	cs:           6,600 (0.14%)
	objc:         1,948 (0.04%)
	lex:          1,880 (0.04%)
	awk:            978 (0.02%)
	pascal:         940 (0.02%)
	asm:            866 (0.02%)
	php:             79 (0.00%)
	csh:             20 (0.00%)
	sed:              5 (0.00%)

	Total Physical Source Lines of Code (SLOC)                = 4,560,021
	Development Effort Estimate, Person-Years (Person-Months) = 1,389.78 (16,677.33)
	 (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
	Schedule Estimate, Years (Months)                         = 8.38 (100.54)
	 (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
	Estimated Average Number of Developers (Effort/Schedule)  = 165.87
	Total Estimated Cost to Develop                           = $ 187,739,998
	 (average salary = $56,286/year, overhead = 2.40).


### Questions to consider with your study buddies

* Do these files make up a single executable, or a suite of related programs?
* How do you begin compiling all of these files?
* Once you've compiled them, how do you link them together?
* How long do you think it takes to compile all of these files?
* What happens if there is a build failure along the way?
* What if there is a bug in one out of the 14,601 files?  When you fix it, must
  you start from the top and rebuild everything?


Build systems are software which automate task of building software.  As
software systems grew larger and larger the task of assembling the finished
product became more and more difficult.  More automation was needed to make
this process faster, easier, and to reliably deliver a consistent output.
Increasingly sophisticated tools have evolved to meet these needs.

The evolution of these tools might be explained in this progression:

1.  Compiler commands manually entered
2.  Shell scripts collecting compiler commands into one, repeatable program
    -   Build scripts
3.  Declarative domain-specific programming languages for orchestrating the selective execution of build scripts
    -   Unix make
    -   GNU make
4.  Declarative domain-specific programming languages to simplify the creation of build scripts
    -   GNU Autotools
    -   CMake

*   [https://en.wikipedia.org/wiki/Build_automation](https://en.wikipedia.org/wiki/Build_automation)
*   [https://en.wikipedia.org/wiki/Software_build](https://en.wikipedia.org/wiki/Software_build)


Let's build a small C++ project by hand as a way of illustrating why automation
is desirable.

[Build tool demo for C++](buildsys/)


----------------------------------------------------------------------------
# Java Build Systems Shootout

There are three dominant build systems in the Java ecosystem:

* Ant
* Maven
* Gradle

In this class we use Gradle.  I hope that this demonstration illustrates why
Gradle is superior to the other options.

[Java Build Tools Comparision](https://technologyconversations.com/2014/06/18/build-tools/)

    $ git clone https://github.com/vfarcic/JavaBuildTools
    $ cd JavaBuildTools

Ant is controlled by the files `build.xml` and `ivy.xml`

    # build with Ant -> build/jar/java-build-tools.jar
    $ ant jar


Maven is controlled by `pom.xml`.  It must also connect to a "repository" on
the internet to function.  I'm not entirely sure what happens when the network
goes down...

    # build with Maven -> target/java-build-tools-1.0.jar
    $ mvn package


Gradle is controlled with the file `build.gradle`.  It also starts and leaves
running a background process to facilitate future builds.

    # build with Gradle -> build/libs/JavaBuildTools-1.0.jar
    $ gradle tasks jar


*Note: if the Gradle build fails, edit `build.gradle` and remove the 'task
wrapper' block at line 17*


## [Gradle Wiki](https://usu.instructure.com/courses/547959/pages/gradle-wiki)



Lecture 6: Module1\Sep_09\README.md
================================================================

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



Lecture 7: Module1\Sep_11\README.md
================================================================

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



Lecture 8: Module1\Sep_13\README.md
================================================================

CS3100 - Module 1 - Lecture 08 - Fri Sep 13

# Announcements

# Call on 2 designated questioners


# Topics:
* 2.3 How do function parameters cross from user into kernel mode?
* 2.4 Types of syscalls
* 2.5 System programs



--------------------------------------------------------------------------------
# 2.3 How do function parameters cross from user into kernel mode?

There are three primary methods:

## 1. CPU registers

* Pros: Registers are really fast; this works just like an ordinary function call
* Cons: CPU registers are very small and few


## 2. A block or table of memory; just put the address to this block into one register
This is the method used by Linux and Solaris

* Pros: No size limit
* Cons: Slower than registers

![Figure 2.7](Figure-2.7.jpg)


## 3. The program call stack

* Pros: Convenient for the CPU/Kernel to use; more space than registers
* Cons: Same as #2


This choice defines an *Application Binary Interface* (ABI)

The reason a C++ program which performs an I/O operation can be compiled and
run on different Operating Systems (e.g. Linux and Windows) is *not* because
each of those OSes use the same underlying system call API for I/O.  It is
because the C++ language's system-call interface handles those details for you.



----------------------------------------------------------------------------
# 2.4 Types of syscalls

System calls are how your application makes use of the services that the
Operating System provides.  Looking forward to Assignment 2, you will be
studying system calls from these categories:


## Process Control

+ chdir()
+ nice()
+ sleep()
+ fork()
+ wait()


## File Management

+ open()
+ read()
+ write()
+ close()
+ mkdir()
+ stat()
+ link()
+ symlink()
+ unlink()


## Device Management

+ dup2()
+ sync()
+ ioctl()


## Information Maintenance (find out info about my own process)

+ getcwd()
+ getpid()


## Communication

+ kill()
+ msgget()
+ msgrcv()
+ msgsnd()
+ semctl()
+ semget()


## Protection

+ ulimit()
+ chgrp()
+ chmod()
+ chown()
+ chroot()
+ access()



## How Context Switches happen

Remember that a context switch is when your process makes a system call which
causes kernel code to run, and the CPU changes from user mode into the kernel
mode

1. Execution control passes from my user process into the system call's function in the kernel
2. The CPU hardware switches into its privileged mode (a.k.a. kernel mode)
3. The kernel is allowed to a privileged operation
4. Finally, when the privileged operation is complete, the execution control returns to the calling process

![System calls require a context switch](Figure-2.6.jpg)



----------------------------------------------------------------------------
# 2.5 System programs

Many system programs on Unix are simple programs providing a command-line
interface to an API call of the same name:
 
* `chgrp`
* `chmod`
* `chown`
* `chroot`
* `mkdir`
* `nice`
* `sleep`
* `stat`
* `ulimit` (see note below)

Other system programs don't share the name of the system call they wrap, but otherwise 

* cd  -> `chdir()` (see note below)
* ln  -> `link()` and `symlink()`
* rm  -> `unlink()`
* pwd -> `getcwd()` (see note below)

*Note*: `ulimit`, `cd` and `pwd` aren't technically *system programs* but
rather conveniece commands provided by your shell (e.g. bash)





Lecture 9: Module1\Sep_16\README.md
================================================================

CS3100 - Module 1 - Lecture 09 - Mon Sep 16

# Announcements


## Hill AFB STEM Recruitment

Juniors: Come get an internship this coming summer.  Visit the table downstairs
on 1st floor of ENGR.  Interviews next week.

If you want to get your Master's degree, Hill will *pay* you to do it!
You don't have to show up to work while you're in school.

Seniors: We're looking for new hires *right now*.  Bring a resume today or
tomorrow to 1st floor of ENGR, visit a hiring supervisor right away.


## FSLC Guest Presentation: Thomas Hatch & Tyler Johnson of SaltStack 

I am pleased to announce two special guests from SaltStack will visit our next
meeting.

SaltStack is a Utah tech-startup that created an open-source project called Salt.
Salt is a Python-based configuration management software and remote execution engine.

Thomas Hatch & Tyler Johnson will introduce *Plugin Oriented Programming*
(POP), an exciting, new way to design large-scale software projects.  Learn
what it's like to work on an real-life project and how *you* can get involed in
open-source development right now.

Pizza will be provided.

ESLC 053 at 6PM Wednesday 9/18




# Call on 2 designated questioners


# Topics:
* 2.6.2 Mechanisms vs. Policies
* 2.6.3 OS Implementation
* 2.7 Operating System Structure
* The Tanenbaum–Torvalds debate

----------------------------------------------------------------------------
# 2.6.2 Mechanisms vs. Policies

#### Mechanism
* *How* to do something
* The actual, nitty-gritty code

#### Policy
* *What* to do when a mechanism is to be enacted
* *When* to enact a mechanism
* The "rules"

These ideas are separated from each other to maximize flexibility


## Examples of Policies:

* All processes must have a unique ID number
* Users can't access files belonging to other users
* Processes cannot access the memory of other processes


## Examples of Mechanisms:

* Maintain a list of in-use PIDs, don't assign a new process a number from that list
* User and group ownership of filesystem objects; permission bits on each file and directory
* Process ownership of memory regions; permission bits in the kernel's memory table



----------------------------------------------------------------------------
# 2.6.3 OS Implementation

OSes historically were written in assembly language (ASM)

*   ASM is tightly related to a particular CPU
*   OSes were tightly related to particular CPUs
*   An OS needs to be super-efficient, ASM gives high level of control


OSes now are written in high-level languages, primarily C and C++

* As compiler technology improves, so can the OS (sort of a "for free"
  performance improvement)
* Easier to write, debug and port to other kinds of hardware


#### Port(v)
To refactor/rewrite software designed to operate on one platform to run on
another



----------------------------------------------------------------------------
# 2.7 Operating System Structure

## MS-DOS - 'member DOS?
* MS-DOS was designed to be light on resources
* not a multitasking, multi user system - didn't need to be complex
* example of a monolithic system

![Figure 2.9](Figure-2.9.jpg)

#### Monolithic
1. Formed of a single large block of stone
2. (Of an organization or system) large, and intractably indivisible and uniform

### Advantages of Monolithic design
* Small - less to go wrong, more reliable
* Small - much less resource intensive
* Cheap to develop, maintain, etc.


### Disadvantages of Monolithic design
* Difficult to update - can't do a live update
* If there are parts of the OS I just don't need (e.g. a device driver for
  a mouse I don't have), I'm out of luck and have to spend the RAM on
  holding it in memory
* inflexible for different users - difficult to customize to your needs
* Single point of failure - if part of it crashes, the whole thing crashes






----------------------------------------------------------------------------
# 2.7.2 The Layered Approach to OS design

![Figure 2.13](Figure-2.13.png)

What are the layers?

1. Hardware
2. Device drivers
3. ???
N. User interface / API


## Microkernel OSes
![Figure 2.14](Figure-2.14.png)

Kernels tend to become big and complex over time. More complexity -> more bugs in the privileged lower layer.

Carnegie Mellon University developed _Mach_, a modular, microkernel OS

Only the most important services remain in the kernel (Layer 0)

Other services are implemented as daemons which communicate via message passing


### Advantages of Microkernel design
* Security advantages - if you hack a daemon, you didn't hack the whole OS
* No single point of failure
* Only use what you need
* Divide the labor of design & development

### Disadvantages of Microkernel design
* More costly in terms of memory, CPU time, etc.
* Must necessarily be a multi-tasking system
* Message passing becomes a bottleneck (vs. shared memory)
* More interactions and interdependencies => more potential for bugs
* Smaller attack surface means fewer critical vulnerabilites


## Hybrid approach: Loadable kernel modules

Tries to give the best of both worlds; a monolithic kernel can have a small
core, but pick and choose new parts to load into memory

On Linux these system programs are used to inspect and manipulate kernel
modules:

* lsmod
* rmmod
* insmod
* modprobe



### Advantages of loadable kernel modules
* Easier to port the OS to different architectures
* If there are parts of the OS I just don't need (e.g. the driver for a Wacom
  pen), I don't need to load it



--------------------------------------------------------------------------------
# The Tanenbaum–Torvalds debate

A.K.A. The flame war to end all flame wars on Usenet.  Usenet was a message
board built using pre-web technologies.  It was most popular among college
students/faculties and computer power users from the early 80's through the mid
90's.  It's decline began in 1993 when America Online made it accessible to
normies.  The advent of the world-wide web and increasing use by pirates 

Structurally and culturally I'd say it most resembles Reddit; users made posts
to newsgroups organized by topics.  Unlike Reddit, Usenet newsgroups were
organized hierarchically.

* [The original Usenet discussion](https://groups.google.com/d/msg/comp.os.minix/wlhw16QWltI/XdksCA1TR_QJ)
* [Wikipedia's write-up](https://en.wikipedia.org/wiki/Tanenbaum%E2%80%93Torvalds_debate)


## Tanenbaum: LINUX is obsolete

* Writing a monolithic kernel in 1991 is "a giant step back into the 1970s"
* Linux is too-closely tied to the 80386 processor, which won't catch on
* Being monolithic and specific to the 80386 means Linux will be unportable

> Don't get me wrong, I am not unhappy with LINUX.  It will get all the people
> who want to turn MINIX in BSD UNIX off my back.  But in all honesty, I would
> suggest that people who want a **MODERN** "free" OS look around for a
> microkernel-based, portable OS, like maybe GNU or something like that.



## Torvalds: Time for some serious flamefesting!

> I'd like to be able to just "ignore the bait", but ...  

* You make Minix as a hobby; I make Linux as a hobby, but I don't use that as
  an excuse for poor performance. "Linux still beats the pants of minix in
  almost all areas"
* I agree that micro-kernels are nicer, but "minix doesn't do the micro-kernel
  thing very well, and has problems with real multitasking" (read: multithreading)
* Linux may be less portable, but using the advanced 80386 features simplifies
  its design



Lecture 10: Module2\Sep_18\README.md
================================================================

CS3100 - Module 2 - Lecture 10 - Wed Sep 18

# Announcements

## Computer Science Department Fall Opening Social

Today 3pm at the USU Challenge Course


## FSLC Guest Presentation: Thomas Hatch & Tyler Johnson of SaltStack 

I am pleased to announce two special guests from SaltStack will present at our
FSLC meeting tonight.

SaltStack is a Utah tech-startup that created an open-source project called Salt.
Salt is a Python-based configuration management software and remote execution engine.

Thomas Hatch & Tyler Johnson will introduce *Plugin Oriented Programming*
(POP), an exciting, new way to design large-scale software projects.  Learn
what it's like to work on an real-life project and how *you* can get involed in
open-source development right now.

Pizza will be provided.

ESLC 053 at 6PM Wednesday 9/18


## Fall STEM Career Fair

Next Monday 9/23 @ the TSC

Dust off your resumes


# Call on 2 designated questioners


# Topics:
* Assembly language system call demo
* Assignment #2 - Black box process lab
* Raspberry Pi Setup


----------------------------------------------------------------------------
# [Assembly language system call demo](asm_syscall_demo/README.md)


----------------------------------------------------------------------------
# [Assignment #2 - Black box process lab](https://usu.instructure.com/courses/547959/assignments/2762738)


----------------------------------------------------------------------------
# Raspberry Pi Setup


## Using the Raspberry Pi

This mini computer uses an HDMI port for display output.  It has four USB ports
suitable for a mouse and keyboard.  The included microSD card functions as the
RPi's hard disk.  The RPi has an Ethernet port and a WiFi adapter for network
connectivity.  You may plug it into a TV or computer screen, or you may access
it "headless" over the internet via SSH (advanced).


## Installing and setting up your Raspberry Pi

See the instructions in the assignment description on [Canvas](https://usu.instructure.com/courses/547959/assignments/2762738)

### [Connecting to your RPi remotely](../Remote_RPi.md)


Lecture 11: Module2\Sep_20\README.md
================================================================

CS3100 - Module 2 - Lecture 11 - Fri Sep 20

# Announcements

## If you don't have a Raspberry Pi for Assignment #2

Contact me to check one out.


## Fall STEM Career Fair

Come network with some of the top firms in the science, technology,
engineering, and mathematics industries! This is a great way to take advantage
of setting up your next internship or full-time job after graduating college.
Also, expand your net work by meeting recruiters face-to-face. Companies span
from the FBI to IM Flash!

Monday 9/23 3pm-7pm @ the TSC


## CyberSecurity Special Interest Group meeting

Tuesday 9/24 6pm @ HH326

Ryan Beckstead will be presenting on how to clean up your computer, scan for
viruses and some router configurations.   

If you've expressed interest in competing in the DOE Cyberforce competition in
November, this is the place to be.



# Topics:
* 3.1 What is a process?



----------------------------------------------------------------------------
# 3.1 What is a process?


*Remember:* a process and a program are two different things

#### Program
Code sitting idle on a disk

#### Process
A program that is executing



A program has certain regions of data which do different things in the running process.

#### Text Section
Part of a program containing machine-code instructions

#### Data section
Part of a program containing hardcoded data & global variables




Certain parts of a process don't exist on disk: they are only needed when the
process is executing

#### Program Counter
CPU Register pointing to the next instruction to run

#### Stack
region of memory containing temporary data used by the process for local
variables and function calls

#### Heap
region of memory which the program may allocate as needed. can also be deleted as needed.


![Figure 3.1 - Stack and Heap regions of memory](Figure-3.1.png "Stack and Heap regions of memory")



We can inspect the regions of a program on Unix with the ```objdump``` utility

    $ objdump -Ssdx executable | less




## 3.1.2 What states may a process be in?

This is not an exhaustive list, nor are these exact names used across all OSes.
But these concepts do exist across all modern OSes.

* New - The process is being created by the OS but hasn't yet started executing
* Running - The instructions in the process's text section are being executed
* Waiting - The process is waiting for an external event (I/O, Signal, etc.)
* Ready - The process is done waiting, and may be taken up by the next available CPU
* Terminated - The process has finished and the OS is in the midst of cleaning it up

This figure describes the lifecycle of a process on our system from birth to death.

![Figure 3.2 - Process state lifecycle state chart](Figure-3.2.png "Process state lifecycle state chart")

As you run and watch your programs, see if you can determine which system calls
cause a process to move from the running queue onto the waiting queue.




## 3.1.3 How does the OS keep all of this straight?

What information might the kernel need to remember about a process? 

* Position of the instruction pointer
* State of CPU registers
* State of the call stack
* PID
* Open sockets, files, other data resources


#### Process Control Block (PCB)

![Figure 3.3 - PCB diagram](Figure-3.3.png "PCB diagram")


Where it makes sense, the PCB will maintain separate copies of some of the
above information for each *thread* within a process.

The data recorded within the PCB is also known as the *context* of the process



Lecture 12: Module2\Sep_23\README.md
================================================================

CS3100 - Module 2 - Lecture 12 - Mon Sep 23

# Announcements

## Fall STEM Career Fair

Come network with some of the top firms in the science, technology,
engineering, and mathematics industries! This is a great way to take advantage
of setting up your next internship or full-time job after graduating college.
Also, expand your net work by meeting recruiters face-to-face. Companies span
from the FBI to IM Flash!

Monday 9/23 3pm-7pm @ the TSC


## CyberSecurity Special Interest Group meeting

Tuesday 9/24 6pm @ HH326

Ryan Beckstead will be presenting on how to clean up your computer, scan for
viruses and some router configurations.

If you've expressed interest in competing in the DOE Cyberforce competition in
November, this is the place to be.


# Action Items

0.  Run the `blackbox` program and find the menu item that corresponds to the
    memory leak (*Hint: use `htop` to help you indentify which one it is for
    you*).

    What happens on your RPi when the system finally runs out of memory?

1.  Clone this lecture notes repository onto your RPi.  Find today's lecture
    notes, enter the `fork_demos/` directory and build the demo programs with
    the `make` program.

    ```
    git clone https://gitlab.cs.usu.edu/erik.falor/fa19-cs3100-lecturenotes.git
    cd fa19-cs3100-lecturenotes/Module2/Sep_23/fork_demos
    make
    ```

    Play with these programs to see what they do.  Don't worry if you don't
    completely understand the C++ code, but see if you can figure out the gist
    of each.  Watch `htop` while running them.


# Topics:

* 3.2 Process scheduling



----------------------------------------------------------------------------
### What does a PCB look like in real-life?

We can take a peek at the PCB in Linux since it's an Open-Source OS

    $ git clone git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git

This only takes about 20 minutes to download :'(

It's better to make a 'shallow' clone of this repository:

    $ git clone --depth 1 git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
    $ vim linux/include/linux/sched.h +/"struct task_struct {"




----------------------------------------------------------------------------
# 3.2 Process scheduling


### Multiprogramming
Making best use of the CPU

This is done by splitting up the work so that many things can be worked on
simultaneously (apparently, at least).


#### Parallelism
Working on more than one thing simultaneously


#### Concurrency
Splitting up a large task into smaller pieces which you work on a piece at a time


#### Jobs (a.k.a. tasks)

All the stuff a computer needs to do:

* Programs or data which the CPU needs to process
* You may see these in a process viewer tool (i.e. htop, Process Explorer on
  Windows, etc.)


#### Timesharing (a.k.a. multitasking)

This is multiprogramming done by splitting up all of the tasks into little
"timeslices", and doing a little bit of work, then switching to the next task
and doing a little bit of work on it...



## 3.2.1 Scheduling Queues

Keeping a queue of jobs, and prioritizing it based upon whether their needed
resources are available (i.e. I/O)

<details>
<summary>I/O bound</summary>

The limiting factor for a program is waiting for I/O

</details>


<details>
<summary>CPU bound</summary>

The limiting factor for a program is the amount of computation it needs to do.

</details>




## 3.2.2 Schedulers

#### Scheduler
An algorithm for deciding which process should use the CPU and for how long.


#### Degree of multiprogramming
The number of (running) processes that a system holds in memory




## 3.2.3 Context switching

When the scheduler decides that it's time to swap processes between the ready
queue and a waiting queue, it performs a context switch.

It copies the currently-running process's PCB into memory, then restores the
PCB of the process at the front of the Ready queue onto the CPU and begins
executing at its restored instruction pointer.

<details>
<summary>**Q:** Are context switches useful to the user?</summary>

**A:** No. From the user's view of the system, context switching is pure overhead;
it is time that the computer is *not* doing your useful work.

</details>



Lecture 13: Module2\Sep_25\README.md
================================================================

CS3100 - Module 2 - Lecture 13 - Wed Sep 25

# Announcements

## FSLC Bash Course Crash Course

Wednesday 9/25 6pm @ ESLC 053

Linux Hackers calling you a n00b? Feeling sad because your bash skills aren't
up to snuff? Still trying to figure out the difference between `fish` and `zsh`?

Well don't you worry, we at FSLC have a solution for you!

Join us at the biannual **BASH COURSE CRASH COURSE**! iWhere you can make all
your bash dreams come true!  We'll be talking about navigation, file
manipulation, and much more!  Be the envy of your class This Wednesday at
6:00pm in the ESLC room 053!



# Call on 2 designated questioners


# Topics:

* Mud Card Questions
* 3.3 Processes creation and termination



--------------------------------------------------------------------------------
# Mud Card Questions

* Describe what happens when your Raspberry Pi runs out of memory due to
  `blackbox` leaking like a sieve
* Last time we talked about a system call named `fork()`.  How many times does
  this function return?
* How many generations of the `fork_bomb` does it take to crash a Raspberry Pi?

Jot down for me any other questions or ideas that come to mind.


--------------------------------------------------------------------------------
# 3.3 Processes creation and termination

Well, when a mommy and a daddy process love each other very much...

Actually, processes reproduce asexually, like amoeba and bacterium.  A child
process is *nearly* an exact duplicate of its parent, inheriting *all* of its
parent's traits, save one.

This sounds boring and nearly useless: what's the point of having two identical
processes?

Or, it might sound terrifying: how can I tell whether I'm the original or the
clone?

The upshot is that with only one parent per process, the family tree of all
running processes is quite simple:

    $ pstree

On Unix-derived OSes the `fork()` system call creates a new process.



### When a child process is created, how does it know what to do?

As discussed before, a child process is a clone of its parent, inheriting
everything from command-line arguments to variables to open files, memory
space, CPU registers and the instruction pointer.

The only discernible difference between parent and child is: 

<details>
<summary>The child sees that the return value of `fork()` is</summary>

is the number `0`.

</details>


<details>

<summary>The parent sees that the return value of `fork()` is</summary>

the process ID of its child; a positive number

</details>


#### Process ID (PID)
The unique ID number of a running process

We can retrieve our PID with the system call `getpid()`.  It returns an
integer, usually in the range of `2` - `32768`.

By inspecting its PID a process can tell whether it's the original or the
clone.


**Fun Fact:**

You can see what that maximum PID is on your Linux system by reading the file
`/proc/sys/kernel/pid_max`.  If you write a new number to this file *that*
becomes the new maximum PID.



## 3.3.1 How are processes created?

Once a process forks into two processes, there are a few possibilities for what
a parent and its new child process may do next:


### Execution Possibilities

0.  Parent executes concurrently alongside its child e.g. the parent calls
    `wait()` at some later time

1.  Parent process waits for its child to terminate before continuing e.g. the
    parent calls `wait()` immediately



### Address Space Possibilities

0. Child remains a clone of its parent, executing the same program

1. Child loads a new program into its address space, becoming a new process
   e.g. child calls a function from the exec family of system calls to load a
   new program into its address space


[Demo: Fork/exec in C++](../Sep_23/fork_demos/fork_exec.cpp)


* What are the implications for processes created in each of the four ways?

0. two identical processes taking turns
1. two identical processes running in parallel
2. two *different* processes taking turns
3. two *different* processes running in parallel


* What happens if a process forks a child, which goes on to fork a child, which
  goes on to fork a child, ad infinitum?

*Try this out on your RPi!*

[Demo: Fork bomb in C++](../Sep_23/fork_demos/fork_bomb.cpp)



## Important process-related system calls

#### fork()
Splits a process into two identical copies, parent & child
Is called  ...  time(s) and returns  ...  time(s)


#### exec()
Causes a process to overlay its address space with a new program from disk and begin execution as a new process
Is called  ...  time(s) and returns  ...  time(s)


#### wait()
Enables a parent process to block until its child terminates; also communicates the disposition of a child process back to its parent


#### exit()
Inform the OS that this process wants to be removed from the queue of running processes


## 3.3.2 Process termination

On a Unix-derived system, a parent process can find out what happened to its
child from one of the wait family of system calls. In particular, the parent
can know whether the child terminated normally or abnormally (return 0; at the
end of its `main()`), or whether a child terminated due to receipt of a fatal
signal (e.g. `SIGKILL`, `SIGABRT`, etc.). For this reason, information about
processes which have terminated is maintained by the kernel until the parent
process asks for it.

#### reap
Collecting the final disposition of a child process, allowing the OS to remove
the terminated child process from its records.  This is accomplished on
Unix-derived OSes with a member of the `wait` family of system calls:

* `wait()`
* `waitpid()`
* `waitid()`


#### zombie
A process which has terminated but whose parent hasn't yet called `wait()` on its
behalf.

[Demo: Zombies! in C++](../Sep_23/fork_demos/zombies.cpp)



Lecture 14: Module2\Sep_27\README.md
================================================================

CS3100 - Module 2 - Lecture 14 - Fri Sep 27


# Call on 2 designated questioners


# Topics:

* Mud card
* 3.4 Interprocess Communication (IPC)


--------------------------------------------------------------------------------
# Mud card responses from Sep 25

*   A lot of students reported that they haven't yet run `blackbox`.  What's
    the hold up?
    -   `Ctrl-Alt-T` will open a terminal, so you can use the RPi without a mouse

*   "Why are there 2 man pages for the `wait` command?  If I run `man wait`, I
    get a man page, so what's the deal with the other one?"

*   "How to configure my RPi to be accessible over SSH?"
    -   Did you know about this document?
        https://gitlab.cs.usu.edu/erik.falor/fa19-cs3100-lecturenotes/blob/master/Module2/Remote_RPi.md

*   Review the `fork_exec` program from last time
    -   Add prompts to slow the process down
    -   In Windows and in Java, the `fork()/exec()` pair of functions is
        represented by a single function.  You'll become familiar with this
        style in the next assignment.


--------------------------------------------------------------------------------
# 3.4 Interprocess Communication (IPC)


## 3.4.1 Shared Memory

A process can designate a region of its own address space to be open for other
processes to access. As C++ programmers, you know only too well that such
access ordinarily results in a Segmentation Violation. Setting up a region of
shared memory tells the OS to chill out about this. It is then up to the
processes to coordinate access; the OS won't help you keep things straight.


Two processes engaging in this sort of sharing may take on the roles of
producer and consumer:


#### Producer
Creates information for a consuming process


#### Consumer
Consumes information from a producing process

You might also think of this along the lines of the server/client metaphor.
Note that these roles are not fixed; processes may alternate between these
roles.



### Blocking vs. Non-Blocking behavior

A function call *blocks* if execution pauses until the operation completes.

    if (0 == fork()) {  // child process
        sleep(10);
        exit(1);
    }
    else {              // parent process
        pid_t kid = wait(NULL); // this call BLOCKS until the child process terminates
        cout << "My poor child " << kid << " has perished!\n";
    }


Two types of shared memory buffers
----------------------------------
#### bounded buffer: buffer size has a limit
The consumer may have to wait if the buffer is empty, and the producer may have
to wait for the consumer to remove items when the buffer becomes full


#### unbounded buffer: buffer size is not limited
The consumer may have to wait if the buffer is empty, but the producer will
never experience a "full" buffer





## 3.4.2 Message Passing

* This technique allows processes to synchronize without sharing address space.
* It is particularly useful in a distributed environment (i.e. across a
  network), but the principles are still commonly applied within a standalone
  system

Two primitive operations are provided by any message passing system:

* `send()`
* `receive()`

There are many implementation choices to be made in a message-passing system:

### Direct vs. Indirect communication

#### Direct communication
The sender knows the name of the recipient

#### Indirect communication
The sender puts messages in a "mailbox" without needing to know the recipient




### Synchronous Communication
`send()`/`receive()` methods *block* until the other side does something with the message


#### Blocking send()
I wait until somebody takes the message from my hand; the mailbox can be size 0 in this case


#### Blocking receive()
The `receive()` method blocks until a message arrives


At first blocking may sound like a bad thing because it puts a stop to our
program.  It can be very useful as it allows us to coordinate two or
more running processes.  We can control the pace of execution of processes by
causing a *rendezvous*.


#### Rendezvous
When both the sender and the receiver block, they are at that moment, paused at
known positions in their code



However, there are times when mutually blocking programs can get stuck in such
a way that they cannot become unstuck...

#### Deadlock
When two or more processes are mutually waiting upon each other for an event
that will never happen (because they're both blocking)





### Asynchronous Communication
`send()`/`receive()` methods appear to return instantaneously, whether or not
the other side has responded to the message.

##### Non-Blocking send
The `send()` method returns immediately, regardless of what the recipient does


##### Non-Blocking receive
The `receive()` method either immediately returns a valid message or NULL.  In
this case the recipient will check for a message later.




### Automatic buffering vs. Explicit buffering

Since our processes are not sharing memory directly, there is a data structure
in the kernel which acts as a buffer or a queue for our messages. There are
three possibilities for implementing this queue:


#### Zero capacity
The queue has a max length of zero; the sender and receiver must rendezvous to
hand the message over


#### Bounded capacity: The queue has a finite length
send() behaves asynchronously until the queue is full, at which point the
send() operation becomes blocking


#### Unbounded capacity
The queue has infinite length and the sender never blocks (until the OS crashes
due to lack of memory)


Message passing is typically *slower* than shared memory.

If it's slower, why use it?
* Much easier to make a distributed (i.e. cluster) system than with shared memory
* Execution synchronicity and predicability - rendezvous
* *Portability:* I don't have to worry as much about details of memory layout, OS version, etc. (TCP/IP is a prime example of this)
* *Atomicity:* A message is a discrete unit - you either get it, or you don't



Lecture 15: Module2\Sep_30\README.md
================================================================

CS3100 - Module 2 - Lecture 15 - Mon Sep 30


# Topics:
* Mudcard activity: Compare/Contrast Shared Memory and Message Passing
* 4.1 What are the advantages of multiprocessing?
* 4.2 Multicore programming
----------------------------------------------------------------------------
## Mudcard activity: Compare/Contrast Shared Memory and Message Passing


Discuss with your study buddies these questions.  Record your ideas and
questions on your mudcards.

*   Can a process share memory with another process without getting the OS
    involved?

*   Can a process pass a message to another process without getting the OS
    involved?

*   What does "blocking" mean?  Give an example.

*   What does "non-blocking" mean?  Give an example.

*   What do you think happens to the sender when a message is put into a
    bounded-capacity message queue that is not full using blocking `send()`?

    *   What happens to the sender when that queue is full?
    
    *   What if the queue uses non-blocking `send()`?

*   Describe what happens when messages are exchanged over a zero-capacity
    buffer using blocking `send()`/`receive()`


----------------------------------------------------------------------------
## 4.1 What are the advantages of multiprocessing?

* Prevent the appearance of "freezing"
* You can get things done faster; slow programs can wait in parallel, and I'm
  always using the CPU to the fullest
* Support multiple users on one computer



What could happen if we let individual processes partake in multiprocessing?

#### Responsiveness
Your application can do slow stuff "in the background" while the UI always appears to be "fast"

#### Resource sharing
Separate "processes" can share memory space w/o needing to get the OS involved

#### Economy
Spawning threads uses less overhead than forking; context switching between threads is quicker than processes, too


### Behold, THREADS!

One program image with a single, unified memory space, multiple call stacks and PCBs to enable one program to use multiple CPU cores at once!

![Figure 4.1](Figure_4.1.png)



### 4.2.1 Challenges of multithreaded systems

1. Finding Tasks
    *   What can be done in parallel?

2. Balance
    *   If we parallelize, do we gain enough speed to offset the overhead?

3. Data Splitting (Spillman data massage program)
    *   Can the data be partitioned among threads? If it can, we call this an
        "embarassingly parallel" problem.
    *   Examples: Image processing

4. Data Dependencies
    *   Can we partition the data such that threads don't need to be
        "downstream" from other threads?
    *   An assembly line (or our shell's pipelines) aren't parallel systems

5. Testing & Debugging
    *   When there's more going on, there's more to go wrong.
    *   Debugging parallel systems is *notoriously* difficult


----------------------------------------------------------------------------
### 4.2.2 Types of parallelism

#### Data parallelism
Distribute subsets of data across cores & do same operations on different data

Example: GPUs rendering a 3D scene

#### Task parallelism: each core/thread is doing different operations

Example: GUI application where 1 thread manages the UI, and other threads do
slow tasks "in the background"

Real Talk - this isn't an either-or proposition.  Most applications are a hybrid
of these two approaches.



Lecture 16: Module3\Oct_02\README.md
================================================================

CS3100 - Module 2 - Lecture 16 - Wed Oct 02

# Announcements

## FSLC meeting tonight

[piVPN](https://github.com/pivpn/pivpn)

Simple OpenVPN installer, designed for raspberry pi

* Wednesday, 10/2
* 6pm @ ESLC 053




## DC435 meeting this Thursday

**Docker + ELK == win by Jeff Murray**

* Learn how to spin up elk instance inside docker and stuff
* We currently meet at Bridgerland Technical College campus
* 1301 N 600 W, Logan
* Room 840
* The room will open at 6:30 and meeting will kick off at 7:00pm.


# Call on 2 designated questioners


# Topics:
* Introduce Assignment #3
* 4.2 Amdahl's Law and the limits of multicore programming
* 4.3 What implementations of multithreaded systems exist?


----------------------------------------------------------------------------
# Introduce [Assignment #3](https://usu.instructure.com/courses/547959/assignments/2699284)

The infamous Command Shell assingment.

I've given you an extra week to work on this assignment: it's not due until
*after* fall break.  Don't procrastinate!  It really is this big of an
assignment!


----------------------------------------------------------------------------
# 4.2 Amdahl's Law and the limits of multicore programming

One processor juggling four tasks can use concurrency to spread the work out
evenly such that a little slice of each task gets its turn on the CPU
frequently and fairly:

![Figure 4.3](Figure_4.3.png)


When we add more CPUs we can do N things at once, leading to a speedup of a
factor of N:

![Figure 4.4](Figure_4.4.png)


A problem I can avoid simply by throwing money at it?  I love these!  And I'm
positive that there are no downsides or pitfalls at all!


### Amdahl's Law

![Amdahl's Law](amdahls_law.jpg)


The meaning of the variables in this image:
===========================================

* `S_N` = speedup I get from N CPUs
* `P` = proportion of the code which is parallel in nature
* `N` = # of CPUs


What do you think happens as `N -> +inf`?

[Amdahl's calculator](https://docs.google.com/spreadsheets/d/1BCEXj0oc7Nwfnq-cureAlqPQ_a6Vu7mPshjZCn95VCg/edit?usp=sharing)

*   Adding extra cores becomes less helpful
*   The total possible speed-up becomes the reciprocal of the proportion of the
    program that runs serially
    *   The less serial code there is the faster we can go
    *   Unfortunately, minimizing the amount of serial code is *really hard*


----------------------------------------------------------------------------
# 4.3 What implementations of multithreaded systems exist?


#### User Threads (a.k.a. Green Threads)
All of threads' bookkeeping is handled in user space

**User Thread Pros**
*   Fewer system calls = less OS overhead
*   Not terribly difficult to implement in some languages
*   Implementation may benefit from language/app-specific insight

**User Thread Cons**
*   Very difficult to implement in some languages
*   Each language/runtime system re-invents this wheel
*   Can't leverage multiple cores
*   When one thread makes a blocking system call *the entire* app is blocked

Green Threads were so named because they were created by the Green team at Sun
Microsystems for use in early versions of the Java Virtual Machine (the modern
JVM uses *real* multithreading).  It is still used by many programming
languages which claim to support "threading".  Because you can't *really* use
all of your CPUs this way, Java and C++ folks don't consider this to be _real_
threading.




#### Kernel Threads
All of threads' bookkeeping is handled by the OS

![Light Weight Process](lwp.png)

**Kernel Thread Pros**
*   All programs can benefit from a well designed scheduler (the OS has to do this anyway)
*   Can utilize separate CPU cores

**Kernel Thread Cons**
*   Thread operations are now a system call
*   Kernel bloat



## Pop Quiz - can you identify the type of threading?

I've written the same program in a few different programming languages.  Each
program spawns the following threads:

*   1 main thread which starts up the worker threads, then waits for them to
    finish (they won't...)
*   6 CPU-bound worker threads which increment `a` in a forever loop
*   1 I/O-bound worker thread which copies data from a slow disk device

Can you tell which implementation of threading (**kernel** vs. **user**) each
language uses just from watching the CPU graph in `htop`?

[Threads demo](../threads)

| Language | Program          | Threading implementation
|----------|------------------|-------------------------
| C++      | `threads.cpp`    | Kernel threads
| Scheme   | `threads.scm`    | User/Green threads
| Python2  | `threads_py.py`  | Hybrid (I/O can be done in parallel, CPU work is serial)
| Python3  | `threads_py.py`  | Hybrid - idem.
| Cython3  | `threads_py.py`  | Hybrid - idem.
| Java     | `threads.java`   | Kernel threads



Lecture 17: Module3\Oct_04\README.md
================================================================

CS3100 - Module 3 - Lecture 17 - Fri Oct 04


# Call on 2 designated questioners


# Topics:
* 4.3 What implementations of multithreaded systems exist?
* 4.5 Cool Pool Party
* 4.6 What could possibly go worng with threading?


----------------------------------------------------------------------------
## 4.3.1 Many-to-one threads

For every user-space process there is at least one thread running in the kernel
ready to handle its system calls.

![Many to One](many-to-one.png)

In this scheme many user-level threads share a single kernel thread.  When a
system call is made by one of the threads, the kernel thread is unavailable to
other threads within the process.




## 4.3.2 One-to-one

Each user-space thread gets its own kernel thread.

![One to one](one-to-one.png)

**One-to-one Pros**
* I/O-bound threads truly don't block the other threads
* The application can truly use all of your CPU cores

**One-to-one Cons**
* OS-specific code is needed
* You run into the kernel's limit on the number of threads

This is the model used by Linux, Mac, Windows and AIX



## 4.3.3 Many-to-many

A pool of user-threads is served by a (smaller) pool of kernel threads.  Each
time a user-level thread makes a syscall it can be handled by a different
kernel thread.

![Many to many](many-to-many.png)

All of the benefits of one-to-one threading without the OS'es limitation on
number of threads.


## [Hyperthreading](https://en.wikipedia.org/wiki/Hyper-threading)

> Hyper-threading is Intel's proprietary simultaneous multithreading (SMT)
> implementation used to improve parallelization of computations (doing
> multiple tasks at once) performed on x86 microprocessors.

> For each processor core that is physically present, the operating system
> addresses two virtual (logical) cores and shares the workload between them
> when possible. The main function of hyper-threading is to increase the number
> of independent instructions in the pipeline; it takes advantage of
> superscalar architecture, in which multiple instructions operate on separate
> data in parallel. With HTT, one physical core appears as two processors to
> the operating system, allowing concurrent scheduling of two processes per
> core. In addition, two or more processes can use the same resources: If
> resources for one process are not available, then another process can
> continue if its resources are available.


----------------------------------------------------------------------------
# 4.5 [Cool Pool Party](https://www.youtube.com/watch?v=O6CNdlJp9c8)

* Even though threads are cheaper to make than processes, we're greedy people
  and want more performance.

* Or, we want to pretend that we have unlimited threads despite having a finite
  number of kernel threads.

A Thread Pool lets us maintain these illusions.


### This sounds too good to be true. How does it work?

0.  Spawn a number of generic threads at program startup time (when we won't
    notice how slow this is)
1.  Maintain a queue of tasks which our generic threads can execute
2.  There isn't a 1:1 correspondence between our tasks and the number of
    threads in the pool, so we can keep making up tasks and pretending that
    they each get their own thread
3.  The runtime environment can maintain the optimal number of threads for us,
    so we don't even have to worry about that detail.





----------------------------------------------------------------------------
# 4.6 What could possibly go worng with threading?

Here are some questions to think over:

* What should happen when a thread calls fork() or exec()?

* What should happen when a signal is received? Which thread has to drop what
  it's doing to handle it?  Assume that I installed the handler *before*
  spawning threads.

* What if you need to cancel a thread before it gets to a nice stopping point?

Here there are two possibilities for stopping a thread:


#### Asynchronous cancellation
One thread immediately and forcibly terminates the target thread

#### Deferred cancellation
The target thread periodically checks (possibly by looking at a global
variable) whether it should terminate.  Gives the target thread a chance to
clean up before it quits


## Storing data
What if a thread has data that is neither global nor local? Data on the heap
can be shared between all threads (this is, after all, one of the motivations
of threading as an alternative to forking processes).
  
But local variables only last as long as the current function call, and are
only visible to the current call stack; and a multi-threaded process as many
separate call stacks.
  
Thread Local Storage is the middle ground.



#### Thread Local Storage (TLS)
Memory which isn't in a threads call-stack, and which persists across function
calls, but isn't accessible to other threads within the same process.

TLS also has the advantage of cache-locality: if a thread is running
exclusively on the same CPU core, its TLS will likely stay on that CPU's main
cache.


Lecture 18: Module3\Oct_07\README.md
================================================================

CS3100 - Module 3 - Lecture 18 - Mon Oct 07

# Announcements

# Call on 2 designated questioners


Chapter 5: Process Synchronization

## Topics
* 5.1  What is a race condition?
* 5.2  What is the "critical-section" problem?





--------------------------------------------------------------------------------
# 5.1. What is a race condition?

#### Race Condition
A situation where several processes read & write same data concurrently, and
the outcome of the execution depends on the order the processes accessed the
common data

[Race Condition demos](RaceCondition/)


These demos work out the way they do because there is a race condition between
reading and incrementing the counter.

Only one of the producer or consumer should be allowed to perform a pair of
read/write operations on this variable.

This region of code is a "critical-section".


--------------------------------------------------------------------------------
## 5.2. What is the "critical-section" problem?

#### Critical-Section
A segment of code in which shared resources are accessed


    do {
        /* ENTRY SECTION */

        critical section
        ...

        /* EXIT SECTION */

        remainder section
        ...

    } while (true);


A solution to the critical-section problem must satisfy the following three
requirements:

1. **Mutual exclusion:** If one process is executing its critical section, no other
   processes may be executing in their critical section

2. **Progress:** If no process is in its critical section, then only those
   processes not in their remainder sections are considered for the choice of
   next entrant to the critical section

3. **Bounded waiting:** There is a limit to the number of times a process is
   denied entry to its critical section in favor of other processesounded
   waiting: 


Operating systems themselves may have multiple threads of execution, and take
one of two approaches to this problem when it comes to their own
critical-sections:

#### Preemptive kernel
Allows a process to be preempted (interrupted or prevented) in kernel mode (e.g. system calls may be interrupted)

#### Non-preemptive kernel
A kernel-mode process is not allowed to be preempted; it continues to run until it exits kernel-mode, performs a blocking operation, or yields the CPU

Preemptive pros: more responsive b/c less risk that a kernel task runs too long

Non-preemptive pros: free from race conditions b/c only one kernel process is active at a time


#### Atomic
Said of any operation which happens in one logical step

In general, if an operation takes more than one machine-code instruction to
complete it is not atomic. If such an operation takes place outside of a
critical-section it is possible that another process can observe the
partially-completed operation, resulting in a race condition.




Lecture 19: Module3\Oct_09\README.md
================================================================

CS3100 - Module 3 - Lecture 19 - Wed Oct 09

# Announcements

Hey you! Yes you there!  Stressed out about homework?  No, Not your English
paper! I can't help you there.

I mean your programming assignment! What if I told you that you can learn to go
from Programming Zero to Programming Hero?  All it would take is an hour of
your day?  An hour for a lifetime of happiness, wealth, and success, sounds
like a steal.

What is the catch?  You!  You are a Catch and deep inside lies the programming
lion among men!  Come and learn how to be a better programmer and become better
at almost everything else!

Tonight @ 6pm in room ESLC 053 

# Call on 2 designated questioners


## Topics
* Mud card pop quiz
* 5.5  What is a mutex lock?
* 5.6  What is a Semaphore?



--------------------------------------------------------------------------------
# Mud card pop quiz

* What is a *race condition*?

* What is a *critical-section*?

* What does *atomic* mean?

* Do multi-threaded programs running on a 1-CPU system need mutual exclusion?

* Do multi-threaded programs running on a multi-CPU system need mutual exclusion?

* What are the 3 requirements that any solution to the *critical-section* must
  satisfy?

* What's better: *Preemptive kernels* or *Non-preemptive kernels*?  Why?



--------------------------------------------------------------------------------
# 5.5 What is a mutex lock?

#### Mutex
Short for MUTual EXclusion

Protects a critical section by allowing only one process to enter a region of
code at a time.

A mutex can be thought of as an object containing a bool variable `available`,
and supporting two basic operations:

```
class Mutex {

    bool available;

    void acquire() {
        while (!available)
            ; /* busy wait */
        available = false;
    }

    void release() {
        available = true;
    }
};
```


The critical section is protected like so:
```
do {
    /* ENTRY SECTION */
    
    mutex.acquire();
    critical section
    ...

    /* EXIT SECTION */
    mutex.release();

    remainder section
    ...

} while (true);
```




## Mutex Spinlocks

Recall the implementation of a mutex from above.

The problem with my mutex is that `/* busy wait */` in the middle - that's a
waste of CPU for any other process that is waiting to enter the critical
section.

This type of CPU-inefficient mutex is called a "spinlock" because the CPU just
sits and spins while you wait.



#### Spinlock
A mutex which causes the CPU to "spin" until the lock may be acquired

There is, however, one nice thing about a spinlock: no context-switch is needed.

How can a context-switch more of a waste of the CPU busy loop?  That busy while
loop can be as few as one or two CPU instructions.  It may take hundreds or
even thousands of instructions to achieve a context-switch.  Think of the
overhead of

1. Preparing arguments for a function call
2. Preparing a new stack frame in the called function
3. Setting up local variables in the new stack frame
4. Copying the process state into a PCB structure in RAM
5. Invoking the OS scheduler (another function call), and all of the work it
   does to decide which queues all processes belong in

Spinlocks are actually a more effective use of the CPU in situations where a
process is not expected to wait very long for a lock.

*Q:* How will I know when it's okay to use a spinlock?

*A:* It's a balance between the time wasted by the CPU being in a busy loop vs.
the overhead of making a system call.


## Potential race condition in a spinlock

Disassembly of a simplified spinlock's `acquire()` method reveals a race
condition between testing the availability of the mutex and marking it
unavailable.

```C
int available = 1;

void acquire() {

    /* This test and loop happens in two CPU instructions */
    while (!available)
                                cmpl   $0x0,-0x4(%rbp)
                                je     b <acquire+0xb>
        ; /* busy wait */

    /* this assignment takes two CPU instructions */
    available = 0;
                                movl   $0x0,-0x4(%rbp)
                                mov    $0x0,%eax
}
```

The issue arises because testing `!available` and making an assignment to
`available` are not *atomic* operations.


--------------------------------------------------------------------------------
# 5.6. What is a Semaphore?

![Navy Semaphore Dude](semaphore.jpg)

IRL a semaphore is a system of long-distance communication using flags.  The
way the signalman holds the flags indicates a letter or digit.  All of the
letters of the alphabet and all ten digits may be signaled by a single person.

A mutex which uses a `bool` to encode two states, `available` and `!available`.

A semaphore is like a mutex which uses an `int` and can encode many more
states.  They are useful, for example, when a resource may be accessed by more
than one process at a time up to some limit.

#### Binary semaphore
Can range between 0 and 1; this is the same thing as a mutex

#### Counting semaphore
Its states can range over an unrestricted domain

When a Semaphore `S` is created, it is initialized with a value greater than
zero.  Semaphores support two basic operations, `wait()` and `signal()`:

```C

init(S, n) {
    S = n;
}

...

init(Semaphore, 8); /* semaphore is initialized to 8 */

wait(S) {
    while (S <= 0) /* so long as no resources are available */
        ;          /* busy wait */

    S--;  /* consume a resource */
}


signal(S) {
    S++; /* Put my resource back */
}
```

It is important that inspecting, incrementing and decrementing the Semaphore
value is done atomically!



POSIX defines an API for operating-system level semaphores.

[Semaphore demo in C++](semaphore/)


## 5.6.1: Semaphore usage

Consider a situation where 8 processes may access a resource simultaneously.
A semaphore is initialized to the value of 8.  16 threads are spawned to work
on this resource. As each thread reaches its critical section, they each use
the semaphore's wait() operation:

```C
do {

    safe code
    ...

    /* ENTER CRITICAL SECTION */
    semaphore.wait();

    critical section code
    ...

    /* EXIT CRITICAL SECTION */
    semaphore.signal();

    safe code
    ...

} while (true);
```

There should be only 8 threads within the critical section. As soon as one
leaves the critical section it increments the semaphore's counter, immediately
allowing another waiting thread to enter its critical section. In this system
there are at most 8 threads using the critical section at once.





Lecture 20: Module3\Oct_11\README.md
================================================================

CS3100 - Module 3 - Lecture 20 - Fri Oct 11

# Announcements

## Mid-Term Exam is next week

The exam is open in the testing center Tuesday Oct 15th through Thursday Oct 17th.

Monday's lecture will be review of the material on the exam.

The lecture is canceled next Wednesday, Oct 16th, to give you plenty of time to study and take the exam.



# Topics:
* 5.7.3 The Dining-Philosophers Problem
* 5.6.3 Deadlocks and Starvation


--------------------------------------------------------------------------------
# 5.7.3 The Dining-Philosophers Problem

Philosophers (as perceived by Computer Scientists, anyway) spend their lives
alternatively thinking their big thoughts and eating.

![The Dining Philosophers](dining_philosophers.png)

Philosophers don't interact with their neighbors directly - small talk is too
far beneath the lofty heights of their metaphysical musings.

Occasionally, a Philosopher becomes hungry and will try to pick up the two
chopsticks adjacent to them (one at a time) to eat from a shared bowl of rice
(Philosophers are big on the philosophy that "sharing is caring").

They need both chopsticks to eat, and release both (one at a time) when they
are finished.

Ideally no Philosophers starve at this table.  Philosophers are smart people,
so this shouldn't be a problem, right?

In the case of 5 philosophers, there are six unites of shared data:

* One Bowl of rice (data set)
* Semaphore `chopstick[5]`, each element initialized to 1


Main loop of Philosopher *i*
----------------------------

```Java
while (true) {

    chopstick[i].wait(); // Grab the LEFT chopstick 
    chopstick[ (i + 1) % 5 ].wait(); // Grab the RIGHT chopstick 

    eatRice();

    chopstick[i].signal(); // Return the LEFT chopstick 
    chopstick[ (i + 1) % 5 ].signal();  // Return the RIGHT chopstick 

    thinkLoftyThoughts();

}
```


* Is there anything wrong with this algorithm?

* Can you do better?


--------------------------------------------------------------------------------
# 5.6.3 Deadlocks and Starvation

Like all things on a computer, there are a number of ways this can fall apart.

#### Deadlock
A situation where two or more processes are mutually waiting upon each other,
such that no progress is ever made.

The deadlocked processes are waiting indefinitely for an event that can be
caused by only one of the waiting processes; the cycle of waiting cannot be
broken.

#### Starvation
A situation where a process waits forever within the semaphore, never having a
chance to acquire its resource.  No progress is ever made.

## 5.7.2 The Readers-Writers Problem

Throughout our discussions of threads or processes accessing shared resources
we have broadly partitioned them into two classes, *producers* and *consumers*,
where both participants may modify the shared resource.

Another way to participate in a concurrent or parallel system is as
*readers* and *writers*.

#### Readers
May only read the data set; they do not perform any updates

#### Writers
Can both read and write the shared data set

The problem
-----------
Because readers don't modify the shared data, it makes no difference when many
of them to share simultaneous access.  However, if there is more than *one*
writer at a time, trouble will ensue.  Trouble may also arise if readers
attempt to access the shared data while the writer is in the midst of its work.

Several variations of how readers and writers are considered.  All involve some
concept of priorities.  The idea is to ensure that only one single writer can
access the shared data at a time.


Shared data
-----------
Semaphore `rw_mutex` initialized to `1`
Semaphore `mutex` initialized to `1`
`int read_count = 0`


Structure of the writer process
-------------------------------
```C
do {
    wait(rw_mutex);
    ...
    /* writing is performed */
    ...
    signal(rw_mutex);
} while (true);
```


Structure of reader processes
-----------------------------

```C
do {
    wait(mutex);
    read_count++;
    if (read_count == 1) {
        wait(rw_mutex);
    }
    signal(mutex);

    ...
    /* reading is performed */
    ...

    wait(mutex);
    read count--;
    if (read_count == 0) {
        signal(rw_mutex);
    }
    signal(mutex);
} while (true);
```



Readers-Writers Problem Variations
----------------------------------

* First variation - no reader is kept waiting unless writer has permission to use shared object
* Second variation - once the writer is ready, it performs the write ASAP

Both variations may have starvation, leading to even more variations

In practice this problem is solved by the kernel providing reader-writer locks



Lecture 21: Module3\Oct_14\README.md
================================================================

CS3100 - Module 3 - Lecture 21 - Mon Oct 14

# Announcements

## `concatenate.py` script has been fixed

In your lecture notes repository is a Python script which concatenates all
`README.md` files from all lecture notes into one file called `all_notes.md`.
This will be helpful as you study for this week's midterm exam.

```
$ git clone git@gitlab.cs.usu.edu:erik.falor/fa19-cs3100-lecturenotes.git
$ cd fa19-cs3100-lecturenotes
$ python concatenate.py
Concatenating lecture #1 Module0/Aug_26/README.md
Concatenating lecture #2 Module0/Aug_28/README.md
Concatenating lecture #3 Module0/Aug_30/README.md
Concatenating lecture #4 Module0/Sep_04/README.md
Concatenating lecture #5 Module1/Sep_06/README.md
Concatenating lecture #6 Module1/Sep_09/README.md
Concatenating lecture #7 Module1/Sep_11/README.md
Concatenating lecture #8 Module1/Sep_13/README.md
Concatenating lecture #9 Module1/Sep_16/README.md
Concatenating lecture #10 Module2/Sep_18/README.md
Concatenating lecture #11 Module2/Sep_20/README.md
Concatenating lecture #12 Module2/Sep_23/README.md
Concatenating lecture #13 Module2/Sep_25/README.md
Concatenating lecture #14 Module2/Sep_27/README.md
Concatenating lecture #15 Module2/Sep_30/README.md
Concatenating lecture #16 Module3/Oct_02/README.md
Concatenating lecture #17 Module2/Oct_02/README.md
Concatenating lecture #18 Module3/Oct_04/README.md
Concatenating lecture #19 Module3/Oct_07/README.md
Concatenating lecture #20 Module3/Oct_09/README.md
Concatenating lecture #21 Module3/Oct_11/README.md
Concatenating lecture #22 Module3/Oct_14/README.md

Concatenated notes saved to all_notes.md
This file is marked read-only because running the concatenate script again will
delete it. Keep your personal notes elsewhere, or rename the file.
```

## FSLC Meeting

* Wednesday, 10/16
* 6pm @ ESLC 053



# Call on 2 designated questioners


# Midterm Exam Review

* 35 questions 
* 143 points

How to prepare for my exams:

1.  Attend this review lecture
2.  Mastery Quizzes on Canvas


## Chapter 1
* Sections 1 through 8
* Section 11
* User view and Resource Allocator view of an OS
    * What are the goals of the system under each perspective?
* Storage structure
* Single and multi-processor systems
* CPU Dual-mode operation
    * Privileged instructions
    * User mode instructions
* Parallelism vs. Concurrency
* Asymmetric multiprocessing vs. Symmetric multiprocessing (SMP)



## Chapter 2
* Sections 1 through 7
* OS services
* System calls
    * How do arguments get from your code into the kernel?
* Design goals of an OS
* Mechanism vs Policy
    * What the rules are
    * How the rules are implemented/enforced
* OS architecture: simple, layered, monolithic, microkernel (not modules or hybrid systems, or iOS/Android)
    * Pros & Cons of monolithic architecture
    * Pros & Cons of micro-kernel architecture


## Chapter 3
* Sections 1 through 4
* Process concept and details
    * How does a process differ from a program?
    * Memory sections of a process, text, data, stack & heap
* Context switch
* Process state
    * Process Control Block - what's recorded here?
    * Program counter
* The Operating System's process scheduler
    * Job queue
    * What are the 5 states a process can be in?
* IPC
    * Producer/Consumer
    * Shared memory (SHM)
    * Message passing
    * Mailboxes
    * Pros & cons of SHM vs. Message Passing
* Effect of buffering on synchronization 
    * Synchronous vs. Asynchronous communication
    * Blocking vs. non-blocking behavior
    * Zero capacity, bounded & Unbounded capacity buffers


## Chapter 4
* Sections 1 through 3
* Section 6; only 4.6.2, 4.6.3
* Benefits of threading
* Challenges of multicore programming
    * Amdahl's Law
    * Cancelling threads (asynchronous vs. deferred)
* Threading models
    * One-to-One
    * Many-to-One
    * Many-to-Many
* Thread pools


## Chapter 5
* Sections 1, 2, 4, 5, 6, and 7
* Race condition, instruction interleaving
* Critical sections
    * 3 requirements of a solution to the critical section problem
* Synchronization hardware
* Mutexes, semaphores
    * Spinlocks vs. causing a context switch
* Classic problems of synchronization
    * Dining Philosophers


Lecture 22: Module4\Oct_21\README.md
================================================================

CS3100 - Module 3 - Lecture 22 - Mon Oct 21

# Announcements

## SDL/USU Technical Lecture Series

4:30 pm on Tuesday, Oct. 22 at ENGR 201.

Dr. Quinn Young, Systems Engineering Group lead at SDL, will discuss how
systems engineering provides technical oversight and management of modern
systems and their complexities.

More information about this exciting event is available on our
[website](https://usu.us19.list-manage.com/track/click?u=416137052a6df3a9b4e2659c7&id=c53d848814&e=96b2445203).

See you there!  




# Topics:
* Midterm Exam recap
* Assignment #3 is due Wednesday


--------------------------------------------------------------------------------
# Midterm Exam recap

* Average Score = 70%
* Average Time = 18:38


* Q:    A single processor system can only do one thing at a time. (22% answered correctly)
* A:    True


* Q:    Which of the following instructions should be privileged? (select all that apply) (21% answered correctly)
* A:    1.  Access I/O device.
        2.  Set value of the CPU timer
        3. Turn off interrupts

Other distractors:
1.  Read a value from memory
2.  Write a value to memory
3.  Multiply two values


* Q:    Which of the following are considered advantages of a microkernel design. (select all that apply) (33% answered correctly)
* A:    1.  Don't need to modify the kernel to extend the OS
        2.  Easy to port to new hardware

Other distractors:
1.  Faster context switching
2.  Easier to install on a virtual machine


--------------------------------------------------------------------------------
# Assignment #3 is due Wednesday

* Be sure to closely read the assignment description.  Many of your questions
  have answers in there that you may have missed on your first reading.
* Check Piazza for questions/answers.  This is the preferred venue for
  answering questions because it multiplies our effectiveness.  Plus, I'll
  notice your participation on-line and can reward you with participation
  points at the end of the semester.



Lecture 23: Module4\Oct_23\README.md
================================================================

CS3100 - Module 4 - Lecture 23 - Wed Oct 23

# Announcements

## FSLC CyberHacker Movie Night

Tonight we are watching a classic movie about hacking that literally sparked
the creation of cyber-security in the US.  That's right we'll be watching the
movie *Wargames*. So come on down to ESLC 053 at 6pm to view this classic.

FSLC now has a [Discord!](https://discord.gg/RHppcek), and you're invited!


## Lucid Programming Competition

Join us for the 7th annual Lucid Programming Competition. Compete against teams
from universities across Utah for a chance to win an Amazon gift card worth up
to $300. It's always a good time—you won't want to miss it!

Register with your team or as an individual. Complete this form to secure your
spot in the competition: https://www.golucid.co/programming-competition

* Saturday, November 2, 2019
* 8:00 a.m. - 2:00 p.m.
* ENGR 108



# Call on 2 designated questioners


# Topics:
* 6.1.1 CPU-I/O Burst Cycle
* 6.1.2 CPU Scheduler
* 6.1.3 Preemptive Scheduling

--------------------------------------------------------------------------------

# 6.1.1 CPU-I/O Burst Cycle

Process execution consists of a cycle of CPU execution and I/O wait.

   I/O Wait -> CPU -> I/O Wait -> CPU -> I/O Wait -> CPU -> I/O Wait -> and so on.

![The CPU-I/O burst cycle](burst_cycle.png "The CPU-I/O burst cycle")

Eventually, the final CPU burst ends with a system request to terminate execution.

## Key insights:

* An I/O-bound program typically has many short CPU bursts
* A CPU-bound program might have a few long CPU bursts
* Overall, bursts tend to be short

![CPU burst durations/frequency](cpu_burst_duration.png "CPU burst durations/frequency")

This distribution can be important in the selection of an appropriate
CPU-scheduling algorithm.


# 6.1.2 CPU Scheduler

a.k.a. short-term scheduler

#### CPU scheduler: selects a process from the processes in memory that are ready to execute

The list of processes on a system is conceptually stored in collection of
queues based on the state of the program (i.e. ready queue, I/O queue, etc.)

Note:
=====
The ready queue is not necessarily a first-in, first-out (FIFO) queue.  We'll
treat it like it is for convenience sake, but it could be implemented as a
different data structure



# 6.1.3 Preemptive Scheduling

There are 4 circumstances under which CPU-scheduling decisions may take place:

## The 4 circumstances

1. A process switches from the running state to the waiting state (for example,
   as the result of an I/O request or an invocation of wait() for the
   termination of a child process)
   
   "I'm at a good stopping point"

2. A process switches from the running state to the ready state (for example,
   when an interrupt occurs)

   "Timmy, let the other children have a turn now"

3. A process switches from the waiting state to the ready state (for example,
   at completion of I/O)

   "Your table is ready"

4. A process terminates of its own accord

   `return 0; // at the end of main`


### In circumstances 1 & 4, there is no choice for the OS scheduler to make

The process has made the scheduling decision for itself.

This situation is called "non-preemptive" or "cooperative" scheduling.  Under
this scheme, once the CPU has been allocated to a process the process keeps the
CPU until it releases the CPU either by terminating or by switching to the
waiting state.  Nothing can interrupt the process.

This scheme depends upon processes to give up their turns on the CPU

#### non-preemptive pro: Works on simple hardware w/o dedicated timers
#### non-preemptive con: Bugs in programs (e.g. an infinite loop or some other bug is encountered) causes the entire system to hang


### Circumstances 2 & 3, therefore, are considered "preemptive"

The preemptive method is used by all modern mainstream server & desktop OSes.

Preemption also affects the design of the operating-system kernel.  During the
processing of a system call, the kernel may be busy with an activity on behalf
of a process.  Such activities may involve changing important kernel data (for
instance, I/O queues).  What happens if the process is preempted in the middle
of these changes and the kernel (or the device driver) needs to read or modify
the same structure?

Chaos ensues.

#### preemptive pro: More robust against programs which don't share
#### preemptive con: Requires more a sophisticated and complicated OS
#### preemptive con: Can result in race conditions when data are shared among several processes


# 6.1.4 Dispatcher

#### Dispatcher: the module that gives control of the CPU to the process selected by the short-term scheduler

This function involves the following:

* Switching context
* Switching to user mode
* Jumping to the proper location in the user program to restart that program

#### Dispatcher latency: The time it takes for the dispatcher to stop one process and start another running 

The dispatcher should be as fast as possible, since it is invoked during every
process switch.



Lecture 24: Module4\Oct_25\README.md
================================================================

CS3100 - Module 4 - Lecture 24 - Fri Oct 25

# Announcements

# Call on 2 designated questioners


# Topics:
* Mudcard review
* Assignment #4 preview
* 6.2 Scheduling Criteria
* 6.3 Scheduling Algorithms
* 6.3.1 First-Come, First-Served Scheduling
* 6.3.2 Shortest-Job-First Scheduling


--------------------------------------------------------------------------------
# Mudcard review


# [Assignment #4 preview](https://usu.instructure.com/courses/547959/assignments/2699285)



# 6.2 Scheduling Criteria

There are many possible CPU-scheduling algorithms to choose from. Which one you
use affects the behavior of the system by favoring certain types of processes
over others.

Criteria which may be taken into consideration by the scheduler:
================================================================

* CPU utilization. In general, we want to keep the CPU as busy as possible.


* Throughput. If the CPU is busy executing processes, then work is being done.

#### Throughput: the number of processes that are completed per time unit


* Turnaround time. How long does it take to execute that process from start to
  finish?

#### Turnaround time: The interval from the time of submission of a process to the time of completion 

Turnaround time = Spawn time + CPU execution + I/O Wait + Waiting in ready queue


* Waiting time. The CPU-scheduling algorithm can't help how much time a process
  spends waiting for I/O, or how much computation a process must make. It can
  try to minimize the amount of time the process spends in the ready queue.

* Response time. Time from the submission of a request until the first response
  is produced.

#### Response time: the time it takes a process to start responding, not the time it takes to output the response.

In an interactive system, turnaround time may not be the best criterion. Often,
a process can produce some output fairly early and can continue computing new
results while previous results are being output to the user.

The turnaround time is generally limited by the speed of the output device.


### Takeaways:

* It is desirable to maximize CPU utilization and throughput and to minimize
  turnaround time, waiting time, and response time.

* Investigators have suggested that, for interactive systems (such as desktop
  systems), it is more important to minimize the variance in the response time
  than to minimize the average response time. A system with reasonable and
  predictable response time may be considered more desirable than a system that
  is faster on the average but is highly variable.



# 6.3.1 First-Come, First-Served Scheduling

The Good:
---------
The simplest scheduling algorithm of them all (just a FIFO queue)


The badly ugly:
---------------
Sensitive to the order in which processes arrive

This is a problem when the slowest process arrives first.

Given these processes, how will this algorithm schedule them?

|Process|Burst Time|
|:-----:|:--------:|
|   P1  |    24    |
|   P2  |    3     |
|   P3  |    3     |

![First-Come, First-Served waiting time](fcfs_convoy.png "The old Convoy Effect")

<details>
<summary>What's the waiting time for each process?</summary>


|Process|Waiting Time|
|:-----:|:----------:|
|   P1  |    0       |
|   P2  |    24      |
|   P3  |    27      |

</details>

<details>
<summary>What's the *average* waiting time for all processes?</summary>
17.0

</details>

<details>
<summary>What's the *average* waiting time for all processes if the arrived in the order P2, P3, P1?</summary>
3.0

</details>


#### Convoy Effect: delay felt by all the other processes which wait for the one big process to get off the CPU



The [convoy](https://www.youtube.com/watch?v=Sd5ZLJWQmss) effect results in
lower CPU and device utilization than might be possible if the shorter
processes were allowed to go first.

This particular problem is most associated with FCFS scheduling



# 6.3.2 Shortest-Job-First Scheduling

Take advantage of the fact that we know all processes exhibit a CPU-I/O Burst Cycle:

CPU -> I/O Wait -> CPU -> I/O Wait -> CPU -> I/O Wait -> and so on.

The SJF algorithm associates with each process the length of the next CPU burst
(don't worry about where this length comes from just yet...)

The SJF scheduling algorithm is provably optimal, in that it gives the minimum
average waiting time for a given set of processes.

Given these processes, how will this algorithm schedule them?

|Process|Burst Time|
|:-----:|:--------:|
|   P1  |    6     |
|   P2  |    8     |
|   P3  |    7     |
|   P4  |    3     |


![Shortest-Job-First example](sjf_example.png "SJF scheduling chart")

<details>
<summary>What order will the SJF scheduler place these processes?</summary>
P4, P1, P3, P2

</details>


<details>
<summary>What's the waiting time for each process?</summary>

|Process|Waiting Time|
|:-----:|:----------:|
|   P1  |    3       |
|   P2  |    16      |
|   P3  |    9       |
|   P4  |    0       |


</details>


<details>
<summary>What's the *average* waiting time for all processes?</summary>
7.0

</details>


<details>
<summary>What would the *average* waiting time for these processes be under FCFS?</summary>
10.25

</details>


The catch:
----------
The real difficulty is knowing the length of the next CPU request.

The short-term scheduler simply doesn't have enough information available to
know how long the next CPU burst will be. Our next best approach to predict
this is to approximate or estimate this duration.

The next CPU burst is generally predicted as an exponential average of
the measured lengths of previous CPU bursts.

![Burst time exponential moving average](burst_prediction.png "Predicting the next CPU burst")




Lecture 25: Module4\Oct_28\README.md
================================================================

CS3100 - Module 4 - Lecture 25 - Mon Oct 28

# Announcements

# Call on 2 designated questioners


# Topics:
* 6.3.3 Priority Scheduling
* 6.3.4 Round-Robin Scheduling
* 6.3.5 Multilevel Queue Scheduling
* 6.5 Multiple-Processor Scheduling
* 6.5.2 Processor affinity
* 6.5.3 Load Balancing
* Assignment 4 Questions




# 6.3.3 Priority Scheduling

#### Priority Scheduling: Associate a priority rank with each process, selecting the highest priority process to execute next

Generally, smaller priority values are considered *higher* priority than larger
ones.

It's better to be in 1st place than 10th place. This mnemonic works until your
system (*cough* Linux *cough*) starts assigning *negative* priority numbers...
then it's better to be in -10th place than 1st place.

The priorities are not necessarily related to the expected burst times; they
may be set by the user according to their own whim.  Scheduling priority on
Linux systems can be set and changed with the `nice(1)` and `renice(1)`
commands.  On Windows you can adjust the priority of a running process with the
Process Explorer tool.

Suppose these processes arrive at the scheduler having been assigned these
priorities and with expected burst times.  They are scheduled thus:

|Process|Burst Time|Priority|
|:-----:|:--------:|:------:|
|   P1  |   10     |    3   |
|   P2  |    1     |    1   |
|   P3  |    2     |    4   |
|   P4  |    1     |    5   |
|   P5  |    5     |    2   |

![Priority scheduling chart](priority.png "Priority scheduling chart")


<details>
<summary>What's the waiting time for each process?</summary>

|Process|Waiting Time|
|:-----:|:----------:|
|   P1  |    6       |
|   P2  |    0       |
|   P3  |   16       |
|   P4  |   18       |
|   P5  |    1       |

The average wait time is 8.2.  Remember, the burst time is *not* taken into
consideration in this decision: only the priority ranking counts!

</details>


Shortest-Job-First scheduling is a *special-case* of priority scheduling, where
the priority number is the inverse of the next predicted burst time.  The
shorter the next burst is expected to be, the higher the priority.


#### Starvation: A process which remains in the waiting queue forever becomes starved

Starvation can happen in Priority Scheduling for processes with really low
priority; they may never get a turn if there's always another process with a
higher priority.

#### Aging: Increasing a processes' priority as it sits on the wait queue

Through aging processes we can guarantee that they will get a turn *eventually*

# 6.3.4 Round-Robin Scheduling

Similar to FCFS, but with preemption so that process switches are guaranteed to
happen eventually.

#### Time Slice: a small unit of time which is the longest "turn" a process can take in the Running state.

a.k.a. "Time Quantum"

If there are `N` processes in the Ready queue, then each process will get `1/N` of
the CPU time, spread out over chunks in the size of the system's time slice.

If a process on the running queue doesn't make a system call (e.g. doesn't do
an I/O operation that might cause it to wait) the system preempts it when its
time slice expires, forcing it to the back of the Ready queue.


Given these processes burst times and a time slice of 4:

|Process|Burst Time|
|:-----:|:--------:|
|   P1  |    24    |
|   P2  |    3     |
|   P3  |    3     |

We get this many context switches:

![RR forced context switches](rr_context_switches.png "Round Robin forced context switches")


#### RR drawback: Context switches are forced even when N = 1 and there is no need to share.

RR works well when the overhead of making a context switch is low.

In general, you want to scale your time slices such that they are significantly
longer than the time it takes to do a context switch; otherwise, you spend as
much time performing context switches as you do useful work.

![Round Robin time slices vs. # of context switches](rr_time_slice_sizes.png "Round Robin time slices vs. # of context switches")

Consider "Response Time" vs. "Turnaround Time"

#### Turnaround time: The interval from the time of submission of a process to the time of completion 
#### Response time: the time it takes a process to start responding, not the time it takes to output the response.

Generally, RR has higher *turnaround* time than SJF, but a lower *response* time


# 6.3.5 Multilevel Queue Scheduling

Which is better, RR or FCFS? Why choose when you can have both!

MLQ divides processes into two classes:

#### Foreground processes: interactive processes that people might see

Examples:
Your terminal, browser, word processor

#### Background processes: batch processes which humans won't notice 
Examples:
System daemons, scheduled backups, antivirus, system updates



### The Strategy
The difference between these processes is that they have different
response-time requirements.

We'll use a scheduling algorithm for those processes which need to feel more
responsive, at the expense of more context switches.

Processes which need to get a lot of work done in one stretch will benefit from
longer time slices and fewer context switches, and spending just a bit more
time waiting on the ready queue won't cramp their style.

We can also have more than just two queues, assigning priorities to processes
based upon who is using them, and what type of work they do (give the CEO the
highest priority so they don't throw a tantrum).

### Starvation warning!
There is a possibility of starvation with MLQ: we could spend all of our time
serving the foreground queue and leave the background queue on the back burner.

We might do have time-slices among the queues, so that we guarantee that at
least 10% of the CPU is devoted to background processes so that they aren't
neglected forever.



# 6.5 Multiple-Processor Scheduling

## Asymmetric multiprocessing
* Only one processor (the master) accesses the system data structures,
  alleviating the need for data sharing
* The other processes handle all user code
* Simple to implement

## Symmetric multiprocessing (SMP)
Each processor is self-scheduling. This means that either:
* all processes are in a common ready queue
* each processor has its own private queue of ready processes

Presently, this is the most common type of multiprocessing in mainstream OSes.


# 6.5.2 Processor affinity
The property that a process has an affinity for the processor on which it is currently running.

Why?

0. A process has accessed a lot of RAM while it was on processor 1. All of that
   data is cached in CPU 1's private, fast cache.
1. Moving this process over to CPU 2 means that we either copy the cache, or
   throw all of that data away, only to slowly read it back in from RAM

Keeping a process on the same CPU maximizes our return on investing in the
overhead.

There are two approaches to implementing processor affinity:
* soft affinity - we'll do our best to keep a process on the same CPU, but no
  guarantees.
* hard affinity - lock a process to a specific processor (or set of processors)

For example, Linux implements soft affinity, but has support for hard affinity.
See the man page for the `taskset(1)` command.


# 6.5.3 Load Balancing
Under SMP it is important to keep the work spread evenly across all CPUs so
that we can maximize utilization.

#### Load Balancing - attempt to keep the workload evenly distributed

Explicit load balancing is mostly needed on systems where each processor has
its own private queue of tasks; when a system uses a common ready queue load
balancing naturally takes care of itself.

It's easy to imagine why: when a processor becomes idle, it's immediately
assigned the next available task.



# [Assignment 4 Questions](https://usu.instructure.com/courses/547959/assignments/2699285)

What questions do you have about the upcoming assignment?


Lecture 26: Module4\Oct_30\README.md
================================================================

CS3100 - Module 4 - Lecture 26 - Wed Oct 30



# Chapter 7: Deadlock

# Topics
* 7.1 System Model
* 7.2.1 Deadlock Necessary Conditions
* 7.2.2 Resource Allocation Graphs
* 7.3 Methods for Handling Deadlocks
* 7.4 Deadlock Prevention
* 7.5 Deadlock Avoidance
* 7.5.1 Safe State
* 7.5.3 The Banker's Algorithm



--------------------------------------------------------------------------------
# What is "Deadlock"?

[Deadlock Demo in C++](deadlock/)


# 7.1 System Model

The system consists of N processes which are desired by M resources.

Of the N processes, each one may need a different subset of the M resources to
fulfill its task.


#### Resource Instances: Number of requests a particular resource my serve at one time

In this system, a resource may be used by a finite number of processes at a
time. Maybe the resource itself supports a limited amount of concurrency or
parallelism; perhaps we have 8 CPU cores or 3 printers, and it really doesn't
matter *which* device serves the request. The point is that the resource is
limited in some way.

Because each resource may be used by only so many processes at a time, we need
to protect their access with locks (or semaphores).


Each process utilizes a resource as follows:

0. **Request** 
   A process requests a resource, or waits until it becomes available

1. **Use** 
   The process uses the resource, making some progress with it

2. **Release**
   The process concludes its work, making the resource become available for
   another process

## 7.2.1 Deadlock Necessary Conditions

Deadlock can occur if these conditions hold simultaneously:

0. **Mutual Exclusion**
   Only one process at a time can use a resource
   (Either the resource has only one instance, or we're requesting the final
   available instance)

1. **Hold and Wait**
   Process holding one resource is waiting to acquire resource held by another process

2. **No Preemption**
   A resource can be released only be the process holding it after the process completed its task

3. **Circular Wait**
   Set of waiting processes such that .P_n-1. is waiting for resource from `P_n`,
   and `P_n` is waiting for `P_0`

   + "Dining Philosophers" in deadlock


## 7.2.2 Resource Allocation Graphs

We can visualize this system model with a Resource Allocation Graph (RAG), and
through examination identify deadlocked systems.

In a RAG the symbols have these meanings:

* Circles represent **processes**
* Rectangles represent **resources**
    + Dots within the resources represent **instances** of resources
* Arrows running from processes to resources are **requests**
* Arrows running from resources to processes are **holds**


![Resource Allocation Graph](resource_allocation_graph.png)

In this diagram

0. Process `P1` requests an instance of resource `R1`, but that resource is
   held by `P2`
1. `P2` wants requests an instances of resource `R3`, but that resource is held
   by `P3`
2. Both available instances of resource `R2` are held by processes `P1` and `P2`
3. Nobody wants to use `R4` (Fallout 76?)


Does this diagram represent a system in deadlock?

* A RAG without cycles does not have a deadlock.

* A RAG with cycles *may* have a deadlock; it depends upon how the resources
  are allocated.

* When all instances of a resource are *allocated* by processes participating
  in a cycle, then the system is in deadlock.


What about this system?

![Another RAG](rag_with_deadlock.png)


Or this system?

![Yet another RAG](rag_cycle_but_no_deadlock.png)


**Mud card activity**

0.  On your mud cards draw the resource allocation graph illustrating the
    situation in [deadlock/deadlock.cpp](deadlock/deadlock.cpp) when that
    process locks up.

    *   What are the processes?
    *   What are the resources?


1.  Draw another RAG illustrating what that process looks like when it isn't
    deadlocked.


# 7.3 Methods for Handling Deadlocks

0. Prevent or avoid deadlocked states
1. Allow a system to enter deadlock, detect it and recover
2. Kick the can down the road and leave it to applications to solve

"Kicking the can" is the option most OSes take, including Linux, UNIX and Windows


# 7.4 Deadlock Prevention

Provide a set of methods to ensure that at least one of the four necessary
conditions are impossible to occur. Et voila, no deadlock

0. Mutual Exclusion
   Shareable resources are those that can be used simultaneously by an
   arbitrary number of processes. They cannot be involved with deadlock.
   A read-only file is an example of a shareable resource.

   Cons: Unfortunately, most useful resources are not shareable. :(

1. **Hold and Wait**

   OS guarantees that whenever a process requests a resource, it does not hold
   any other resources.

   Cons: Low resource utilization; starvation possible

2. **No Preemption**

   If a process with some resources can't immediately get the rest of its
   needed resources, then it gives *all* of them up and tries again later.

   Cons: Really only practical for resources that are easy to save and restore
   later (such as a CPU).


3. **Circular Wait**

   Impose a total ordering of all resource types, and require that each process
   requests resources in an increasing order of enumeration.

   Cons: Having a total ordering isn't sufficient in itself; applications must
   be written to honor it.


In practice, a Deadlock Prevention scheme results in lower device utilization,
and decreased system throughput


# 7.5 Deadlock Avoidance

The OS gets extra information in advance which allows it to satisfy allocation
requests in an order which precludes deadlock from happening.

#### Deadlock Avoidance: ensure that a system will never enter an unsafe state


## 7.5.1 Safe State

A system is in a safe state when there exists a sequence of all processes such
that each process can immediately receive the resources it needs to finish its
work

### Deadlock == Unsafe state

#### Unsafe State != Deadlock

![Safe spaces for processes](safe_space.png)

A system in an unsafe state *may* become deadlocked. Once an unsafe state is
reached, the deadlock prevention measures discussed above cannot preclude
deadlock from happening.

* When a system is in safe state => no deadlocks

*  When a system is in unsafe state => possibility of deadlock

![A system in an unsafe state](rag_unsafe_state.png)



## 7.5.3 The Banker's Algorithm

The name refers the fact that this Algorithm could be used in a financial
system to ensure that a bank never allocates its available cash in such a way
that it can no longer satisfy the needs of its customers.

Each process must a priori claim its maximum resource use. Any one process
cannot declare that it needs more resources than are available.

#### a priori = something you just know ahead of time

When a process requests a resource it may have to wait if fulfilling the
request would leave the system in an unsafe state.

When a process gets all its resources it must return them in a finite amount of
time (progress).

* `n` = # of processes in the system
* `m` = # of types of resources available in the system

This algorithm may require `O(m * n^2)` complexity.



Lecture 27: Module4\Nov_01\README.md
================================================================

CS3100 - Module 4 - Lecture 27 - Fri Nov 01

# Call on 2 designated questioners



# Topics:
* Deadlock mud card activity
* 7.5.3 The Banker's Algorithm
* Chapter 8: Main Memory
    * 8.1 Background
    * 8.1.3 Logical Versus Physical Address Space


----------------------------------------------------------------------------
# Deadlock mud card activity

## Dining Philosophers' Problem

1. Draw a Resource Allocation Graph showing the Dining Philosophers' in
   deadlock.

2. Draw a Resource Allocation Graph showing the Dining Philosophers' when they
   are *not* in deadlock.

## Identify Deadlock

Together with your study buddies, decide whether each of the following images
describe an system in deadlock:


![rag0.png](rag0.png)
<details>
<summary>Is this system in deadlock?</summary>

**No** As soon as `P2` is done `P3` can proceed.

</details>


![rag1.png](rag1.png)
<details>
<summary>Is this system in deadlock?</summary>

**No** As soon as `P3` releases its resources `P1` or `P2` will be able to
proceed.

</details>


![rag2.png](rag2.png)
<details>
<summary>Is this system in deadlock?</summary>

**No** As soon as either `P2` or `P4` release their resources `P1` and `P3` will be able to proceed.

</details>


![rag3.png](rag3.png)
<details>
<summary>Is this system in deadlock?</summary>

**Yes** There are two cycles:

* `P1 -> R1 -> P2 -> R5 -> P4 -> R2 -> P1`
* `P1 -> R1 -> P2 -> R4 -> P3 -> R5 -> P4 -> R2 -> P1`

</details>



# 7.5.3 The Banker's Algorithm

Created by Computer Science legend and real-life wizard Edsger Dijkstra.

* [The original description (in Dutch)](https://www.cs.utexas.edu/users/EWD/ewd01xx/EWD108.PDF)
* [The mathematics behind the Banker's Algorithm](http://www.cs.utexas.edu/users/EWD/ewd06xx/EWD623.PDF)

The name refers the fact that this Algorithm could be used in a financial
system to ensure that a bank never allocates its available cash in such a way
that it can no longer satisfy the needs of its customers.

Each process must claim its maximum resource use before it it can make
requests.  Any one process cannot declare that it needs more resources than are
available.

When a process requests a resource it may have to wait if fulfilling the
request would leave the system in an unsafe state.

When a process gets all its resources it must return them in a finite amount of
time (progress).

This algorithm may require `O(m * n^2)` complexity.

* `n` = # of processes in the system
* `m` = # of types of resources available in the system


--------------------------------------------------------------------------------
# 8.1 Main Memory: Background


#### Physical
Pertaining to the actual, raw hardware

#### Logical
An abstraction; pertains to the perspective we impose upon the system for convenience's sake


## Problem #0: Speed

Most computers which you use are of the von Neumann architecture, which means
they use a single memory bank for both executable code and ordinary data.

At every instruction the CPU is reading from memory, either to

0. fetch instructions to execute
1. fetch/store the data those instructions operate upon

The CPU may only access two types of storage directly:

0. CPU Registers
1. Main Memory (RAM)

Any other storage (disk, DVD-ROM, network) must 1st be copied into one of these
locations in order for the CPU to even use them. This is slow.

Accessing main memory (RAM) is slow compared to accessing CPU registers. This
means that some CPU instructions cannot complete in their ordinary timeframe.


#### Stall
When the CPU cannot execute an instruction because it must wait for data to become available


A CPU stall is the hardware equivalent of sleeping on Disk I/O.

We wish to maximize computational throughput by minimizing stalls.


#### Cache
A small region of fast memory between the CPU and RAM intended to minimize stalling the CPU


## Problem #1: Protection

Once computers were built to support multiple processes and multiple users, we
began to need to protect these from each other.

Each process lives under the illusion that it's own memory space begins at
address 0. But this cannot literally be true for all processes simultaneously,
as each process may only access a portion of the entire physical address space.

The hardware itself is built to support a useful abstraction. In order to
create this partitioning of the physical memory space into multiple logical
spaces, the CPU provides two registers which denote the legal memory boundaries
for a process.

#### Base Register
Contains the smallest legal physical memory address for a process

#### Limit Register
Contains the size of the physical memory address space available to the process

![Base and Limit Registers](base_limit_registers.png)

The highest physical address a process may access is `base + limit`

Together, these registers map from "Logical" space to "Physical" space

Q. How does the CPU/OS know where to put the Limit Register?



Lecture 28: Module4\Nov_04\README.md
================================================================

CS3100 - Module 4 - Lecture 28 - Mon Nov 04

# Announcements

## Aggies Dominated the Lucid Programming Competition

Congratulations to the USU teams who crushed the Lucid Programming Competition
this past Saturday.

[Lucid Programming Competition Leaderboard](https://contest.golucid.co/)



# Topics:
* Assn4 due on Wednesday
* 8.1.3 Logical Versus Physical Address Space
* 8.1.5 Dynamic Linking


----------------------------------------------------------------------------
# Assn4 due on Wednesday

What questions or issues do you have?



# 8.1 Main Memory: Background

The Operating System tries to strike a balance between three demands with its
approach to the main memory of a computer:

## *REVIEW* Problem #0: Speed

* Fetching instructions to execute
* Fetch/store the data those instructions operate upon
* Work with limited registers & RAM
* Minimize CPU stalls


## *REVIEW* Problem #1: Protection

Computers built to support multiple processes and multiple users need to
protect these from each other.


## Problem #2: Binding

Recall that a program is an inert entity on disk. When it is copied into RAM
and begins execution it becomes active, and those instructions encoded within
the program need to know where their addresses point to.

How can an on-disk program possibly know what values its base and limit
registers will take at runtime?

What if you have multiple instances of the same program running? Must they
share the same address space?


#### Binding
Mapping addresses within a program to locations within a processes' memory space 

Three possibilities exist here:

1.  *Compile-time binding*: Assign memory addresses statically within the
    program's text section.


#### Absolute code
Program instructions which encode physical memory addresses; the compiler
"knows" where this program will reside in memory when it's running

2.  *Load-time binding*: When the program is loaded the OS selects a value for
    the base register and edits all instruction's memory access operands to
    account for this offset



#### Relocatable code
Program instructions are modified at load-time to account, offsetting by the value in the processes' base register

3.  *Execution-time binding*: When an executable may be moved from place to
    place in memory at runtime, binding must be delayed until runtime. Special
    CPU hardware is required for this to be possible (MMU).

   This creates a 3rd kind of memory space called *virtual memory*.  We'll cover
   *virtual memory* in more depth in Chapter 9.  Mainstream OSes today use
   Execution-time binding.


Q. Does the OS itself load parts of itself with Execution-time binding?



# 8.1.3 Logical Versus Physical Address Space

#### Logical Address
An address generated by the CPU

These are addresses encoded within CPU instructions; sources and destinations
of data in operations.


#### Physical Address
An address seen by the memory unit

* Compile-time and Load-time binding generate *logical* and *physical* addresses.

* Execution-time binding generates another type of address, called a *virtual address*.

* The text uses the terms *logical address* and *virtual address* interchangably. smh


#### Memory Management Unit (MMU)
Hardware device which maps virtual addresses into physical addresses

![Relocation register maps logical addresses to physical](relocation_register.png)


# 8.1.5 Dynamic Linking

#### Statically linked libraries
System libraries which are treated as other objects, combined by the loader into the program image

#### Dynamically linked libraries (DLL)
System libraries linked to user programs at run-time

#### Shared Objects (SO)
The Unix jargon for DLL


DLL's allow a program to decide, at runtime, whether or not to include some
functionality, increasing program flexibility.  You can even add functionality
to a compiled program *after* the fact by providing a DLL with a compatible
interface.



#### Stub
Small bit of code which is replaced at run-time with the matching, dynamically linked code

The stub may include information about which version of the dynamic function is
required, or where to find it, etc.


### DLL Pros:

* Enables a plug-in architecture
* Bugfixes can be made without replacing the entire application
* Operational choices can be delayed as late as possible
* Multiple versions of a library may be installed, allowing old, legacy applications to continue operating

### DLL Cons:

* Increased overhead in time
    * Runtime system must search for a file
    * Time spent reading and loading the file
* Increased overhead in space
    * Stub code costs bytes
    * Each DLL has a fixed size overhead for boilerplate code
* Possible incompatibilities between client application and a shared library
    * The interface in the DLL might not match the driver code
    * An app can load a library that is too new or too old, leading to bugs or crashes
    * "DLL Hell"

[Demo: Dymanically Linked Library demo](dll/)

### Fun stuff to try:

* Create a separate implementation of the demo function in a different file;
  choose to load one library or the other at runtime

* Create a separate implementation of the demo function with a completely
  different signature; prompt the user to choose which one you want to use



Lecture 29: Module4\Nov_06\README.md
================================================================

CS3100 - Module 4 - Lecture 29 - Wed Nov 06

# Announcements

## FSLC Linux Cool Tools

Tonight we are discussing your favorite Linux tools that make using your
computer a breeze.  Is there a program that is your best-kept secret?
Sharing is caring!

So come on down to ESLC 053 at 6pm to share your favorite cool tools!


## Assignment 4 is due today

If you are participating in the Utah State Science Week Coding Challenge on
HackerRank.com.  This contest runs from Nov 4 2019, 12:00 pm MST to Nov 8 2019,
01:00 pm MST.

You can't just sign up and get two free days; you have to demonstrate that you
are spending enough time on the coding challenge to detract from this
assignment.

To qualify for the extension, send me an email with your HackerRank username.
I'll be checking the leader board to make sure my generosity isn't being
abused.



# Topics:
* Introduce Assignment 5
* DLL demo & memory regions


----------------------------------------------------------------------------
# Introduce [Assignment 5](https://usu.instructure.com/courses/547959/assignments/2699286)


# DLL demo & memory regions

[../../Module4/Nov_04/dll/](../../Module4/Nov_04/dll/)


Watch the memory regions as the shared libraries are loaded/unloaded on your
RPi with this command:

    $ watch -d -n 1 cat /proc/$(pgrep main)/maps



Lecture 30: Module5\Nov_08\README.md
================================================================

CS3100 - Module 5 - Lecture 30 - Fri Nov 08

# Announcements

## HackUSU

USU's 24-hour hackathon - November 15-16th

Register and find more information at https://hackusu.org



# Topics:
* 8.2 Swapping
* 8.3 Contiguous Memory Allocation
* 8.3.2 Memory Allocation
* 8.3.3 Fragmentation
* 8.4 Segmentation
* 8.5 Paging
* 8.5.4 Shared Pages


----------------------------------------------------------------------------
## Intro video

[What is DOS Protected Mode? | Nostalgia Nerd](https://www.youtube.com/watch?v=XAyQLV5bbb0)


## Memes

![NullPointerException vs. NullReferenceException](NPE_NRE.jpg "NullPointerException vs. NullReferenceException")


# 8.2 Swapping

Last time we discussed the possibility of a running process being copied from
RAM onto the Disk (or s ome other, slower "backing store" that's larger than
RAM) when it has been idle for a long time.

#### Swapping
Moving a process's memory image from RAM onto a backing store, or vice versa.

This gives us the illusion of (nearly) unlimited RAM, but at the cost of speed.
When your computer is going slow, and you hear the HD clicking and see the HDD
access light flickering, this is probably what's going on.

We will now discuss the problems we run into with regards to juggling many
processes' images in memory. Keep these problems in mind because they are
magnified 10,000 fold when swapping is involved because the same problems can
occur there, except they take much longer to play out.

#### Thrashing
Said of a process that is so busy swapping data back and forth to the backing
store that it spends more time in this activity than in doing useful work



# 8.3 Contiguous Memory Allocation

This section deals within the framework of physical memory.

The CPU cannot directly access disk drives; it may only access Registers and
RAM. Therefore, a program must be copied into main memory in order to become a
running process.

An early method of arranging many processes in memory is contiguous memory
allocation.

#### Contiguous Memory Allocation
Put the entire process image into a single extent of memory

*What problems can you envision for the contiguous memory allocation scheme?*

* If the free memory isn't contiguous, you can run out of memory while still
  having enough memory - it's just not in a useful position


# 8.3.2 Memory Allocation

Instead of just dividing up the RAM by entire procesess, we'll divide RAM into
many fixed-size partitions. Think of the level of organization created by
dividing a parking lot into stalls instead of just letting anybody park
wherever they wish (or how nice a parking lot becomes after a snowstorm before
the plows have a chance to clear it off).

#### Partition
Fixed-size region of memory which contains exactly one process

*What problems can you envision for the fixed partition allocation scheme?*

* Your partition size limits how large a process can be
    * If I choose a partition size that's too small, lots of programs won't run
      on my system
    * If I choose a partition size that's too big, I'm wasting lots of space

### Variable Partition Method
OS keeps track of which parts of memory are used and which are available;
processes are given a chunk of memory based upon its needs

* The OS gives out a parking stall that's just the right size for your car (process)
* The chunks of memory must still be contiguous

#### Hole
A block of available memory from which the OS may draw

When a process begins, the OS searches for a hole that is large enough to
accommodate the process. When it finds a hole that is larger than needed, the
OS gives part of it to the process, and the remainder becomes a smaller hole.

*What problems can you envision for the variable partition method?*


#### Dynamic Storage-Allocation Problem
Concerned with how to satisfy a request of size *n* from a list of free memory holes

There are three common strategies to solving this problem:

* First-Fit: Allocate the 1st hole in the list which is large enough for this request
* Best-Fit: Scan the entire list and allocate the smallest hole which is just
  large enough; this leaves the smallest remaining hole
* Worst-Fit: Scan the entire list and allocate the largest hole, leaving behind
  the largest hole

#### Which strategy is best?

Simulations have shown that 1st-fit and best-fit are better than worst-fit in
terms of storage space efficiency and time. 1st-fit is faster than best-fit,
and these are approximately equal for storage space efficiency.
  

# 8.3.3 Fragmentation

With all of these leftover holes, we have to decide what to do about them.
When holes become too small they are very unlikely to be useful at all.

#### External Fragmentation
When the free holes are not contiguous, then we arrive at a situation where
there is enough free memory in the system to satisfy the request, but it is not
usable.


#### Internal Fragmentation
When memory allocated to a process is slightly larger than needed memory; this
size difference is memory internal to a partition, but is still unused memory


#### Compaction
Solve the problem of external fragmentation by shuffling memory contents to
place all free memory together in one large block.

Compaction is possible only if relocation is dynamic, and is done at execution-time.
Absolute Code bound at compile-time and load-time relocatable code cannot have
compaction applied to it.

Now you know why modern, mainstream OSes use execution-time binding.


# 8.4 Segmentation

This section deals within the framework of logical memory. The idea of
segmentation relates to the view of memory that a programming language gives
you as a programmer.

We think in terms of "stack", "heap", globals and text data (code). Each of
these can be thought of as distinct segments of memory, each to their own
purpose.

In other words, a logical address space is a collection of segments. Each
segment has its own size, and the program knows where to find them at run time.

The advantage of this view of things is that it supports a non-contiguous
address space for a program. The disadvantage is that the segments may have
arbitrary sizes, leading to external fragmentation :(


Now, recall that all of these problems that happen in RAM can *also* happen to
our swap space, except there it's 10,000X worse!

# 8.5 Paging

Finally, we've arrived at the method used by modern OSes, which combines the
advantages of fixed-size partitions with a way to minimize the amount of
thrashing and fragmentation that occurs on the backing store.


#### Frames
Fixed-size blocks of physical memory

#### Pages
Fixed-size blocks of logical memory

Paging works by partitioning memory (and the backing store) into fixed-size
blocks and allocating these to processes as needed. This avoids external
fragmentation because there are no blocks of memory which are too small to be
useful.


The CPU keeps track of the mapping of pages to frames with a page table. 

#### Page Table
A table mapping pages to memory frames.  Given a page number, the page table
returns the physical address at which this page begins

![Paging Hardware](paging_hardware.jpg)


### Address Translation Scheme
With the addition of a page table, the addresses used by the CPU will now look
a little bit different. An address generated by CPU is a 2-tuple: (p, d)

* Page number (p)
    used as an index into a page table which contains base address of each page
    in physical memory

* Page offset (d)
    combined with base address to define the physical memory address that is
    sent to the memory unit

![Address Translation Scheme](page_num_offset.png)


With paging, internal fragmentation is a risk: if a process only needs to
allocate 1 byte it may be given a 4k block. However, this is the most memory a
process can possibly waste.

![Paging model of Physical and Logical Memory](paging_model_of_logical_phys_mem.png)

![Paging Example](paging_example.png)


Many modern hardware platforms support paging by providing hardware which
manages a page table.

The Page table itself is kept in main memory

#### The page-table base register (PTBR) points to the page table

#### The page-table length register (PTLR) indicates size of the page table

In this scheme every data/instruction access requires two memory accesses

* One for the page table 
* One for the data / instruction

Thus, memory access is slowed by a factor of `2` :(


The two memory access problem can be solved by the use of a special fast-lookup
hardware cache called associative memory or translation look-aside buffers
(TLBs)


#### Translation Look-aside Buffer

High-speed, associative memory cache

The TLB is given a page number. It is able to look for that page number in all
of its entries *simultaneously*. In order for it to be that fast, it must be
quite small.

![Paging Hardware + TLB](paging_hardware_with_TLB.png)


# 8.5.4 Shared Pages

Paging combined with Execution-Time binding offers an attractive possibility;
with memory nicely partitioned into small chunks, we can avoid the possibility
of filling our frames with duplicated data from common processes by *sharing*
those identical pages among many processes.

*What problems can you envision for the shared page allocation scheme?*

These pages must be read-only. The code they host must be reentrant (or pure code)

#### Reentrant (Pure) Code
Non self-modifying code

![Shared Pages Example](shared_pages_example.jpg)


Lecture 31: Module5\Nov_11\README.md
================================================================

CS3100 - Module 5 - Lecture 31 - Mon Nov 11

# Announcements

## inovint.com

* Make a profile
* Post your skills
* Network with friends 
* Start the next million dollar company

For more information
* email: alexjigo903@outlook.com
* phone: 385.260.7903


## AIS CyberSecurity Club Meeting

Matt Lorimer of USU IT is presenting on the `nmap` network analysis tool

* 6pm Thursday, 11/14
* Huntsman Hall (HH) 220




# Topics:
* 8.5 Paging
* Chapter 9: Virtual Memory
    * 9.1 Virtual Memory
    * 9.2 Demand Paging


--------------------------------------------------------------------------------
# 8.5 [Paging](../Nov_08/README.md#85-Paging)


# 9.1 Virtual Memory

#### Virtual Memory (VM)
Essentially equivalent to the concept of *logical memory* introduced in Chapter 8

There isn't any strong consensus on the distinction between logical & virtual memory.


#### Virtual Address Space
This can be much, much larger than the available physical memory


VM also allows files and memory to be shared by two or more processes through
page sharing.

* Common libraries needed by many processes can be loaded into RAM once, and
  those pages can be viewed by each process as belonging to them exclusively

* Shared Memory Interprocess Communication can be implemented through shared
  pages

* Pages can be shared between parent/child processes across fork() system call,
  speeding up that method of process creation



# 9.2 Demand Paging

By dealing with memory a page at a time, another exciting possibility arises.
What if we could execute a process without loading the entire program into
memory? Instead of taking the time to copy the entire program into the process
image, we could just copy the first bit of main(). When we come to a point in
the program where we need more pages of code or data, we'll bring those in,
as-needed.

#### Demand Paging
Load a process into memory one page at a time, and only as needed

Pros:

* Less I/O needed, no unnecessary I/O
* Less overall memory needed 
* Faster response
* Support more users

#### Pager
Part of the kernel which decides which pages must be in memory

A pager which only brings pages into memory when they are actually needed is
called a *lazy swapper*

#### Memory resident
Said of pages which are loaded into physical memory frames

What is a system like with a pager?

* When pages needed are already memory resident:
	+ No difference from non demand-paging
* If page is needed and is not memory resident:
	+ Need to detect and load the page into memory from storage
	+ Without changing program behavior
	+ Without programmer needing to change code

To support demand paging the Memory Management Unit (MMU) needs to augment its
page table to keep track of the *memory resident* status of each page

When the MMU sees a request for a non-resident page, a *page fault* occurs

#### Page fault
A trap into the OS which occurs when a non-resident page is requested

To resolve a page fault, the operating system must:

1. Look at another table to decide whether this reference is even valid (or a seg fault)
	+ Invalid reference => abort
	+ Valid, but not resident
2. Find a free frame
3. Swap page into frame via scheduled disk operation
4. Reset page tables to indicate page now in memory
5. Restart the instruction that caused the page fault

In the extreme case, we can start a process with *zero* pages in memory.

#### Pure Demand Paging
Use the page fault procedure to handle *all* of our page loading



Lecture 32: Module5\Nov_13\README.md
================================================================

CS3100 - Module 5 - Lecture 32 - Wed Nov 13

# Announcements

## FSLC Meeting: CyberSecurity competitions

You are invited to a panel discussion with USU cybersecurity competitors just
participated in the NIATEC Invitational this past weekend.  This meeting is for
you if you have ever wondered:

1. How do I get involved with computer security?
2. What is a CyberSecurity competition like?
3. How does a team prepare for a competition like this?
4. What is it like to get hacked by a *real* Red team?

* Tonight @ 6pm
* ESLC room 053


## AIS CyberSecurity Club Meeting

Matt Lorimer of USU IT is presenting on the `nmap` network analysis tool

* 6pm Thursday, 11/14
* Huntsman Hall (HH) 220


## Lecture cancelled this Friday, Nov 15

Use this extra time to work on Assignment 5 or participate in the HackUSU hackathon.



# Call on 2 designated questioners


# Topics:
* 9.4 Page Replacement
* 9.4.1 (p. 410) Basic Page Replacement
* 9.3 Copy On Write


----------------------------------------------------------------------------
# 9.4 Page Replacement

#### Degree of multiprogramming
The maximum number of processes that a single-processor system can accommodate efficiently

#### Over-allocation
Running more processes than the system has physical memory to support

By over-allocating memory we are able to increase the degree of
multiprogramming on the system. Demand paging lets us get away with this...
some of the time. At some point, however, we'll have to make a tough decision.

* Q. What happens if there is no free frame for this page I must load?
* A. Find a page which is resident but not really being used right now, and swap it out.

Page replacement completes separation between logical memory and physical
memory.

Large virtual memory can be provided on a smaller physical memory

It is desirable that we have an algorithm which will result in the minimum
number of page faults.


# 9.4.1 (p. 410) Basic Page Replacement

When a process requires a non-resident page and triggers a page fault,

1. Pause the process

2. Find the location of the desired page on disk

3. Find a free frame:
	+ If there is a free frame, use it
    + If there is no free frame, use a page replacement algorithm to select a
      victim frame
	+ Write victim frame to disk

4. Bring the desired page into the (newly) free frame; update the page and
   frame tables

5. Continue the process by restarting the instruction that caused the page
   fault

Note that now there are potentially 2 page transfers per page fault :(


## Evaluating A Page Replacement Algorithms

1. Choose the number of frames of physical memory which exist in our system
2. Create a sequence of simulated page requests
3. Count the number of page faults which would occur in such a system

Do this over and over again to decide how well this page replacement algorithm
will perform IRL

#### Belady's Anomaly: adding more frames may lead to *more* page faults!

This phenomenon is the subject of your final homework assignment coming up on
Nov 20th [Assn6 - Page Replacement & Belady's Anomaly](https://usu.instructure.com/courses/547959/assignments/2699287)

Simulate the FIFO page replacement algorithm (textbook section 9.4.2) for
different numbers of frames to detect occurrences of Belady's Anomaly



# 9.3 Copy On Write

> Don't have a cow, man!
>
> -- Bart Simpson

Shared pages can make forking a process very quick indeed in the case where two
processes share read-only text data.

Because the common use-case of `fork()` is to immediately follow it with a call
to `exec()`, the OS can save itself much work by not even copying pages destined
to be immediately thrown away.

In the event that a child process *does* want to change some of its
non-readonly memory, however, a shared page invites inadvertent Shared Memory
access. The OS can avoid this over-sharing by marking shared pages with a
Copy-On-Write flag. When either process modifes one of its shared pages, the OS
at this time will step in and make a copy of the page, remapping the virtual
address space of the child process to replace the common page with the copy.

This is a common optimization used by many mainstream OSes, including Windows,
Linux and Solaris.

We can observe this optimization for ourselves by forking a process with a
large allocation of writable shared pages, and then modifying them.

### Demo: [cow/](cow/)



Lecture 33: Module5\Nov_18\README.md
================================================================

CS3100 - Module 5 - Lecture 33 - Mon Nov 18

# Announcements

## FSLC Open Source Game Night

* Come relax and de-stress before finals week sucks the fun out of life
* Play Open Source games against each other
* Pizza will be provided

+ Wednesday, 11/20
+ 6pm @ ESLC room 053

FSLC now has a [Discord!](https://discord.gg/RHppcek), and you're invited!





# Topics:
* 9.4.3 Optimal Page Replacement
* 9.4.4 Least Recently Used PR Scheme
* 9.6 Thrashing


----------------------------------------------------------------------------
# 9.4.3 Optimal Page Replacement

Previously, we explored the simple, FIFO page replacement scheme, and observed
how it may suffer from Belady's anomaly, that is, the FIFO page replacement
scheme may perform worse when increasing the number of frames in a system.

The best possible page replacement scheme would know which page will not be
needed for the greatest length of time and replace it.

#### Optimal Page Replacement (OPT)
Replace the page that will not be used for the longest period of time

Of course, this algorithm suffers from a serious flaw: without a time-machine
we won't be able to know which pages have the property of not being needed for
the longest period of time. But don't let that stop you from using OPT as a
convenient standard to measure against; we can always compare our
*implementable* PR scheme against OPT as a measurement of how well it performs.


# 9.4.4 Least Recently Used PR Scheme

By using the recent past as an approximation for the imminent future we arrive at the LRU algorithm.

#### Least Recently Used Algorithm (LRU)
Replace page that has not been used in the most amount of time

How might we implement this algorithm?
* Use a clock or a counter to help us track when we last *used* a page (reads
  or writes), augmenting the page table to have a field to contain this info.
  This means that even reading memory requires us to write to the page table.

  We must also scan the page table looking for the oldest page whenever we need
  to replace a page.
  
* Use a doubly-linked list-based stack; each time we change a page, move it to
  the top of the stack.

  Finding the oldest page is fast as it's at the bottom of the stack. If we
  keep a pointer pointing to the bottom of the stack, we don't even have to
  traverse the list

It has been proven that the LRU algorithm cannot suffer from Belady's anomaly.
All at the low, low cost of always modifying the page table for each and every
access!

LRU is nice on paper, but very few systems actually use it. 


# 9.6 Thrashing

If a process does not have "enough" pages, the page-fault rate is very high

* Page fault to get page
* Replace existing frame
* But quickly need replaced frame back
* This leads to:
    + Low CPU utilization
    + Operating system thinking that it needs to increase the degree of multiprogramming
    + Another process is added to the system, making the paging situation even worse


#### Thrashing: when a process spends more time swapping pages in and out than it spends doing useful work

![Thrashing limits benefit of multiprogramming](thrashing.jpg)



Lecture 34: Module6\Nov_20\README.md
================================================================

CS3100 - Module 6 - Lecture 34 - Wed Nov 20

# Announcements

## Assignment #5 due tonight at midnight

As a reminder, the grading gift cannot be used on the final assignment.
Assn5 is the last time you'll be able to use the grading gift.

Please take the [Assignment 5 effort survey](https://usu.instructure.com/courses/547959/quizzes/752358)
which helps me improve the assignments.


## FSLC Open Source Game Night

* Come relax and de-stress before finals week sucks the fun out of life
* Play Open Source games against each other
* Pizza will be provided

+ Tonight, 11/20
+ 6pm @ ESLC room 053

FSLC now has a [Discord!](https://discord.gg/RHppcek), and you're invited!


# Call on 2 designated questioners


# Topics:
* Introduce [Assignment 6](https://usu.instructure.com/courses/547959/assignments/2699287)
* Improving performance of systems using Virtual Memory
* 9.6.2 Working-Set Model
* 9.7 Memory-Mapped Files
* Interacting with Linux's Virtual Memory system
* Fun Linux Kernel Tricks


----------------------------------------------------------------------------
# Introduce [Assignment 6](https://usu.instructure.com/courses/547959/assignments/2699287)


# Improving performance of systems using Virtual Memory


## System 0

Consider a demand-paging system with the following time-measured utilizations:

| Hardware       | Utilization
|:--------------:|------------
| CPU            |     33.4%
| Swap Disk      |     95.7%
| Filesystem I/O |      6.1%
| RAM            |     98.7%
| # of tasks     |      200

1. What would you say is going on with this system?
    *   Thrashing

2. Where is the bottle neck?
    *   Swap disk is too full & too slow
    *   Not nearly enough RAM

3. How much useful work is being done on this system?
    *   Not a lot

4. What would you suggest in order to improve this system's performance?

- Install a bigger swap device
- Install a faster swap device
- Install more RAM


## System 1

| Hardware       | Utilization
|:--------------:|------------
| CPU            |    100.0%
| Swap Disk      |      0.2%
| Filesystem I/O |      2.2%
| RAM            |     14.9%
| # of tasks     |      150

1. What would you say is going on with this system?
    *   A CPU-bound process has taken over the system

2. Where is the bottle neck?
    *   The CPU can't keep up with its work

3. How much useful work is being done on this system?
    *   Depends on whether the CPU-bound process is stuck in an inf. loop, or
        is doing good work 

4. What would you suggest in order to improve this system's performance?

- Install a faster CPU
- Decrease the degree of multiprogramming


## System 2

| Hardware       | Utilization %
|:--------------:|--------------
| CPU            |      4.7%
| Swap Disk      |      1.5%
| Filesystem I/O |    100.0%
| RAM            |     50.1%
| # of tasks     |      100

1. What would you say is going on with this system?
    *   I/O bound process

2. Where is the bottle neck?
    *   Hard disks - the main filesystem

3. How much useful work is being done on this system?
    *   Not as much as we'd like

4. What would you suggest in order to improve this system's performance?

- Install a bigger, faster hard drive (add an SSD)
- Install multiple hard drives
- Look into *where* the process is doing its I/O; perhaps a kernel thread can
  do *all* of the I/O, freeing up the other threads to do CPU work


## System 3

| Hardware       | Utilization
|:--------------:|------------
| CPU            |     99.7%
| Swap Disk      |      0.0%
| Filesystem I/O |     27.5%
| RAM            |     98.1%
| # of tasks     |   10,090

1. What would you say is going on with this system?
    *   Running out of RAM, lots of proceses
    *   A fork bomb might look like this

2. Where is the bottle neck?
    *   *Way* too many processes

3. How much useful work is being done on this system?
    *   Probably none - all CPU resources are in the Kernel mode, doing system
        calls

4. What would you suggest in order to improve this system's performance?

- Decrease the degree of multiprogramming


## System 4

| Hardware       | Utilization
|:--------------:|------------
| CPU            |      0.9%
| Swap Disk      |      0.0%
| Filesystem I/O |    100.0%
| RAM            |     18.9%
| # of tasks     |       82

1. What would you say is going on with this system?
    *   Very I/O Bound

2. Where is the bottle neck?
    *   The main filesystem

3. How much useful work is being done on this system?
    *   Doesn't look like much

4. What would you suggest in order to improve this system's performance?

- Replace failing hard drive


One approach to limit the effects of thrashing is to observe which frames
belong to which process, and prevent that process from stealing frames from
other processes which would set off this vicious cycle.

#### Local Replacement Algorithm
When one process has run out of frames, don't allow it to steal frames from other processes

This approach requires us to set a limit on how many pages a process needs, and
knowing when to say "enough is enough". How can we know this?


# 9.6.2 Working-Set Model

Look at how many frames a process is using right now, and then observe the
pattern of "where" those frames are. Code is organized into routines. When you
enter a function it is likely that all of the code you need to execute is
bundled together into one location. You won't for example, be able to use the
pages comprising your earlier stack frames until you return from this function.

This assumption underpins all of our approaches to caching. After all, if a
processes' memory access was truly random no caching scheme would be of any
value.

#### Locality model
Process execution migrates from one address space locality to another

When the sum of all localities exceeds your physical frames, you are forced
into thrashing.

The book contains a visualization of a processes' memory-reference pattern,
allowing us to see what a locality looks like:

![A processes' Locality pattern visualized](locality_pattern.jpg)



# 9.7 Memory-Mapped Files

We've studied pure demand paging in which an OS relies entirely on its demand
paging system for all disk-to-memory operations.

Our applications can take advantage of this through an OS API known in Unix as
`mmap()`. The result is that we use an array which is transparently connected to
a file on-disk. Searching for the right byte in the file becomes equivalent to
scanning an array with a for-loop. Array update operations now behave like
`read()`/`write()` system calls.


#### Memory-Mapped Files: treat file I/O as routine memory access

The `mmap()` system call works by associating a disk block with a page of
memory (another reason to favor page-sizes which are multiples of disk blocks).

The file is originally read into memory via demand paging.

But when does written data make it to disk? It happens periodically and / or at
file `close()` time; the user doesn't have to manually see to it ;)

![mmap()](mmap.jpg)


We can even combine the concepts of mmap with shared-memory to share a common
file between processes at the speed of RAM

![mmap() Shared Memory](mmap_shm.jpg)


### Demo: [mmap/](mmap/)


# Interacting with Linux's Virtual Memory system

Your OS is able to take advantage of many optimizations as a result of
demand-paging. The most obvious ones involve caching ordinary disk I/O
operations in unused portions of RAM.

You are now able to understand some more of what htop's pretty color-coded
memory bar has been telling you about your memory use all along.


Enter htop's help screen with the F1 key. It describes the memory bar like this:

    Memory bar:    [used/buffers/cache                            used/total]

* used (green)
  These are frames filled with the pages of running processes: the kind of
  memory we've mostly been discussing these past two chapters

* buffers (blue)
  These frames contain filesystem metadata: information about files on disk
  which are not part of the file's contents. Paths, ownership information,
  permissions, timestamps, etc.

* cache (yellow)
  These frames hold blocks of hard disk data.  Every time you read a file it's
  copied from the disk into RAM anyhow. The OS may as well hold onto it on the
  chance that you need it again.

  This filesystem cache acts like an automatic mmap().
  

Armed with this knowledge, we can observe the effects of our commands on the
system and infer what the OS is doing in response.


--------------------------------------------------------------------------------
# Fun Linux Kernel Tricks

*Note:* In the examples below, commands beginning with a `$` prompt are
intended to be run as an ordinary user.  Commands prefixed with a `#` prompt
denote commands which must be run as the root user.

The Linux Kernel makes it possible for us to poke around with some aspects of
its Virtual Memory system through special files in the /proc directory.


## System memory information /proc/meminfo

This file reports statistics about memory usage on the system

    $ cat /proc/meminfo


## Observing memory fragmentation with /proc/buddyinfo

Recall that we discussed fragmentation back in Chapter 8. The Linux kernel
exposes some of its controls to us through virtual files in the /proc
directory.

By reading from and writing to these files, we can learn a little bit about how
the Linux virtual memory system works.


## From the manpage `proc(5)`:

> This file contains information which is used for diagnosing memory
> fragmentation issues.  Each line starts with the identification of the node and
> the name of the zone which together identify a memory region This is then
> followed by the count of available chunks of a certain order in which these
> zones are split.

    $ watch -d -n.1 cat /proc/buddyinfo


## Compacting memory with `/proc/sys/vm/compact_memory`

> When 1 is written to this file, all zones are compacted such that free memory
> is available in contiguous blocks where possible. The effect of this action
> can be seen by examining /proc/buddyinfo.


## Dropping caches with `/proc/sys/vm/drop_caches`

> Writing to this file causes the kernel to drop clean caches, dentries, and
> inodes from memory, causing that memory to become free. This can be useful for
> memory management testing and performing reproducible filesystem benchmarks.
> Because writing to this file causes the benefits of caching to be lost, it can
> degrade overall system performance.

You choose how many caches to drop by writing values 1, 2, or 3 to this file, 3
being the value that drops the most caches.

> Because writing to this file is a nondestructive operation and dirty objects
> are not freeable, the user should run sync(1) first.

    # echo 3 > /proc/sys/vm/drop_caches


Well, since you mention it...

    # time find /usr/bin -type f -exec cat '{}' > /dev/null \;
    # time find /usr/bin -type f -exec cat '{}' > /dev/null \;   # notice how fast this is the 2nd time!
    # time find /usr/share -type f -exec cat '{}' > /dev/null \; # this really fills up your RAM
    $ watch -d -n.1 cat /proc/buddyinfo
    $ htop
    # sync; echo 3 > /proc/sys/vm/drop_caches
    # echo 1 > /proc/sys/vm/compact_memory


## Controlling the system's "swappiness" with `/proc/sys/vm/swappiness`

The value in this file controls how aggressively the kernel will swap memory
pages. Higher values increase aggressiveness, lower values decrease
aggressiveness.  The default value is 60.

    $ cat /proc/sys/vm/swappiness



Lecture 35: Module6\Nov_22\README.md
================================================================

CS3100 - Module 6 - Lecture 35 - Fri Nov 22

# Announcements

# Call on 2 designated questioners


# Topics:
* 9.7 Memory-Mapped Files
* Interacting with Linux's Virtual Memory system


----------------------------------------------------------------------------
# 9.7 Memory-Mapped Files

We've studied pure demand paging in which an OS relies entirely on its demand
paging system for all disk-to-memory operations.

Our applications can take advantage of this through an OS API known in Unix as
`mmap()`. The result is that we use an array which is transparently connected to
a file on-disk. Searching for the right byte in the file becomes equivalent to
scanning an array with a for-loop. Array update operations now behave like
`read()`/`write()` system calls.


#### Memory-Mapped Files: treat file I/O as routine memory access

The `mmap()` system call works by associating a disk block with a page of
memory (another reason to favor page-sizes which are multiples of disk blocks).

The file is originally read into memory via demand paging.

But when does written data make it to disk? It happens periodically and / or at
file `close()` time; the user doesn't have to manually see to it ;)

![mmap()](mmap.jpg)


We can even combine the concepts of mmap with shared-memory to share a common
file between processes at the speed of RAM

![mmap() Shared Memory](mmap_shm.jpg)


### Demo: [mmap/](mmap/)


# Interacting with Linux's Virtual Memory system

Your OS is able to take advantage of many optimizations as a result of
demand-paging. The most obvious ones involve caching ordinary disk I/O
operations in unused portions of RAM.

You are now able to understand some more of what htop's pretty color-coded
memory bar has been telling you about your memory use all along.


Enter htop's help screen with the F1 key. It describes the memory bar like this:

    Memory bar:    [used/buffers/cache                            used/total]

* used (green)
  These are frames filled with the pages of running processes: the kind of
  memory we've mostly been discussing these past two chapters

* buffers (blue)
  These frames contain filesystem metadata: information about files on disk
  which are not part of the file's contents. Paths, ownership information,
  permissions, timestamps, etc.

* cache (yellow)
  These frames hold blocks of hard disk data.  Every time you read a file it's
  copied from the disk into RAM anyhow. The OS may as well hold onto it on the
  chance that you need it again.

  This filesystem cache acts like an automatic mmap().
  

Armed with this knowledge, we can observe the effects of our commands on the
system and infer what the OS is doing in response.


## Fun Linux Kernel Tricks

*Note:* In the examples below, commands beginning with a `$` prompt are
intended to be run as an ordinary user.  Commands prefixed with a `#` prompt
denote commands which must be run as the root user.

The Linux Kernel makes it possible for us to poke around with some aspects of
its Virtual Memory system through special files in the /proc directory.


## System memory information /proc/meminfo

This file reports statistics about memory usage on the system

    $ cat /proc/meminfo


## Observing memory fragmentation with /proc/buddyinfo

Recall that we discussed fragmentation back in Chapter 8. The Linux kernel
exposes some of its controls to us through virtual files in the /proc
directory.

By reading from and writing to these files, we can learn a little bit about how
the Linux virtual memory system works.


## From the manpage `proc(5)`:

> This file contains information which is used for diagnosing memory
> fragmentation issues.  Each line starts with the identification of the node and
> the name of the zone which together identify a memory region This is then
> followed by the count of available chunks of a certain order in which these
> zones are split.

    $ watch -d -n.1 cat /proc/buddyinfo


## Compacting memory with `/proc/sys/vm/compact_memory`

> When 1 is written to this file, all zones are compacted such that free memory
> is available in contiguous blocks where possible. The effect of this action
> can be seen by examining /proc/buddyinfo.


## Dropping caches with `/proc/sys/vm/drop_caches`

> Writing to this file causes the kernel to drop clean caches, dentries, and
> inodes from memory, causing that memory to become free. This can be useful for
> memory management testing and performing reproducible filesystem benchmarks.
> Because writing to this file causes the benefits of caching to be lost, it can
> degrade overall system performance.

You choose how many caches to drop by writing values 1, 2, or 3 to this file, 3
being the value that drops the most caches.

> Because writing to this file is a nondestructive operation and dirty objects
> are not freeable, the user should run sync(1) first.

    # echo 3 > /proc/sys/vm/drop_caches


Well, since you mention it...

    # time find /usr/bin -type f -exec cat '{}' > /dev/null \;
    # time find /usr/bin -type f -exec cat '{}' > /dev/null \;   # notice how fast this is the 2nd time!
    # time find /usr/share -type f -exec cat '{}' > /dev/null \; # this really fills up your RAM
    $ watch -d -n.1 cat /proc/buddyinfo
    $ htop
    # sync; echo 3 > /proc/sys/vm/drop_caches
    # echo 1 > /proc/sys/vm/compact_memory


## Controlling the system's "swappiness" with `/proc/sys/vm/swappiness`

The value in this file controls how aggressively the kernel will swap memory
pages. Higher values increase aggressiveness, lower values decrease
aggressiveness.  The default value is 60.

    $ cat /proc/sys/vm/swappiness



Lecture 36: Module6\Nov_25\README.md
================================================================

CS3100 - Module 6 - Lecture 36 - Mon Nov 25

# Announcements

## Thanksgiving break starts Wednesday

* No class until next Monday, Dec 2nd.
* Enjoy your break!



# Call on 2 designated questioners


# Topics:
* Chapter 10: Mass-Storage Structure
    * 10.1.1 Magnetic Disks
    * 10.1.2 Solid-State Drives
    * 10.1.3 Magnetic Tapes
    * 10.2 Disk Structure
    * 10.3 Disk Attachment
    * 10.3.1 Host-Attached Storage
    * 10.3.2 Network-Attached Storage (NAS)
    * 10.3.3 Storage-Area Network (SAN)



----------------------------------------------------------------------------
# 10.1.1 Magnetic Disks

These devices provide the bulk of secondary storage on modern computers. Disk
systems are composed of multiple platters attached to a spindle. The disks all
spin together, and as they rotate a disk arm reaches over their surfaces,
reading 1's and 0's from the magnetic polarization of the regions that pass
beneath.

#### Platter
Flat, circular disk coated with a ferromagnetic substance

#### Head
Device which can sense and manipulate magnetic fields

#### Disk Arm
Holds the head and positions it over the surface of a platter

#### Tracks
Circular regions extending concentrically from the center of the platter

#### Cylinders
Set of tracks in all platters the same distance from the center


These disks may spin rather quickly, anywhere from ~5,000 RPM to ~15,000 RPM.
The faster the disk spins, the more rapidly data may be retrieved from it.

In order to read data from the disk we must wait for two things to occur:

#### Seek Time
The disk arm must be positioned to the correct track

#### Rotational Latency
The desired sector must rotate into position below the read head 

#### Random Access Time
The sum of the seek time and the rotational latency


The head doesn't actually touch the surface of the platter. It is suspended
just above the surface by the aerodynamic forces of the air moving above the
spinning disk.

#### Head Crash
When the read/write head contacts the surface of the disk

When a head crashes it scratches the magentic surface and obliterates the data
encoded therein. The only recourse is to have the drive mark the affected
regions unusable, or the drive must be replaced.


#### I/O Bus
the wires and data transfer protocol connecting the disk to the computer system

Common I/O busses you may have heard of include:
* IDE
* SATA
* SCSI
* USB
* Fibre Channel
* Firewire


# 10.1.2 Solid-State Drives

Nonvolatile RAM which is used as a secondary storage device. Broadly speaking
from a high-level perspective, they have many of the same characteristics as
traditional disk drives.

Pros:

* robust: no moving parts to wear out or break
* fast: no seek time for a disk arm, nor rotational latency
* energy efficient: no motors

Cons:

* cost: more expensive per GB
* shorter lifespan: limited number of read/write cycles per location

The SSD itself may be faster than the I/O bus it is connected to. Some SSDs
connect directly to the computer using the same bus which links the CPU to
other high-speed devices such as video cards or RAM.


# 10.1.3 Magnetic Tapes

Were always slower than magnetic disks, but have much larger capacities and far
lower costs. For this reason they are used for backup.

The reason a tape is slower than a disk is that random access requires spooling
the tape out to the desired position. Once the tape is in position read/write
speeds rivaling those of disks may be reached.

The closest many of you have come to a tape is with the Unix `tar` command.
`tar` stands for "Tape Archive", and was is designed to create archive files
suitable for backup to a tape device. If you read its man page you will find
some command-line arguments which make sense only for tape devices!


# 10.2 Disk Structure

As discussed before, disks transfer data by blocks of bytes instead of by
individual bytes. Most disks use a block size of 512 bytes.

#### Logical Block
The smallest unit of data a disk may transfer

Fun fact: Sector 0 of a magnetic disk drive is the 1st sector of the 1st track
on the outermost cylinder.

Each track on the disk is larger than the one that is closer to the center.
This leads to two possibilities:

1. Constant Linear Velocity (CLV) As we progress outward from the center each
   track encodes more data

   If the disk can slow its spinning as the read head moves outward, the head
   will observe that the speed of the disk beneath it is always the same.

   Tracks out from the center appear longer to the head, and contain more
   sectors. We can fit more data on the disk.

2. Constant Angular Velocity (CAV) Each track encodes the same amount of data
   regardless of its distance from the center
   
   In this scenario the rotational speed of the disk remains constant.

   Each track contains the same number of sectors, and each sector encodes the
   same number of bits. The sectors increase in size as we move away from the
   center. The density of bits per track decreases as we move away from the
   center. The head sees that the surface of the disk is moving faster when it
   is positioned over the outer tracks.



## 10.3.1 Host-Attached Storage

There are many options for how a disk may be connected to computer systems.

Connect disks directly to a single computer with a specialized disk I/O bus

Examples:
* SCSI
* IDE
* SATA



# 10.3.2 Network-Attached Storage (NAS)

Expose disks attached to a host using existing network infrastructure

Examples:
* Network File System (NFS) - used in Unix environments
* Server Message Block (SMB) - used on Wintendos
* Common Internet File System (CIFS) - a dialect of SMB

Because we're using an ordinary network, we can run into limitations of TCP
networking, and the NAS can impact the bandwidth of other users of the network.


# 10.3.3 Storage-Area Network (SAN)

Create a private, special-purpose network with specialized protocols optimized
for disk I/O.

Examples:
* Fibre Channel
* iSCSI
* InfiniBand




Lecture 37: Module6\Dec_02\README.md
================================================================

CS3100 - Module 6 - Lecture 37 - Mon Dec 02

# Announcements

## Returning Your Raspberry Pi

Return your complete Raspberry Pi kit (case, RPi computer, MicroSD card, in the
original box) by Friday, Dec 6th.  You can bring it to class or to my office.
Your grade will not go through until I have marked you off my list.  Please
contact me ASAP if there will be any issues with the return.

You will be able to buy the kits from [USU Surplus](https://www.usu.edu/surplus/)
for $40 next week.  This sale is not limited to CS3100 students, and you can
buy more than one kit.



# Call on 2 designated questioners


# Topics:
* 10.5.1: Disk formatting 
* 10.5.2: Boot block
* 10.5.3: Bad Blocks
* 10.6 Swap Space
* 10.7 RAID
* 10.7.1 Improve Reliability via Redundancy
* 10.7.2 Improve Performance via Parallelism
* 10.7.3 RAID Levels


----------------------------------------------------------------------------
# 10.5.1: Disk formatting 

#### Low-level formatting
Dividing a disk into sectors that the disk controller can read and write
(a.k.a. physical formatting)

Each sector can hold
* header information
* data
* error correction code (ECC)

A sector is usually 512 bytes of data, along with the overhead of the header and ECC

#### Logical formatting
Writing file management information and data structures to the disk in support of a file system

To use a disk to hold files, the operating system still needs to record its own
data structures on the disk. This is called "formatting" or "making a file
system"

The OS may also partition the disk into one or more groups of cylinders.
Each partition is treated by the OS as a logical disk

#### Raw Disk I/O
Accessing the data on the disk directly as an array of bytes

The OS may also allow applications to access the disk via raw I/O for
performance reasons; there is less overhead in time and space with raw access
than by going through the OS'es filesystem logic.


# 10.5.2: Boot block

## Problem:

The BIOS which bootstraps the OS needs to read the OS kernel which is
located in a file on a filesystem on the disk. If the OS hasn't been loaded,
how will the BIOS be able to understand the filesystem format of the data?

## Solution:

Just leave the 1st part of the disk unformatted, and put a simple bootstrap
program there which the BIOS can load and execute without needing an OS

This portion of the disk is called the *boot block*, and is located on a disk
designated to be the *boot disk*

#### Master Boot Record (MBR)

The first sector of the boot disk on IBM PC systems


# 10.5.3: Bad Blocks

Hard drives degrade and wear out over time. Hopefully, the head doesn't come
into contact with the surface of the disk and "crash".

When that happens, the disk controller can detect that something is wrong
because the ECC won't add up for those sectors.

* If the error is small, the ECC can be used to recover the missing data.

* If the error is big, then that's too bad :(

The disk (or the OS) can remember which sectors are bad and avoid using them in
the future. The disk may also reserve some spare sectors which are hidden from
the OS. It can logically replace the bad sector with a good one elsewhere on
the disk.

For example, suppose sector #34 has gone bad. The OS will continue to request
data from sector #34, but the disk will surreptitiously use sector #3254124791
instead. This replacement will occur even when raw disk access is used: it is
completely handled by the disk controller, and thus beyond the control of the
OS.

This is like the difference between physical RAM addresses vs. logical RAM
addresses.

# 10.6 Swap Space

Recall that virtual memory uses disk space as an extension of main memory.
The area on disk where the Virtual Memory pages reside when physical memory is
exhausted is similarly divided into page-sized chunks.

This swap area can be a dedicated partition accessed with raw I/O:

Pro:
* Faster access (it's already too slow when compared to RAM, let's not make it
  slower with the overhead of the file system)

Con:
* Once you create the partition, it's a big pain to resize it later

The swap area may instead be stored in a *swap file* residing on the file
system with all of the other files. As it depends upon ordinary file system I/O,
it's pros/cons are the opposite of the swap partition.


# 10.7 RAID Redundant Array of (Inexpensive|Independent) Disks

As storage costs have plummeted it has become feasible to throw money at the
problem of reliable and efficient storage. By combining many disks into one
logical storage system we avoid putting all of our data into one basket, so to
speak.

We are also able to parallelize disk I/O, improving throughput of the system.


# 10.7.1 Improve Reliability via Redundancy

#### Mirroring
Duplicating all data on entire disks

The most obvious approach is to use two disks instead of one. Each disk is a
perfect copy of the other, until that fateful day when the backup image is
required.

Mirroring halves the amount of space available (we're using two disks to do the
job of one, after all) and neither hurts nor improves performance: the data
still exists serially on each disk, thus reads/writes to/from the disk are
limited by the throughput of an individual disk.


# 10.7.2 Improve Performance via Parallelism

#### Data striping
Spreading blocks of data across multiple disks

Instead of treating each block of data as an indivisible unit, we can slice the
block into stripes, storing a fraction of the block on many disks at once. Now
reads/writes can occur in parallel across N disks, meaning that each read/write
operation takes only 1/N as long.

Striping alone does not improve reliability. In fact, striping *increases* our
chances of data loss, because instead of depending upon the odds of 1 disk
failing, we're dependant upon the odds of 1:N disks failing. As we incorporate
more disks we into this system we increase the chance of experiencing a failure
in any one of them.


# 10.7.3 RAID Levels

The correct answer is to combine the concepts of mirroring with striping, with
a little pinch of ECC thrown in.

At the low, low cost of extra disks, we can stripe our data along with ECC
across many disks. We again reap the benefits of parallelism, and a failure in
any one disk won't be enough to stop us. Provided that single failed disk can
be replaced before *yet another* disk fails.

There are many ways to combine mirroring, striping and error correction. The
common configurations are called RAID levels.

![RAID Levels](raid.jpg)

* RAID level 0: Striping for performance only

* RAID level 1: Disk mirroring.
    No performance gain and 50% reduction in storage capacity

* RAID level 2: Memory-style ECC.
    Data from one lost disk can be recovered from the remaining disks in the system.
    Requires fewer disks than simple mirroring
    Striping improves performance

* RAID levels 3&4: (Bit|Block)-interleaved parity
    Like level 2 but requires only 1 extra disk per 4 data disks
    The extra disk in the set contains only parity ECC data

* RAID level 5: Block-interleaved distributed parity
    Like level 4 but parity data is spread across all disks in the array

* RAID level 6: P + Q redundancy scheme
    Like level 5 in that redundancy data is spread across disks, but more of it is kept.
    This means that RAID level 6 arrays are resilient against multiple disk failures.
    Consequently, extra storage is needed for this extra redundancy data.



Lecture 38: Module6\Dec_04\README.md
================================================================

CS3100 - Module 6 - Lecture 38 - Wed Dec 04

# Announcements

## The Testing Center is booked up - here's what you need to do

The testing center is now completely booked. However, they will not turn
anybody away and you will be able to take your exam. It will just take some
planning on your part.

The testing center takes walk in appointments on a first-come, first-served
basis. Due to the increasing popularity of the testing center, you should
expect to wait between 30-60 minutes to get a seat. Because scheduled
appointments start at the top and bottom of the hour, you may find your wait
time is reduced if you arrive at the quarter hours. Walk-ins have less of a
wait earlier in the week.


## DC435 Meeting Tomorrow night

Intro to appsec by llamapope

Space will be open at 6:30 and meeting will kick off at 7:00pm.

We currently meet at Bridgerland Technical College campus located at 1301 N 600 W, Logan, UT 84321 - Room 840



# Call on 2 designated questioners


# Topics:

----------------------------------------------------------------------------
# File Types

Some operating systems encode information about a file's purpose and what
applications may use it into the file metadata.  Some OSes encode this info
into the filename.  Some OSes leave determining file type up to each
application.  Unix is this sort of OS.


## Do you believe in magic?

    https://asecuritysite.com/forensics/magic

The beginning bytes of many types of files include a "magic number" which
identifies a file to an application.  You can view a file's magic number by
running it through a hexdump program such as `xxd`:

    xxd FILENAME | head


[demo: sample files of various kinds](magic/)

Ever wonder why MS-DOS/Windows executables all begin with 'MZ'? Shouldn't that
be 'M$' or at least 'MS'?
    https://en.wikibooks.org/wiki/X86_Disassembly/Windows_Executable_Files#MS-DOS_header


You don't need to learn all of the magic numbers by heart.  On Unix systems the
`file` program scans files for their magic numbers and reports their type and
purpose.

You can find out information about that random archive which was attached in
that email from the Nigerian Prince before you extract it:

    $ file r.zip
    r.zip: Zip archive data, at least v2.0 to extract

    $ file r.tar.gz
    r.tar.gz: gzip compressed data, from FAT filesystem (MS-DOS, OS/2, NT)

Incidentally, these archives contain perfect copies of themselves:
Archiveception. You can unzip these files forever, but watch out when you get
to the part with the skiing henchmen with machine guns (or was it the skiing
scene with the abominable snowman? I can never keep my skiing scenes straight).

    $ while unzip r.zip; do cd r; pwd; done

    $ while tar xf r.tar.gz; do cd r; pwd; done



# File-System Mounting

You will have noticed that Unix dispenses with the awkward convention of "disk
drives" being root file systems in their own right. Every file system in Unix
is attched to the same file tree, including file systems which aren't of the
same device, including file systems which aren't *real* in the sense that they
are in no way related to mass-storage devices. The end result is a single,
unified namespace for all entities which may be accessed under the file system

When a new file system is brought online in a Unix system it is grafted onto the
root file system. This process is called *mounting a file system*.

#### Mount
Attach a file system contained in a separate volume onto the extant
heirarchical tree of files and directories

The location which the new volume's file system is attached is called a *mount
point*.

#### Mount Point
A directory onto which a file system is attached to the main tree

Ordinarily, the directory which is designated to be a mount point for another
file system is left empty. This is because any files and subdirectories
contained within the mountpoint become inaccessible while the file system is
mounted there. In other words, once the new file system is mounted, the names
of files contained within the mountpoint refer to files on the new volume, and
not the old one.

On Unix we use the `mount` command to associate a volume with a directory and
attach the files and directories contained within the volume into the main file
system.


*You may also view a listing of mounted file systems by running `mount` with no arguments*


The `umount` command is used to unmount a file system (notice that the
command's name is missing an 'n'). In order for the unmount operation to be
successful, all files in the target volume must be closed. This includes
directories, which are held open by processes using them as their CWD.


# Stupid Raspberry Pi Tricks: create a file system within a file ... in your file system

One of the nice things about Linux is that there are many commands available
which enable you to manipulate file systems. Combined with the flexibility that
Unix's orthogonal design brings, we can perform experiments safely without
risking a system crash.


Earlier I said that it is possible to fill up a file system with empty files.
Let's try this now. After creating only 2,500 empty files the OS will report
that there is no space left on the storage device, while at the same time
reporting that we've only used a small percentage of its capacity.


Legend:
-------
* Prompts beginning with `$` are commands you run as an ordinary user
* Prompts beginning with `#` are commands you must run as root

0.  Create an empty file named `disk.ext4` that's not too big, nor too small.
    64MB is *just* right for this demo.  We're drawiwng bytes from /dev/zero,
    so this file starts out being completely zeroed out.

        $ dd if=/dev/zero of=disk.ext4 bs=64M count=1

1.  Create a file system in the file `disk.ext4`.  In other words, perform a
    *high-level format* on `disk.ext4`.  We'll use the ext4 general-purpose
    file system because it's the most common on Linux these days and is
    supported by your kernel.

        $ /sbin/mkfs.ext4 disk.ext4

2.  Create a directory onto which to mount the file system stored within
    `disk.ext4`.  Note the directory permissions of this directory:

        $ mkdir mini
        $ ls -ld mini

    If you were to create some files in the mini directory now, you will
    observe that they are inaccessible after the file system in the file
    `disk.ext4` is mounted there:

        $ echo 'Keep it secret; keep it safe.' > mini/secret.txt

    This is a technique that hackers have been known to employ in order to hide
    malicious files.

3.  Mount the file system contained within disk.ext4 onto that directory.
    Notice what the permissions become on that directory once it's mounted:

        $ sudo mount disk.ext4 mini
        $ ls -ld mini

    It is at this point that `secret.txt` is no longer accessible under the
    `mini/` directory.

4.  Enter our new file system by changing into the mini/ directory, and look around.

        $ cd mini
        $ ls -l

    *Note* The directory called `lost+found` was created by `mkfs.ext4`. It is
    where recovered files are placed in the event of a system crash.

    The `df` command reports the amount of "disk free".  The `du` command reports "disk used".

        $ df .
        $ df -i .
        $ du .

    The 1st command displays how much storage capacity our 64MB "disk" has, and
    how much is taken up by the formatting itself.

    The 2nd form of the `df` command counts inodes.

5.  Become root and run a command which will fill up the disk with empty files.

        $ sudo -s
        # for A in {a..z}; do for B in {a..z}; do echo ${A}${B}_; for C in {a..z}; do touch $A$B$C; done; done; done
        # ls | wc -l
        # du -s
        # df .
        # df -i .

6.  While you cannot create any new files (or directories, for that matter),
    you may write data into a file which already exists:

        # dd if=/dev/zero bs=1024 count=800 of=aaa


7.  This miniature filesystem is a safe space to try to unzip a
    [zip bomb](https://www.bamsoftware.com/hacks/zipbomb/) like `42.zip` or
    `5.5GBzipbomb.zip`.  Seriously, be careful where you unzip these files,
    `5.5GBzipbomb.zip` is the smallest zip bomb available on bamsoftware.com,
    and it will cause serious trouble for the unwary application

        # rm -rf *
        # unzip 5.5GBzipbomb.zip


8.  Exit this filesystem on this pseudo-device, unmount it and clean up after yourself:

        # exit
        $ cd ..
        $ sudo umount mini
        $ rm disk.ext4

9.  Observe that our secret file is still there, safe and sound

        $ cat mini/secret.txt


# Building and installing the Linux Kernel on your Raspberry Pi

[Instructions for building the Linux kernel on RPi](https://www.raspberrypi.org/documentation/linux/kernel/building.md)

Look at the files in the `/boot` directory

* The `.dtb` files seem to be built by the code you clone from https://github.com/raspberrypi/linux
* There are two `kernel*.img` files; for our RPi3 we use `kernel7.img`


Local Build notes:

0.  Backup all files under `/boot`:

        $ sudo cp -R /boot /boot.bak

1.  Install the `git`, `bison`, `flex`, `libncurses-dev`, `libssl-dev` and `bc`
    packages

        $ sudo apt update
        $ sudo apt install -y git bison flex libncurses-dev libssl-dev bc

    *Note: you likely already have `git` installed*


2.  Clone only the most recent commit from the source tree on GitHub.  You
    don't need all of the commits, and beginning from the most recent one saves
    a *lot* of time

        $ git clone --depth=1 https://github.com/raspberrypi/linux ~/rpi-linux.git

    This step took me ~4 minutes on my RPi

3.  Enter the repository and set up the source code

        $ cd ~/rpi-linux.git
        $ export KERNEL=kernel7
        $ make bcm2709_defconfig

    This step took me ~16 seconds

4.  At this point I copied the Linux logo originally taken from Linus Torvald's
    git repository into this one so you can tell the difference at boot time
    (the default Raspberry Pi kernel uses their own logo at boot time instead
    of Tux the Linux penguin).

        $ cp ~/logo_linux_clut224.ppm ~/rpi-linux.git/drivers/video/logo

    I might also go into the kernel config and change the system's hostname

        $ make menuconfig
          General Setup -> Local version - append to kernel release
          "-bob-the-unixcorn-v7"

5.  `$ make -j4 zImage modules dtbs`

    This step takes almost 2 hours!

6.  Install any kernel modules that were built in the previous step to obtain
    functionality that's not part of the kernel itself:

        $ sudo make modules_install

    This step takes just a minute or two (forgot to check the time)

7.  Copy `.dtb` files and overlays into `/boot`

        $ sudo cp arch/arm/boot/dts/*.dtb /boot/
        $ sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
        $ sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
        $ sudo cp arch/arm/boot/zImage /boot/kernel7.img

8.  Look at the current kernel version

        $ uname -r

9.  Reboot

10. Check the kernel version again to verify that it's different from before

        $ uname -r
