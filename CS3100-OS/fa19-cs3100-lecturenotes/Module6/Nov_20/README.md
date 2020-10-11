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

