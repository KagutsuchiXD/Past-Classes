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

