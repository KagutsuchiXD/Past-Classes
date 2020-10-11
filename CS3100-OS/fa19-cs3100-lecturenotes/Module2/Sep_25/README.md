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

