# conda_fix.py

### Enable passwordless authentication to online Git Services from within Anaconda

To keep things simple, I have written a Python program which will perform all
of the necessary steps to upgrade your Anaconda command-line environment for
this to work. You will need to use git to get a copy of my program. After my
program upgrades your Anaconda enviroment it will pop open a notepad window
containing your own SSH key. You will need to log into Bitbucket and submit the
SSH key into your Bitbucket settings page (this is a different page than the
per-repository settings page; be sure that you are in the right place when you
set this up!)

1.  Open the Anaconda Command Line

1. Download this code from Bitbucket with git
   ```git clone https://bitbucket.org/erikfalor/conda_fix.git```

1. Move into the new conda_fix directory created by the previous command:
   ```cd conda_fix```

1. Run the conda_fix.py Python program:
   ```python conda_fix.py```

1. When Notepad opens up, follow the instructions printed at the bottom of the
   command window to install your SSH key on Bitbucket.
