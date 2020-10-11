# Threading implementation demo

This directory contains the same program written in a few different programming
languages.  Each program spawns the following threads:

*   1 main thread which starts up the worker threads, then waits for them to
    finish (they won't...)
*   6 CPU-bound worker threads which increment `a` in a forever loop
*   1 I/O-bound worker thread which copies data from a slow disk device

By running the programs and watching the CPU graph in `htop` you will notice a
difference between each implementation.


| Language | Program          | Threading implementation
|----------|------------------|-------------------------
| C++      | `threads.cpp`    | Kernel threads
| Scheme   | `threads.scm`    | User/Green threads
| Python2  | `threads_py.py`  | Hybrid (I/O can be done in parallel, CPU work is serial)
| Python3  | `threads_py.py`  | Hybrid - idem.
| Cython3  | `threads_py.py`  | Hybrid - idem.
| Java     | `threads.java`   | Kernel threads


## Threading and Python

Doing parallel processing in Python is a bit tricky, due to an implementation
detail.  Python has a Global Interpreter Lock (GIL) which allows only one
thread to be active in the interpreter at once.  This means that threads cannot
be used for parallel execution of Python code.  While parallel CPU computation
is not possible, parallel IO operations are possible using threads.  This is
because performing IO operations releases the GIL.

Many attempts have been made at removing Python's GIL, but so far none have
been successful.

* [Multiprocessing and multithreading in Python3](https://www.ploggingdev.com/2017/01/multiprocessing-and-multithreading-in-python-3/)
* [Inside the Python GIL](https://youtube.com/watch?v=ph374fJqFPE)
* [Understanding the Python GIL](https://youtube.com/watch?v=Obt-vMVdM8s)
* [Python Concurrency From the Ground Up](https://youtube.com/watch?v=MCs5OvhV9S4)
* [How Did Python Become A Data Science Powerhouse?](https://youtube.com/watch?v=9by46AAqz70)
* [The Gilectomy How's It Going PyCon 2017](https://youtube.com/watch?v=pLqv11ScGsQ)
* [Writing faster Python](https://youtube.com/watch?v=YjHsOrOOSuI)

