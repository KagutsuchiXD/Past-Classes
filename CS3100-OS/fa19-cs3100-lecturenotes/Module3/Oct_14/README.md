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
