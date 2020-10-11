# Unix command line basics


## Jargon

#### Terminal or Console

An interactive program which displays and reads textual information to and from a user.


#### Shell

A text-based user interface which accepts commands from a user 

A shell runs within the context of a terminal; the terminal reads the keyboard
and sends the users's text to the shell.  The shell's output is displayed on
the terminal's grid of characters.

shell : terminal :: webpage : browser


#### Directory

A.K.A. "folder"; a location to store files and other directories


#### Current working directory

The directory your shell program is currently running in.

Commands that use files and directories will look in the current directory first.


#### Argument

Extra information given to a program in the form of a string from the command line.

Arguments may refer to objects on a computer system such as the names of files,
directories, user names, or host names.

While arguments may appear as integers, floating-point numbers, or other
structures, they are always passed by the OS to a program as an array of
strings.  It is the responsibility of the program accepting the arguments to
convert these strings into other data types as necessary.


#### Option (also: Switch, Flag)

A command-line argument used to modify a program's behavior.

In some programs the mere presence or absence of a command line option is
enough to change the program's behavior.  These are often referred to as
"boolean options" or "flags", though the former term has long since been abused
into being a synonym for "option".

Some options must themselves be followed by further arguments in order to be
meaningful.



## Basic Unix commands


**TASK**                         |  **COMMAND**
---------------------------------|-------------------------------------------
Print arguments to screen        |  `echo ARG0 ARG1...`
List files                       |  `ls` 
Print file to screen             |  `cat FILE0 FILE1...`
Create a new, empty file         |  `touch FILE0 FILE1...`
Delete a file                    |  `rm FILE0 FILE1...`
Change Directory                 |  `cd DIR`
Clear the screen                 |  `clear`
Print Working Dir (where am I?)  |  `pwd`
Make a new directory             |  `mkdir DIR`
Remove an empty directory        |  `rmdir DIR` (only works on empty dirs)
View the manual for a command    |  `man COMMAND`



## Changing directories

Use the `cd` command to change your working directory.  In the examples below
the '$' represents your prompt.  You don't type the '$', but rather the text
that follows.

Go up one level to leave the directory you are presently in

    $ cd ..


You can use the tilde '~' character as shorthand for your home directory.

Return to your home directory regardless of your current location

    $ cd ~

Go back to a directory under your home named 'workspace':

    $ cd ~/workspace

On Linux & Mac you can return to your home directory by running `cd` without
any arguments.

    $ cd



## Creating a .gitignore file on Windows

Windows's File Explorer tries to prevent you from creating a file whose name is
only an extension; that is, file names beginning with `.` are not encouraged on
this OS.  However, some programs which follow the Unix tradition (e.g. git)
require special files with names begining with `.`.  Bypass Windows's File
Explorer and use the Unix command-line tool `touch` to create such files.  Once
created, you can open them in a Windows program like any other file.

    $ touch .gitignore


Files whose names begin with `.` are ordinarily hidden from Unix programs such
as `ls`.  You can give `ls` the `-a` flag to enable it to display *ALL* files,
even hidden ones.
    
    $ ls -a
    .git/  .gitignore  Assign1.class  Assign1.java  README.md



## A word on "standard" command-line arguments

Options can be preceded by zero, one or two hyphens.  Options for commands for
`cmd.exe` on Windows are even preceded by a front slash `/`.  There are many
standards governing the *right* way to present command-line arguments.  They
are all equally invalid.

![XKCD: Standards](standards.png)



### Common command-line options

Nevertheless, there are some options which mean the same thing to many
different programs.  Check the documentation before trusting this list;
before you leap

*   `--help` or `-h`
    Print a usage message
*   `--verbose` or `-v`
    Produce more output than usual
*   `--version`, `-version`, sometimes `-V`
    Report the version number of the program
