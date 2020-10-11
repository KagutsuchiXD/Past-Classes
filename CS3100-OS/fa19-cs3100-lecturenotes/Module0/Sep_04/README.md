CS3100 - Module 0 - Lecture 04 - Wed Sep 04

# Announcements

## Free software and Linux Club
*   Opening meeting tonight - 6pm @ ESLC 053
*   Get acquainted with Linux and Open Source Software


## [DC435](https://dc435.org): DefCon 2019 lessons learned
*   7pm Thursday, Sept 5th
*   Bridgerland Technical College @ 1301 N 600 W - Room 840

DC435 is our local chapter of the DefCon computer security conference scene.
It is a friendly place to dip your toes into the world of cybersecurity.

DC435 meets at 7:00pm every First Thursday of every month.



# Call on 2 designated questioners

# Topics:
* Interfacing with the Operating System via the command line
* Linux command line guide
* Using command line arguments in your code


----------------------------------------------------------------------------
# Interfacing with the Operating System via the command line

There are many ways to interact with a computer.  Human Computer Interaction
(HCI) researchers recognize four [1]:

<details>
<summary>1. Instructing</summary>

Telling the computer what to do through shortcut keys, buttons, typing strings
of characters. Quick and prompt feedback.

</details>


<details>
<summary>2. Conversing</summary>

Holding a back-and-forth dialog with a computer
* Wizards
* Pop-up dialog boxes
* Context-sensitive menu systems
* Prompts

</details>


<details>
<summary>3. Manipulating</summary>

Leverage users' knowledge of the "real-world" through analogs to familiar
concepts:

* Desktop
* Icons
* Files
* Folders
* Trash bin
* Point-and-click
* Drag-and-drop

Characterized by continuous representation of the interface (the desktop is
always present), use of direct physical actions as opposed to abstract textual
instructions.

</details>

<details>
<summary>4. Exploring</summary>

Moving through virtual or physical environments.

* Virtual reality
* Augmented reality
* "It's a UNIX system, I know this!"

</details>

[1] Interaction Design: Beyond Human-Computer Interaction (4e). Preece, Rogers,
Sharp; Wiley, 2015. pp 47-54


## Discuss with your study buddies:

* What categories do you think a Command Line Interface (CLI) fall into?
* What categories do you think a Graphical User Interface (GUI) fall into?
* Into which categories would you place a voice-activated assistant?
* How about an Augmented Reality (AR) interface?
* These four categories don't have to be the end-all-be-all of ways humans may
  interact with computers.
  * What other categories might you propose?
  * How would your scheme re-arrange things?




----------------------------------------------------------------------------
# [Unix command line guide](../Unix_CLI.md)


----------------------------------------------------------------------------
# Using command line arguments in your code

Let's write a simple Java class called `Args` that inspects its own
command-line arguments which are passed in as an array of String objects to the
`main()` method.

This program can be built using this command (remember that the '$' represents
your shell's prompt):

    $ javac Args.java

And may be run with zero arguments:

	$ java Args 


Or many arguments:

	$ java Args 1 2 3 4 5


Special arguments called *switches* or *options* may be given which instruct
the program to perform special actions.  

	$ java Args -add 1 2 3 4 5

	$ java Args -mul 1 2 3 4 5


The meaning of a switch is entirely up to each program.  Different programs can
interpret a switch like `-r` in totally different ways.
