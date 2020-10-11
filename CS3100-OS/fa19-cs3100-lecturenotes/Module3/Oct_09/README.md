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



