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

