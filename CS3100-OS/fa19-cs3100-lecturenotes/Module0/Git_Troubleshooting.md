# Git Troubleshooting Guide


## SSL certificate problem: unable to get local issuer certificate

Pushes to and clones from the GitLab server via an HTTPS-style URL are failing
with an error message mentioning an SSL certificate.

This is happening because the SSL library included with your installation of
Git does not trust the certificate authority which issued the certificate for
my GitLab server.  Most often it is students using Git+Bash for Windows, but
this could happen on other platforms as well.

The best work-around is to use the SSH interface instead of HTTPS.  This
involves creating an SSH key and changing the remote repository's URL over to
an SSH-style address with the `git remote set-url` command.  You will find a
Canvas page in Module 0 called "Creating and using an SSH Key with Git".  This
page contains a video that walks you through the process.

After you've imported your SSH key into GitLab, you will be given the option to
use an SSH-style URL.

1.  You will find this URL on your repository's GitLab page by clicking the
    blue "Clone" dropdown button at the upper-right of the page.

2.  Copy the URL listed in the "Clone with SSH" box

3.  In your command shell you will use another form of the `git remote` command
    to change the URL

    ```
    git remote set-url origin git@gitlab.cs.usu.edu:USERNAME/cs3100-LAST-FIRST-assn0
    ```

4.  Run `git push` to verify that git can talk to the remote GitLab server.



## usage: ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]

Pushes to and clones from the GitLab server via an SSH-style URL are failing
with this error message:

	$ git push -u origin master
	usage: ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
			   [-D [bind_address:]port] [-E log_file] [-e escape_char]
			   [-F configfile] [-I pkcs11] [-i identity_file]
			   [-L address] [-l login_name] [-m mac_spec]
			   [-O ctl_cmd] [-o option] [-p port]
			   [-Q cipher | cipher-auth | mac | kex | key]
			   [-R address] [-S ctl_path] [-W host:port]
			   [-w local_tun[:remote_tun]] [user@]hostname [command]
	fatal: Could not read from remote repository.

Most often it is students who installed and used Anaconda when taking a
previous course from me.  This is most common cause is an incorrect piece of
configuration in your global `.gitconfig` file.  To remove it, run this
command:

    git config --global --unset core.sshCommand

Afterward, re-try your `git push` or `git clone` command.


## *git push* says "No such file or directory" and *Anaconda3* appears in the error message

You're getting an error message that looks something like this:

    $ git push origin master

    C:\\Users\\Jarvis\\Anaconda3\\Library\\usr\\bin\\ssh -i C:\\Users\\Jarvis\\.ssh\\id_rsa -F C:\\Users\\Jarvis\\.ssh\\config: C:\Users\Jarvis\Anaconda3\Library\usr\bin\ssh: No such file or directory

    fatal: Could not read from remote repository.
    Please make sure you have the correct access rights and the repository exists.


This problem is essentially the same as the previous issue: git is still trying
to run Anaconda's `ssh` command but you have uninstalled Anaconda from your
computer.  The remedy is the same as for the previous problem:

    git config --global --unset core.sshCommand



## I've created an SSH key, but GitLab still asks for a password

GitLab won't ask for a password if it has a copy of the SSH public key that
matches a key on your local machine.

* Ensure that you have generated an SSH public key on your system.  Look for a
  subdirectory named `.ssh` under your home folder.  You should have a file
  with the `.pub` extension.

* Check that the contents of the public key file are correctly imported into
  your GitLab account.

* SSH prefers to use a public key called `id_rsa.pub` before one called
  `id_ed25519.pub`.  If you have both public keys on your local machine try
  importing the other one to GitLab.



## Git asks me for my username and password, but freezes when I enter the password

Git isn't frozen; your keystrokes are merely hidden from the screen to prevent
a passerby from reading your password.  Enter it as usual and press Enter.
