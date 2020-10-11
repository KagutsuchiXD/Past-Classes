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

