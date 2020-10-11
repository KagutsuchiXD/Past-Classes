Operating System Semaphore
==========================
This program implements processes which use a "System V Semaphore".  Through a
sequence of system calls two or more processes vie for control of a critical
section of code guarded by a semaphore.  When a process has the "key" it may
proceed.  If the key is not available, the process will block until another
process releases its key.

Watch as the processes trip over each other as they both access the shared
piece of data simultaneously.


Running this demo
-----------------
1. Run `make` to build the program
2. Open two terminals and navigate into this directory
3. In one terminal run `./main` and press ENTER to acquire the key and enter
   the critical section
4. In another terminal run `./main` and press ENTER to attempt to acquire the key
5. Return to the first terminal press ENTER to release the key, observing what
   happens in the other process



System V IPC information
------------------------
The following system commands may be run from the command line to provide
visibility into the System V IPC system.

* `lsipc`: Show information on IPC facilities currently employed in the system
* `ipcs`:  Show detailed information about message queues, shared memory
  segments and semaphores that have been created in the system

IPC resources can be created and removed with these commands:

* `ipcmk`: Make various IPC resources
* `ipcrm`: Remove various IPC resources
