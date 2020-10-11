# How to use Git to submit homework

## Create an SSH key and load it on GitLab

*   You can avoid the tedious entry of username and password by creating an [SSH key](https://usu.instructure.com/courses/547959/pages/creating-and-using-an-ssh-key-with-git) and importing it into your GitLab profile.  
*   Completing this step now will prevent potential issues with SSL certificates later.  If you see an error about an SSL certificate, follow the instructions in the [Git Troubleshooting Guide](Git_Troubleshooting.md)


## On your computer

0.  **[Windows Users Only]**
    Install and configure [Git for Windows](https://usu.instructure.com/courses/547959/pages/required-software-installation-instructions)

1.  Launch a command shell and use the  `git config` command to set up your name and email address.  Git needs to know who you are so that when you make commits it can record who was responsible.
    ```
    git config --global user.name  "Danny Boy"
    git config --global user.email "danny.boy@houseofpain.com"
    ```

2.  Ensure that you're not presently within a git repository by running the
    command ```git status```

    *Protip:* You *don't* want to create a git repository within a git
    repository.  *Always* run `git status` before using any command which
    creates a new git repository to ensure that you are not already within a
    git repository.  You want to see `git status` present an error message in
    this situation as it will confirm that you are *not* already inside a git
    repository.

    ```
    $ git status
    fatal: not a git repository (or any parent up to mount point /)
    Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set)
    ```

3.  Initialize a new git repository (the *local* repo) with the `git init`
    command.  I'll be boring and name my repo cs3100-falor-erik-assn0.  The
    repo's name on your own computer isn't terribly important, so long as you
    can keep things straight.

    ```
    git init cs3100-falor-erik-assn0
    ```

    *Protip:* Always provide a name for your repo to `git init`.  If you forget
    to provide a name here, git makes the current directory into a git repo!


4.  Enter the new directory
    ```
    cd cs3100-falor-erik-assn0
    ```

5.  Open an editor and create a new file in this directory. You might call it
    "README.md" and say something nice to your grader (hey, you never know...)


6.  Return to your command shell ask git about the status of your little repository
    ```
    git status
    ```


7.  Use `git add` to add the file `README.md` to your repository.
    ```
    git add README.md
    ```

8.  Get the status of your repository again; it should tell you that you have changes
    ready to be committed
    ```
    git status
    ```

9. You're ready to permanently commit to these changes.  Use the `-m` option to add a brief message (between double quotes) about this change.
    ```
    git commit -m "Created the README.md file"
    ```

10. Get the status of your repository once more; the directory should be "clean".
    ```
    git status
    ```


11. Review the commit history of your repository
    ```
    git log
    ```



## On the GitLab website

Now you're ready to put your code out on the web.  You will make a new, empty
repository under your account into which you will send the code from your
computer to this empty location on GitLab.

0.  Log in to your GitLab account

1.  Click on the white `+` button in the blue bar at the top of the page

2.  Choose **New Project**

3.  Give your repository a name that follows the course guidelines:
    `cs3100-falor-erik-assn0` is appropriate here

    *Protip:* _Do not_  add a `README.md` file from the web interface; this will only mess things up for you.

4.  Click "Create Repository"

5.  Scroll down to the bottom of the resulting page and find the section titled
    "Push an existing Git repository".  Run the commands listed there in your
    command window.   They should look something like this:

    ```
    git remote rename origin old-origin
    git remote add origin git@gitlab.cs.usu.edu:USERNAME/cs3100-LAST-FIRST-assn0.git
    git push -u origin --all
    git push -u origin --tags
    ```

6.  Refresh your browser window.  Instead of seeing **The repository for this
    project is empty**, you should see your README.md file.


You are now ready to hack on your code.


## I'm having some troubles with Git

See the [Git Troubleshooting Guide](Git_Troubleshooting.md) for solutions to the most common problems.
