CS3100 - Module 6 - Lecture 38 - Wed Dec 04

# Announcements

## The Testing Center is booked up - here's what you need to do

The testing center is now completely booked. However, they will not turn
anybody away and you will be able to take your exam. It will just take some
planning on your part.

The testing center takes walk in appointments on a first-come, first-served
basis. Due to the increasing popularity of the testing center, you should
expect to wait between 30-60 minutes to get a seat. Because scheduled
appointments start at the top and bottom of the hour, you may find your wait
time is reduced if you arrive at the quarter hours. Walk-ins have less of a
wait earlier in the week.


## DC435 Meeting Tomorrow night

Intro to appsec by llamapope

Space will be open at 6:30 and meeting will kick off at 7:00pm.

We currently meet at Bridgerland Technical College campus located at 1301 N 600 W, Logan, UT 84321 - Room 840



# Call on 2 designated questioners


# Topics:

----------------------------------------------------------------------------
# File Types

Some operating systems encode information about a file's purpose and what
applications may use it into the file metadata.  Some OSes encode this info
into the filename.  Some OSes leave determining file type up to each
application.  Unix is this sort of OS.


## Do you believe in magic?

    https://asecuritysite.com/forensics/magic

The beginning bytes of many types of files include a "magic number" which
identifies a file to an application.  You can view a file's magic number by
running it through a hexdump program such as `xxd`:

    xxd FILENAME | head


[demo: sample files of various kinds](magic/)

Ever wonder why MS-DOS/Windows executables all begin with 'MZ'? Shouldn't that
be 'M$' or at least 'MS'?
    https://en.wikibooks.org/wiki/X86_Disassembly/Windows_Executable_Files#MS-DOS_header


You don't need to learn all of the magic numbers by heart.  On Unix systems the
`file` program scans files for their magic numbers and reports their type and
purpose.

You can find out information about that random archive which was attached in
that email from the Nigerian Prince before you extract it:

    $ file r.zip
    r.zip: Zip archive data, at least v2.0 to extract

    $ file r.tar.gz
    r.tar.gz: gzip compressed data, from FAT filesystem (MS-DOS, OS/2, NT)

Incidentally, these archives contain perfect copies of themselves:
Archiveception. You can unzip these files forever, but watch out when you get
to the part with the skiing henchmen with machine guns (or was it the skiing
scene with the abominable snowman? I can never keep my skiing scenes straight).

    $ while unzip r.zip; do cd r; pwd; done

    $ while tar xf r.tar.gz; do cd r; pwd; done



# File-System Mounting

You will have noticed that Unix dispenses with the awkward convention of "disk
drives" being root file systems in their own right. Every file system in Unix
is attched to the same file tree, including file systems which aren't of the
same device, including file systems which aren't *real* in the sense that they
are in no way related to mass-storage devices. The end result is a single,
unified namespace for all entities which may be accessed under the file system

When a new file system is brought online in a Unix system it is grafted onto the
root file system. This process is called *mounting a file system*.

#### Mount
Attach a file system contained in a separate volume onto the extant
heirarchical tree of files and directories

The location which the new volume's file system is attached is called a *mount
point*.

#### Mount Point
A directory onto which a file system is attached to the main tree

Ordinarily, the directory which is designated to be a mount point for another
file system is left empty. This is because any files and subdirectories
contained within the mountpoint become inaccessible while the file system is
mounted there. In other words, once the new file system is mounted, the names
of files contained within the mountpoint refer to files on the new volume, and
not the old one.

On Unix we use the `mount` command to associate a volume with a directory and
attach the files and directories contained within the volume into the main file
system.


*You may also view a listing of mounted file systems by running `mount` with no arguments*


