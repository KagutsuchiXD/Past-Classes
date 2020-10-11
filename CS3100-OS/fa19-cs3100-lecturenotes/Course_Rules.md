# Course Rules _(how to succeed in my classroom)_


## Table of Contents

* Your GitLab account
* Assignment Submissions
* Examinations
* Behavior and Professional Conduct
* Be The Designated Questioner (5% of your final grade)
* In-Class Learning Activities and Online Discussions (5% of your final grade)



--------------------------------------------------------------------------------
## Your GitLab account

Unless otherwise stated all assignments will be submitted to the course GitLab
server [GitLab](https://gitlab.cs.usu.edu).  Use the email address supplied by
the school to register for an account.


### Do not push your work to public repositories

To prevent academic dishonesty, submissions made to public repositories are
unacceptable and will receive zero points.  It would please me for you to use
your course work as part of your online portfolio, but you must wait until the
semester has concluded to publicize your work.


### Asking for help

The instructor and TA get many requests for help every week.  If you take a few
small steps to respect our time you will be rewarded with better, faster
responses.

When seeking help with assignments, commit your broken code along with a
README.md file explaining your problem.  Push it to GitLab and send an email
briefly explaining your question with the GitLab URL included.  We will respond
as soon as we can, but be aware that we may not be able to quickly respond to
messages sent late at night or on weekends.



--------------------------------------------------------------------------------
## Assignment Submissions

* It is *your* responsibility to be aware of due dates for each assignment.
* You are expected to manage your time wisely so that you can keep up.
* It is *your* responsibility to correctly submit your work before the due date.
* Some assignments build upon previous submissions.  It is on *you* to keep up.
* It is *your* job to convince the grader your submission is complete and
  correct.


### When to Submit (penalty of up to 100% of a submission's grade)

* All assignments are due by 11:59 PM of the due date.
* Git commits timestamped *after* the due date are considered late.
* Git commits timestamped *before* the due date but pushed to the GitLab server
  *after* the due date are considered late.


| Lateness  |            Penalty           |
|-----------|------------------------------|
|< 24 hours | 25% of total points possible |
|< 48 hours | 50% of total points possible |
|>= 48 hours| 100% of total points possible|


*   No assignment is accepted after 48 hours.
    **Do not email me, do not ask, it is not accepted.**
*   Do not expect the TAs or the instructor to be available for last-minute
    questions and assistance.  A lack of planning on your part does not
    constitute an emergency on our part.  In other words, don't expect a timely
    reply to an email sent after 10 PM in the evening or on weekends.
*   If you are planning on being out of town when an assignment is due, be sure
    to get your homework assignment done before you leave or make arrangements
    to work on the road.

Exceptions to the above can only be made in the event of a  *serious,
unexpected* emergency.  Inform the instructor as soon as you can (in advance,
if possible) to work out an arrangement.


#### Grading Gift

Each student is allowed one late submission (up to 48 hours) without penalty
and without question.

*   The gift is automatically used on the first assignment you submit late; you
    do not have to ask for it.
*   The assignment must have been submitted within the acceptable late time
    frame (48 hours in this course).
*   The gift covers late submissions only.  You cannot ask to use it when your
    code is incomplete or incorrect.
*   _The **Grading Gift** may not be used on the final assignment._

Do not use the gift early in the semester just because you feel a little lazy
and want to turn one in a late without penalty.  Later in the semester you may
have a legitimate problem arise and you will have wasted this opportunity to
recover from an honest mistake without consequence.

If you "accidentally" make a late submission, the grading gift is nevertheless
consumed.  Any mistakes in later submissions that you might have corrected
within the 48 hour grace period will result in a penalty appropriate to the
error.


### How To Submit Assignments

* Unless otherwise specified, assignments will be committed to a git repository
  and pushed to the course GitLab server instead of being turned in on Canvas.
* You must push your work to the course GitLab server before the due date to be
  considered on-time.  The timestamps of individual commits are not considered.
* Submissions must be made to private repositories.  Public repositories are
  unacceptable and receive no credit.
* Submissions to other git services (i.e. GitHub, Bitbucket) are *not*
  accepted.

The name of your git repository must follow this pattern:

`Course-LastName-FirstName-Assn#`

Examples:

*   `cs3100-smith-jane-assn1`
*   `cs3100-jones-bill-assn5`

Name your submission with *LastName* and *FirstName* corresponding to your
"Full Name" in Canvas to help us correlate your repository in GitLab with your
assignment on Canvas.

*Failure to follow this format will result in a 10 point penalty*


#### Your submission _MUST_ contain:

1.  Source code files which may be organized into subdirectories as needed.
2.  A file named `.gitignore` used to exclude files and directories from a git
    repository.  On Linux and Mac this file may be hidden from file listings.
    The contents of a `.gitignore` file are explained in more detail below.


#### Your submission _MAY_ contain:

1.  A text file called `README.md` in the top-level directory.  When I provide
    starter code for an assignment it will likely already contain a file named
    `README.md`.  This file is *not* read-only, and you *should* modify its
    contents.  You will put into this file any special instructions or
    explanations for the grader.  Cite any external sources used in the
    creation of your submission (e.g. Stack Overflow, Wikipedia, etc.).  
2.  A directory called `data` if extra data files are used by your program.
3.  A directory named `doc` where you may place any extra supporting
    information for the grader.
4.  Any other subdirectories needed to organize your work as you see fit.


#### Your submission _MUST NOT_ contain:

1.  Directories containing pre-compiled files or other generated files created
    by your IDE or build tools (e.g. `build`, `*.class`, etc.).  An exception
    to this is the `.idea/` subdirectory and an `*.iml` created by the IntelliJ
    IDE.
2.  Zip files, backup files, screenshots or other detritus left behind from
    your experimentations.
3.  Extremely large files.  What is considered "extremely large" depends upon
    the project, but a good rule of thumb is to avoid committing files larger
    than 20 megabytes.

*Inclusion of forbidden files and directories will result in a 10 point penalty*


##### Block unwanted files from your repository with .gitignore

The `.gitignore` file helps you avoid committing unwanted files and directories
to your repository.  `.gitignore` is a simple, plain text file, each line of
which specifies a filename pattern that git will ignore.

The following `.gitignore` file is suitable for assignments in this course:

```
.DS_Store
build
gradle
gradlew
gradlew.bat
.gradle
*.class
*.jar
*.zip
*.bak
```

You may edit this file but be careful to not accidentally allow unwanted files
in to your repository.  Only the names of files are considered; git cannot
ignore files based upon a file's size or its contents.

Be aware that most Windows tools do not allow you to create a new file
beginning a `.`; other tools will automatically add an extension to its name
such as `.txt`, which prevents git from using this file.  The most convenient
way to create these files on Windows is from the Git Bash command line.

*Failure to include a comprehensive .gitignore file will result in a 10 point
penalty, even if no forbidden files or directories are present in your repository.*


### Example structure of a good assignment submission:

```
    cs3100-jamieson-phil-assn2
    |-- .gitignore
    |-- README.md
    |-- Instructions.md
    |-- Assign2.iml
    |-- build.gradle
    `-- src
        |-- Assign2.java
        |-- cpu.java
        |-- dirs.java
        |-- java.java
        |-- mem.java
        `-- os.java

```


### Verifying Your Submission

You are graded on what you submit, not on what you meant to submit.  It is
*solely* your responsibility to ensure that your submission is complete and
correct.  Plan to leave yourself time to double-check your work before you
submit.


#### Reference Implementation

The graders will use Oracle's distribution of the Java SE 12.0.2 or later from
oracle.com as the reference implementation for grading assignments. It is up to
you to either:

* Install Java SE 12.0.2 or later on your own computer

or

* Find a computer with the correct version of Java

Computers in the Engineering Computer lab have the correct version of Java installed.


#### Errors and warnings

* Code which does not run due to errors may, at most, receive half credit
* Warnings are penalized at 5 points per warning
* If your code makes same warning appear many times, each instance costs 5 points



--------------------------------------------------------------------------------
## Examinations

*   There will be two exams this semester; a midterm exam and a final exam
*   Examinations must be taken in the Testing Center
*   The exams are already registered with the testing center and are available
    for you to schedule

The lecture on the Monday of an exam week will be a review.  The midterm exams
may be taken any time between Tuesday and Thursday of that week.  On Friday we
will discuss the results of the exam.  After this discussion it is too late to
make up an exam as the answers will be common knowledge.

You should schedule your time slot for each exam as soon as possible, and add a
reminder to your calendar so that you don't forget to take it.  Again, once the
exam review occurs on the Friday following the exam it cannot be re-taken.

The last lecture before finals week is the review for the Final Examination.



--------------------------------------------------------------------------------
## Ethical Behavior

*   You are expected to conduct yourself in a manner conducive to the
    educational goals of this institution.
*   Assignments must be your own original creation.  While you may do some of
    your work in groups, you may not submit the same work as anyone else.  The
    guideline is to do high-level design work in a group and write your code in
    isolation.  Do not show your code to your friends, even if they promise not
    to copy it, because both of you will receive an Academic Integrity
    Violation when I discover it.
*   It is not out-of-bounds to seek advice and inspiration from online
    resources such as Stack Overflow and Wikipedia; that's how a lot of
    real-world coding happens.  When you borrow ideas from online sources, you
    must cite them in a `README.md` file in your repository.
*   Exams are to be completed without the aid of notes or web resources, unless
    the test contains a statement to the contrary.
*   I will remove disruptive influences from my classroom.
*   Electronic devices may be used in class so long as I do not deem their
    presence to be disruptive.  Do not bother to come to class if you are just
    going to watch movies or play games.



--------------------------------------------------------------------------------
## Be The Designated Questioner (5% of your final grade)

Every student in my course gets their own day to ask a question.

An important part of your training as a software engineer is to develop a habit
of critical thinking.  The best engineers and programmers I worked with have
one thing in common: they were driven to understand *why*.  In each lecture I
call upon students to be the "designated questioners" (DQ) for that day.  When
you are called upon it is your responsibility to ask a *good* question during
that lecture.


### Bad Questions

These examples are not suitable for a DQ's question:

1.  _"When is the exam?"_

2.  _"Will this be on the test?"_

3.  _"How many points will I lose if I turn this in a day late?"_

4.  _"What day did we talk about DOM events?"_


### Good Questions

A good question is one that

* Gets at the *why* of the topic at hand
* Sparks a thoughtful discussion
* Is not trivially answerable by looking on Canvas, the syllabus or the lecture
  notes

In order to think critically and earn your DQ points, do the following:

1.  Restate what you _do_ understand.

    _"As I see it, the DOM is a tree-like data structure similar to the file
    system on my computer. Is that correct?"_

2.  Explain what you _don't_ know.  Putting your misunderstandings into words
    is an effective way to organize your thoughts and to identify gaps in your
    knowledge.
    
    _"I don't get what you mean by 'dispatching control to the view function'.
    Could you please explain this in a different way?"_

3.  Ask a counterfactual question.  When you are called upon to be the DQ but
    don't feel that you need clarification, ask a question that attacks the
    underlying assumptions behind the subject at hand.
    
    _"What would be the difference if we did that computation on the server
    instead of in the browser?"_

    _"Why did you do it that way?  What would happen if you did it the other way?"_


### Opting out

If you have a legitimate reason to not be a DQ, you may contact discreetly me
to work out an alternative arrangement.



--------------------------------------------------------------------------------
## In-Class Learning Activities and Online Discussions (5% of your final grade)

*Regular lecture attendance is correlated with high academic performance* 

Frequently throughout the semester you will participate in in-class learning
activities such as mud-cards, group discussions and assignment retrospectives
to

* Check your understanding
* Reinforce the material by taking a different approach
* Gather feedback on the effectiveness of my instruction

These events are graded for participation rather than performance.  Unless
otherwise stated these activities are worth 5 points each.  You may earn *up to
a maximum of 50 points* over the course of the semester.  This Canvas gradebook
item begins with 0 points and fills up toward 50 points as the semester
progresses.  Be aware that, due to the way Canvas calculates your letter grade,
you will see your grade drop when you get your first points in this category.

I understand that many of you need to miss class in service of other worthy
demands.  This policy does not demand that you attend 100% of my lectures.  You
may miss a few lectures and still receive full points in this category.  That
said, frequent absentees should not expect excellent results.

This policy extends to online discussions hosted on Piazza.  Asking good
questions and giving good answers in a Piazza discussion thread will be
rewarded.  Students participating in online discussions must obey the following
guidelines:

- The greatest benefit from assignments comes when you work out your own
  solution.  Do not post full or partial solutions.
- If you have a complex programming question, design and post a simplified
  version of your problem.
- Discussion forums are not to be used for gossip, inappropriate or hurtful
  messages.  Don't write anything you will regret later.
- Don't expect instant responses on the forums.  We're not on the same schedule
  as you.
