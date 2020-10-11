CS3100 - Module 1 - Lecture 05 - Fri Sep 06

# Call on 2 designated questioners


# Topics:
* Mud Card review
* Assignment #1 Overview
* Build Systems
* Java Build Systems Shootout


----------------------------------------------------------------------------
# Mud Card review

There were a lot of remarks regarding the Human-Computer Interaction
implications of an Iron Man style UI; with respect to both the immersive,
holographic display and the Jarvis/F.R.I.D.A.Y. AI assistant.

Y'all are a bunch of nerds.

Some choice remarks:

> Command line interface would probably include instructing and conversing.  It
> is generally difficult to explore a command line interface unless they have
> really good feedback or a --help menu.

A new category of UI based upon body gestures:

> Something for interacting with objects in a 3D projected reality.  Iron Man
> interface style, or the gloves that replace keyboards. Perhaps that still
> fits in "manipulating", but I feel it's a big difference going from the mouse
> to using my own body movements. I also think having a headset/goggles/glasses
> is different than when it's projected in front of you.

> I feel like every operating system needs to allow all four categories.  It
> would be a bad OS if you couldn't communicate or manipulate data.  There's
> always some help function or file structure to explore, and of course, the
> computer has to converse.


----------------------------------------------------------------------------
# Assignment #1 Overview

https://usu.instructure.com/courses/547959/assignments/2699282



----------------------------------------------------------------------------
# Build Systems

Real-world software systems are too large for a single person to develop alone,
much less comprehend or even build.  A typical end-user application consists of
millions of lines of code written in many different languages.

For example, as of last night the source code for the LibreOffice.org office
software consists of 14,601 files written in as many as 16 different languages,
totalling over 4.5 million lines of code.

	SLOCCount, Copyright (C) 2001-2004 David A. Wheeler
    ===================================================

	Totals grouped by language (dominant language first):
	cpp:      4,116,554 (90.27%)
	java:       276,446 (6.06%)
	python:      61,443 (1.35%)
	C:           36,805 (0.81%)
	perl:        32,075 (0.70%)
	sh:          12,550 (0.28%)
	yacc:        10,832 (0.24%)
	cs:           6,600 (0.14%)
	objc:         1,948 (0.04%)
	lex:          1,880 (0.04%)
	awk:            978 (0.02%)
	pascal:         940 (0.02%)
	asm:            866 (0.02%)
	php:             79 (0.00%)
	csh:             20 (0.00%)
	sed:              5 (0.00%)

	Total Physical Source Lines of Code (SLOC)                = 4,560,021
	Development Effort Estimate, Person-Years (Person-Months) = 1,389.78 (16,677.33)
	 (Basic COCOMO model, Person-Months = 2.4 * (KSLOC**1.05))
	Schedule Estimate, Years (Months)                         = 8.38 (100.54)
	 (Basic COCOMO model, Months = 2.5 * (person-months**0.38))
	Estimated Average Number of Developers (Effort/Schedule)  = 165.87
	Total Estimated Cost to Develop                           = $ 187,739,998
	 (average salary = $56,286/year, overhead = 2.40).


### Questions to consider with your study buddies

* Do these files make up a single executable, or a suite of related programs?
* How do you begin compiling all of these files?
* Once you've compiled them, how do you link them together?
* How long do you think it takes to compile all of these files?
* What happens if there is a build failure along the way?
* What if there is a bug in one out of the 14,601 files?  When you fix it, must
  you start from the top and rebuild everything?


Build systems are software which automate task of building software.  As
software systems grew larger and larger the task of assembling the finished
product became more and more difficult.  More automation was needed to make
this process faster, easier, and to reliably deliver a consistent output.
Increasingly sophisticated tools have evolved to meet these needs.

The evolution of these tools might be explained in this progression:

1.  Compiler commands manually entered
2.  Shell scripts collecting compiler commands into one, repeatable program
    -   Build scripts
3.  Declarative domain-specific programming languages for orchestrating the selective execution of build scripts
    -   Unix make
    -   GNU make
4.  Declarative domain-specific programming languages to simplify the creation of build scripts
    -   GNU Autotools
    -   CMake

*   [https://en.wikipedia.org/wiki/Build_automation](https://en.wikipedia.org/wiki/Build_automation)
*   [https://en.wikipedia.org/wiki/Software_build](https://en.wikipedia.org/wiki/Software_build)


Let's build a small C++ project by hand as a way of illustrating why automation
is desirable.

[Build tool demo for C++](buildsys/)


----------------------------------------------------------------------------
# Java Build Systems Shootout

There are three dominant build systems in the Java ecosystem:

* Ant
* Maven
* Gradle

In this class we use Gradle.  I hope that this demonstration illustrates why
Gradle is superior to the other options.

[Java Build Tools Comparision](https://technologyconversations.com/2014/06/18/build-tools/)

    $ git clone https://github.com/vfarcic/JavaBuildTools
    $ cd JavaBuildTools

Ant is controlled by the files `build.xml` and `ivy.xml`

    # build with Ant -> build/jar/java-build-tools.jar
    $ ant jar


Maven is controlled by `pom.xml`.  It must also connect to a "repository" on
the internet to function.  I'm not entirely sure what happens when the network
goes down...

    # build with Maven -> target/java-build-tools-1.0.jar
    $ mvn package


Gradle is controlled with the file `build.gradle`.  It also starts and leaves
running a background process to facilitate future builds.

    # build with Gradle -> build/libs/JavaBuildTools-1.0.jar
    $ gradle tasks jar


*Note: if the Gradle build fails, edit `build.gradle` and remove the 'task
wrapper' block at line 17*


## [Gradle Wiki](https://usu.instructure.com/courses/547959/pages/gradle-wiki)