The `umount` command is used to unmount a file system (notice that the
command's name is missing an 'n'). In order for the unmount operation to be
successful, all files in the target volume must be closed. This includes
directories, which are held open by processes using them as their CWD.


# Stupid Raspberry Pi Tricks: create a file system within a file ... in your file system

One of the nice things about Linux is that there are many commands available
which enable you to manipulate file systems. Combined with the flexibility that
Unix's orthogonal design brings, we can perform experiments safely without
risking a system crash.


Earlier I said that it is possible to fill up a file system with empty files.
Let's try this now. After creating only 2,500 empty files the OS will report
that there is no space left on the storage device, while at the same time
reporting that we've only used a small percentage of its capacity.


Legend:
-------
* Prompts beginning with `$` are commands you run as an ordinary user
* Prompts beginning with `#` are commands you must run as root

0.  Create an empty file named `disk.ext4` that's not too big, nor too small.
    64MB is *just* right for this demo.  We're drawiwng bytes from /dev/zero,
    so this file starts out being completely zeroed out.

        $ dd if=/dev/zero of=disk.ext4 bs=64M count=1

1.  Create a file system in the file `disk.ext4`.  In other words, perform a
    *high-level format* on `disk.ext4`.  We'll use the ext4 general-purpose
    file system because it's the most common on Linux these days and is
    supported by your kernel.

        $ /sbin/mkfs.ext4 disk.ext4

2.  Create a directory onto which to mount the file system stored within
    `disk.ext4`.  Note the directory permissions of this directory:

        $ mkdir mini
        $ ls -ld mini

    If you were to create some files in the mini directory now, you will
    observe that they are inaccessible after the file system in the file
    `disk.ext4` is mounted there:

        $ echo 'Keep it secret; keep it safe.' > mini/secret.txt

    This is a technique that hackers have been known to employ in order to hide
    malicious files.

3.  Mount the file system contained within disk.ext4 onto that directory.
    Notice what the permissions become on that directory once it's mounted:

        $ sudo mount disk.ext4 mini
        $ ls -ld mini

    It is at this point that `secret.txt` is no longer accessible under the
    `mini/` directory.

4.  Enter our new file system by changing into the mini/ directory, and look around.

        $ cd mini
        $ ls -l

    *Note* The directory called `lost+found` was created by `mkfs.ext4`. It is
    where recovered files are placed in the event of a system crash.

    The `df` command reports the amount of "disk free".  The `du` command reports "disk used".

        $ df .
        $ df -i .
        $ du .

    The 1st command displays how much storage capacity our 64MB "disk" has, and
    how much is taken up by the formatting itself.

    The 2nd form of the `df` command counts inodes.

5.  Become root and run a command which will fill up the disk with empty files.

        $ sudo -s
        # for A in {a..z}; do for B in {a..z}; do echo ${A}${B}_; for C in {a..z}; do touch $A$B$C; done; done; done
        # ls | wc -l
        # du -s
        # df .
        # df -i .

6.  While you cannot create any new files (or directories, for that matter),
    you may write data into a file which already exists:

        # dd if=/dev/zero bs=1024 count=800 of=aaa


7.  This miniature filesystem is a safe space to try to unzip a
    [zip bomb](https://www.bamsoftware.com/hacks/zipbomb/) like `42.zip` or
    `5.5GBzipbomb.zip`.  Seriously, be careful where you unzip these files,
    `5.5GBzipbomb.zip` is the smallest zip bomb available on bamsoftware.com,
    and it will cause serious trouble for the unwary application

        # rm -rf *
        # unzip 5.5GBzipbomb.zip


8.  Exit this filesystem on this pseudo-device, unmount it and clean up after yourself:

        # exit
        $ cd ..
        $ sudo umount mini
        $ rm disk.ext4

9.  Observe that our secret file is still there, safe and sound

        $ cat mini/secret.txt


# Building and installing the Linux Kernel on your Raspberry Pi

[Instructions for building the Linux kernel on RPi](https://www.raspberrypi.org/documentation/linux/kernel/building.md)

Look at the files in the `/boot` directory

* The `.dtb` files seem to be built by the code you clone from https://github.com/raspberrypi/linux
* There are two `kernel*.img` files; for our RPi3 we use `kernel7.img`


Local Build notes:

0.  Backup all files under `/boot`:

        $ sudo cp -R /boot /boot.bak

1.  Install the `git`, `bison`, `flex`, `libncurses-dev`, `libssl-dev` and `bc`
    packages

        $ sudo apt update
        $ sudo apt install -y git bison flex libncurses-dev libssl-dev bc

    *Note: you likely already have `git` installed*


2.  Clone only the most recent commit from the source tree on GitHub.  You
    don't need all of the commits, and beginning from the most recent one saves
    a *lot* of time

        $ git clone --depth=1 https://github.com/raspberrypi/linux ~/rpi-linux.git

    This step took me ~4 minutes on my RPi

3.  Enter the repository and set up the source code

        $ cd ~/rpi-linux.git
        $ export KERNEL=kernel7
        $ make bcm2709_defconfig

    This step took me ~16 seconds

4.  At this point I copied the Linux logo originally taken from Linus Torvald's
    git repository into this one so you can tell the difference at boot time
    (the default Raspberry Pi kernel uses their own logo at boot time instead
    of Tux the Linux penguin).

        $ cp ~/logo_linux_clut224.ppm ~/rpi-linux.git/drivers/video/logo

    I might also go into the kernel config and change the system's hostname

        $ make menuconfig
          General Setup -> Local version - append to kernel release
          "-bob-the-unixcorn-v7"

5.  `$ make -j4 zImage modules dtbs`

    This step takes almost 2 hours!

6.  Install any kernel modules that were built in the previous step to obtain
    functionality that's not part of the kernel itself:

        $ sudo make modules_install

    This step takes just a minute or two (forgot to check the time)

7.  Copy `.dtb` files and overlays into `/boot`

        $ sudo cp arch/arm/boot/dts/*.dtb /boot/
        $ sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
        $ sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
        $ sudo cp arch/arm/boot/zImage /boot/kernel7.img

8.  Look at the current kernel version

        $ uname -r

9.  Reboot

10. Check the kernel version again to verify that it's different from before

        $ uname -r
