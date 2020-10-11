# Fa19 CS3100 Lecture Notes Repository

These notes are an important means of communication from me to you.  You are
accountable for the information contained in these notes and are expected to
clone this repository to your computer to have instant access to this resource.

In addition to serving as a study guide throughout the semester, I will post
code written in class along with example programs and other important resources
to this repository.



## Creating a comprehensive study guide from individual lecture notes files

`concatenate.py` is a Python program written by Michael Hoffmann which
concatenates (joins) all lecture notes found in these directories into a
single, comprehensive file.  You may use this single file to easily find a
topic when you don't remember on which day it was covered or to create a study
guide for an exam.  Only lecture notes files are included; extra files such as
code, images and media are not included.

This program creates a read-only file called `all_notes.md`.  This file is
marked read-only to remind you to not make any important changes as they would
be destroyed the next time you ran this program.



### Instructions:

1. Run `git pull` to get the latest, most up-to-date lecture notes
2. Open a command shell in which Python is available
3. Run `python concatenate.py`
4. The resulting file is named `all_notes.md`

`concatenate.py` works best with Python version 3, though it is
backwards-compatible with Python 2.
