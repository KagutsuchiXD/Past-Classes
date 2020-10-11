# Python Text Tools

This is a complete suite of Unix text tools implemented in simple Python:

1. cat   - combine many files into one.  Also prints out file contents

    python tt.py cat words
    python tt.py cat file0 file1 file2

2. head  - display only the top of a file.  10 lines is the default, this may
   be overridden with the -n argument

    python tt.py head words
    python tt.py head -n 20 words

3. tail  - display only the end of a file. 10 lines is the default, this may be
   overridden with the -n argument

    python tt.py tail words
    python tt.py tail -n 20 words

4. wc    - report the number of lines, words, and characters in a file

    pyhton tt.py wc 2017.annual.singlefile.csv

5. grep  - search for lines in a file containing a pattern, printing only those
   lines.

    python tt.py grep "Cache County" area_titles.csv
    python tt.py grep "New Jersey" area_titles.csv

6. cut   - Given a delimiter and a list of numbers, split lines of a file on
   the delimiter and print out those fields corresponding to the given numbers.
   By default the delimiter is Tab ("\t"), and only the first field is printed.

    python tt.py cut -d, -f1,8,9 2017.annual.singlefile.csv


## Now that I have this program, how do I use it?

Make a smaller data set by taking just the top 3000 lines from the original
file.  Instead of printing the results to the screen, we'll use the `>` symbol
on the command line to redirect the output into a file named `smaller.csv`:

    python tt.py head -n 3000 2017.annual.singlefile.csv > smaller.csv


Make a CSV dataset containing only Cache County data.  First, we need to find
the FIPS area code for Cache County:

    python tt.py grep "Cache County" area_titles.csv
    "49005","Cache County, Utah"

Next, we want to find all of the lines in the huge CSV file which use a FIPS
code of 49005.  We don't want our tool to find other lines which just happen to
contain the digits 49005, so we'll ask our program to look for 49005 surrounded
by double-quotes:

    python tt.py grep '"49005"' 2017.annual.singlefile.csv > cache_data.dat

The above command didn't find the special header line that ought to come first
in any CSV file.  We should include the CSV header line at the top of our Cache
County data to create a valid CSV file.  Let's grab it off the top of the huge
CSV file and put it into a file of its own called `headerline.csv`:

    python tt.py head -n 1 2017.annual.singlefile.csv > headerline.csv

Finally, let's use our concatenation tool `cat` to combine these two files into
one whole CSV file:

    python tt.py cat headerline.csv cache_data.csv > cache.csv


## What can I do with a smaller dataset?

This is just the beginning of what you might do with your new text processing
tools.

* You could use a spreadsheet to examine your crafted dataset.

* Double-check that your program's output matches the sums computed in the  spreadsheet.

* Replace the real-world values with numbers that are easier for you to verify
  manually.

