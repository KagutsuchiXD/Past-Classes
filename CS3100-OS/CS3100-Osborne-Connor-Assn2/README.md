a)Sulky Bravo

This menu item repeatedly alternates calling the system calls read() and write().
According to the system manual, read() reads x amount of bytes from a specified file descriptor and write() writes x amount of bytes to a specified file descriptor.
They are both reading and writing to to the same address but are using a different address for each sett of system calls.
I found this out by tracing the process using strace(). 
I believe this menu option is causing a context switch because it is about a 50/50 split between user and kernel mode.
I also believe this option to be I/O bound due to the low amount of CPU usage and the high amount of waiting for I/O.

b)Polisher Camera

This menu item repeatedly uses the clone() system call to make a new child process that is similar to the current process. It then makes the wait4() system call
that waits for the process to change states and then can return resource usage information. Then it uses the SIGCHLD signal to signal the parent process that
the child process has finished.
I found out what was happening by using strace() and then I looked up what each process does through the manual.
I believe this option is CPU bound due to the work being done on the CPU with no IO waiting.

c) Nervy RobeDeChambre

This menu option calls dup2(1,2) 1,000,000 times where dup2() replicates the new file descriptor 2. Then it prints to the terminal how many seconds it took to 
complete the task. This option also reports how long it took and how many times it called dup2() if you use ctrl^c before it reaches 1,000,000.
I found this information by using strace() and then looking up dup2() in the manual.
This process is CPU bound because all of the work done is through the CPU.

d)Clammy Refugium

This menu option repeatedly calls nanosleep() for 1 second at a time. 
The nanosleep() system call suspends the execution of the calling thread for a specified amount of time.
I found out what this option was doing by using strace().
I believe this option is CPU bound because nanosleep() is the only process being called and the CPU is the only resource being used.

e)Bulky Corpus

This menu option is repeatedly calling the kill() system call on the blackbox process id but because the signal it sends to the process is 0 it never actually
kills the process but still goes through all of the steps for it's system call.
I found out what this option does through strace() and the linux manual.
This is CPU bound because it doesn't utilize the IO and so doesn't depend on IO waiting.

f)Wry Triclinium

This option is repeatedly using the sigreturn() and kill() system calls and the SIGUSR2 signal. Sigreturn() allows for use of the signal handler 
and returns from the signal handler and cleans the stack frame. The kill() system call sends the SIGUSR2 signal to the process running blackbox.
The SIGUSR2 is a user defined signal which is why kill() doesn't kill the blackbox process.
I found this information using strace() and the linux manual.
This is CPU bound due to it only utilizing the CPU with no I/O waiting.

g)Retailer Snaggletooth

This menu option uses the getpid(), gettid(), tgkill(), and rt_sigprocmask() system calls and the SIGFPE signal.
First this option uses rt_sigprocmask() to check the list of blocked signals SIG_BLOCK. Then it uses getpid() to obtain the process id of the calling process blackbox.
Then it uses gettid() to get the thread id for blackbox. Then this option uses tgkill() to send SIGFPE to the thread id. It uses the SIGFPE return value to kill
the blackbox process.
I found this information using strace() and the manual.
This is CPU bound.

h)Gushy Boschbok

This option repeatedly uses the sync() system call. The sync() call is used to store cached data to a selected file system  but because this option isn't
giving any parameters to synch() it is just returning the value 0.
I used strace and htop to see what this option was doing.
This option is IO bound because it spends all of its time in I/O waiting mode.

i)Wiry Raphe 

The only system call that this option uses is write(). I can't tell what exactly it's doing but it does something 1,000,000 times in user mode and then
uses write() to output how long it took.
I used htop and strace to figure out what this menu option does.
This option is CPU bound as it was only running on the CPU mostly in user mode the entire time.

j)Rimy Auspex

This option uses the chmod() system call. chmod() changes the permissions of a specified file location. This menu option uses it to make itself readable, writable,
and executable to the owner, and only readable and executable to everyone else. 
I figuered this out using strace.
This option is CPU bound while running in user modae half the time and kernel made the other half.

k)Horny Cavefish

This menu option performs some sort of operation in usermode 1,000,000 times and then uses write() to output to the terminal how long it took 
and then uses write() again to output a newline.
I used strace to see that it was using two different write() system calls to output to the terminal this time.
I believe this option to be CPU bound as I did not see anything to suggest that I/O was being used.

l)Wary Lev

This option uses read() to read a certain amount of bytes from a /proc/${pid}/3. Then it uses the system call lseek() to reposition the file in the open file description.
The lseek() call is using SEEK_SET to change the file's offset to offset bytes. Then it uses write to /proc/${pid}/4.
I found this out using the manual and strace.
I believe that this is CPU bound due to he fact that in htop there are no grey lines indicating that the is I/O waiting.

m)Header Saguaro

This option is the memory leak that continues until the computer crashes or the process is killed. This option continually uses brk() to continually change
where the process' will end causing it to continue untile there was no memory left.
I used htop to realize that there was a memory leak and strace to see what system call was causing it.
I believe that this is CPU bound due to he fact that in htop there are no grey lines indicating that the is I/O waiting. 

n)Goosy Maremma

This option continuously uses the access() system call. This call is used to check if the process using it can access the specified file location.
This menu option uses access() to check if the file location /proc/self/exe exists. You can tell this because F_OK specifies that the specific call
is checking the file's existence.
I used the manual and strace to understand how this menu option works.
I believe that this is CPU bound because it used a high percentage of the CPU with no I/O info.

o)Customer Monsieur

This menu option repeatedly uses getcwd() to check the current working directory and returns the absolute path.
I used strace and htop to understand what this option was doing.
I believe that this option causes a context switch because there is an even split in the CPU for user and kernel modes. This program is also CPU bound
because there was only IO to print the message when killing the process with ctrl^c.
