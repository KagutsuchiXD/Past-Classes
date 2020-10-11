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

