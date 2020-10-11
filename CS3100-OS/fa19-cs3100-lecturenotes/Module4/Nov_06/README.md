CS3100 - Module 4 - Lecture 29 - Wed Nov 06

# Announcements

## FSLC Linux Cool Tools

Tonight we are discussing your favorite Linux tools that make using your
computer a breeze.  Is there a program that is your best-kept secret?
Sharing is caring!

So come on down to ESLC 053 at 6pm to share your favorite cool tools!


## Assignment 4 is due today

If you are participating in the Utah State Science Week Coding Challenge on
HackerRank.com.  This contest runs from Nov 4 2019, 12:00 pm MST to Nov 8 2019,
01:00 pm MST.

You can't just sign up and get two free days; you have to demonstrate that you
are spending enough time on the coding challenge to detract from this
assignment.

To qualify for the extension, send me an email with your HackerRank username.
I'll be checking the leader board to make sure my generosity isn't being
abused.



# Topics:
* Introduce Assignment 5
* DLL demo & memory regions


----------------------------------------------------------------------------
# Introduce [Assignment 5](https://usu.instructure.com/courses/547959/assignments/2699286)


# DLL demo & memory regions

[../../Module4/Nov_04/dll/](../../Module4/Nov_04/dll/)


Watch the memory regions as the shared libraries are loaded/unloaded on your
RPi with this command:

    $ watch -d -n 1 cat /proc/$(pgrep main)/maps

