# Used for reading files and checking whether they're directories.
import os
import os.path

# Import file read permission masks from stat
from stat import S_IREAD, S_IRGRP, S_IROTH

# Used for checking file names for pattern matches
import fnmatch

# Helper function for sorting directory names in chronological order
import time
def month_day(fname):
    return time.strptime(os.path.split(os.path.dirname(fname))[-1], '%b_%d')


# Searches the given directory recursively for files matching 'notes.*'
# and returns an aggregate list of all found files.
def searchRecursiveForNotes(d, notes='README.md'):
    # Get a list of all files/folders in the directory
    notesFound = []
    children = os.listdir(d)
    for child in children:
        path = os.path.join(d, child)
        if (os.path.isdir(path)):
            notesFound.extend(searchRecursiveForNotes(path))
        elif fnmatch.fnmatch(path, "*/Module?/[ADFJMNOS][aceopu][bcglnprtvy]_[0-3][0-9]/" + notes):
            notesFound.append(os.path.relpath(path))
    return sorted(notesFound, key=month_day)


# Find all files matching 'notes.*' in the current directory
# and all its children directories.
allNotes = searchRecursiveForNotes('.');

# The name of the file to save to.
# To be treated as a constant.
SAVE_FILE = 'all_notes.md'

# Delete all_notes.md if it exists
try:
    os.remove(SAVE_FILE)
except OSError:
    # Otherwise do nothing
    pass

# Make a string with a 2^6 ='s, the fun Python way.
separator = ('=' * 2**6) + '\n'
count = 1

# Open all_notes.md and call the stream fstream
with open(SAVE_FILE, 'w') as fstream:
    for note in allNotes:
        print("Concatenating lecture #%d %s" % (count, note))

        # Write a little header block before each appended file
        fstream.writelines([
                ('\n\nLecture %d: %s\n' % (count, note)),
                separator, '\n'
                ])

        with open(note, 'r') as noteFile:
            fstream.writelines([line for line in noteFile])

        count += 1


# Set all_notes.md as read-only, because this script deletes the file every time
# it's run. all_notes.md is a bad place to put personal notes.
os.chmod(SAVE_FILE, S_IREAD|S_IRGRP|S_IROTH)

print("\nConcatenated notes saved to %s" % SAVE_FILE)
print("This file is marked read-only because running the concatenate script "
    + "again will\ndelete it. Keep your personal notes elsewhere, "
    + "or rename the file.")
