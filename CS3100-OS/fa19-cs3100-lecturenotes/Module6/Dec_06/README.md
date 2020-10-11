CS3100 - Module 6 - Lecture 39 - Fri Dec 06

# Announcements

## Cyberdefence club meeting

*   ENGR 101 - Thursday Dec 12 @ 5:00pm

*   Come learn about Cyberdefense competitions and learn how to prepare to
    enter one.

*   We will be doing a retrospective of the Cyberforce competition, including:
    -   Discussion of why we got hacked and all the places we could have prevented it
    -   A live demo of how we got hacked
    -   A lab on command injection
    -   Gauge interest in forming official teams for future competitions

*   We plan to hit the ground running, so come prepared to put SSH and other
    basic command line skills to use!


## [DC435](https://dc435.org): January Meeting Metasploit 101 by Santiago
*   7pm Thursday, Jan 2nd
*   Bridgerland Technical College @ 1301 N 600 W - Room 840

Metasploit is the most commonly used tool in pentests.
Come and learn what Metasploit is and how to use it


# Final Exam Review

*   35 questions in total - 157 points
*   Covers subjects presented since the midterm exam, Chapters 6-10
*   Available in the Testing Center over the entirety of Finals Week

How to prepare for my exams:

1.  Attend this review lecture
2.  Study the Mastery Quizzes on Canvas



# Chapter 6

* What is the dispatcher, and what responsibilities does it have?

* What is preemptive scheduling
    +   There are 4 circumstances under which CPU-scheduling decisions may take place
    +   Under two of them the scheduler has no decision to make (non-preempive)
    +   For the other two, the scheduler can choose to act (preemptive)

* What is starvation?
    +   Which types of schedulers are susceptible to starvation?

* What is the Convoy Effect?
    +   Which types of schedulers are susceptible to the convoy effect?

* What characteristics does Round-Robin Scheduling have?
    +   What is a "time slice" (a.k.a. "time quantum")?
    +   What is the effect of increasing or decreasing the duration of the time slice?

* What is "processor affinity"?
    +   What's the difference between hard and soft affinity?


# Chapter 7

* What are the conditions necessary for deadlock to occur?
    +   How many of these conditions must be removed to avoid deadlock?

* How do modern OSes deal with deadlock (or not)?

* Be able to read a Resource Allocation Graph (RAG) and identify whether a
  system is in deadlock
    +   What things are represented on a RAG (what do the arrows, boxes and
        circles represent?)

* What is a "safe state", and what does it mean to be in one?

* What is the "Banker's Algorithm", and how does it help prevent deadlock from
  occurring?


# Chapter 8

* At what times can memory addresses be bound to a process?
    +   If dynamic linking is employed, how late can a code library be linked
        in to an executable?

* Understand the difference between physical and logical memory
    +   Virtual memory == logical memory
    +   Does the size of a system's virtual memory need to equal its physical
        memory capacity?

* What are pages and frames?
    +   Which one refers to physical memory, and which refers to logical
        memory?

* What is the page table?

* What is the Translation Look-aside Buffer?

* What does it mean for memory to be fragmented?
    +   What is the difference between external and internal fragmentation?

* What is swapping?
    +   What is thrashing?


# Chapter 9

* What problem do page replacement schemes solve?
    +   Can the Optimal page replacement scheme actually be implemented?
    +   Which page replacement scheme exhibits Belady's anomaly?

* Given a read out of a system's CPU%, paging and I/O utilization, what
  measures would you suggest to improve performance?

* What is demand paging and how does it work?
    +   What is pure demand paging?

* What does it mean to *memory map* a file?
    +   What is the difference between memory mapping a file in *shared* mode
        versus *private* mode.

* What is Copy-on-Write, and when is it employed?


# Chapter 10

* What is "seek time" and "rotational latency"?
    +   Do these delays apply to solid state drives?

* What is "constant linear velocity" and "constant angular velocity" 
    +   How do these affect storage density of the disk?

* What problems does RAID solve?
    +   What benefit does mirroring by itself provide?
    +   What benefit does data striping by itself provide?
    +   What benefit does an error correcting code by itself provide?
