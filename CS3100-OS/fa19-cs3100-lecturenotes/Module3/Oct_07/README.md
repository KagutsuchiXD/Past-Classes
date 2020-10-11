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


