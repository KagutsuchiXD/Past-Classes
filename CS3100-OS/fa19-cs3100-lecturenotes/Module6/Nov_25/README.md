CS3100 - Module 6 - Lecture 36 - Mon Nov 25

# Announcements

## Thanksgiving break starts Wednesday

* No class until next Monday, Dec 2nd.
* Enjoy your break!



# Call on 2 designated questioners


# Topics:
* Chapter 10: Mass-Storage Structure
    * 10.1.1 Magnetic Disks
    * 10.1.2 Solid-State Drives
    * 10.1.3 Magnetic Tapes
    * 10.2 Disk Structure
    * 10.3 Disk Attachment
    * 10.3.1 Host-Attached Storage
    * 10.3.2 Network-Attached Storage (NAS)
    * 10.3.3 Storage-Area Network (SAN)



----------------------------------------------------------------------------
# 10.1.1 Magnetic Disks

These devices provide the bulk of secondary storage on modern computers. Disk
systems are composed of multiple platters attached to a spindle. The disks all
spin together, and as they rotate a disk arm reaches over their surfaces,
reading 1's and 0's from the magnetic polarization of the regions that pass
beneath.

#### Platter
Flat, circular disk coated with a ferromagnetic substance

#### Head
Device which can sense and manipulate magnetic fields

#### Disk Arm
Holds the head and positions it over the surface of a platter

#### Tracks
Circular regions extending concentrically from the center of the platter

#### Cylinders
Set of tracks in all platters the same distance from the center


These disks may spin rather quickly, anywhere from ~5,000 RPM to ~15,000 RPM.
The faster the disk spins, the more rapidly data may be retrieved from it.

In order to read data from the disk we must wait for two things to occur:

#### Seek Time
The disk arm must be positioned to the correct track

#### Rotational Latency
The desired sector must rotate into position below the read head 

#### Random Access Time
The sum of the seek time and the rotational latency


The head doesn't actually touch the surface of the platter. It is suspended
just above the surface by the aerodynamic forces of the air moving above the
spinning disk.

#### Head Crash
When the read/write head contacts the surface of the disk

When a head crashes it scratches the magentic surface and obliterates the data
encoded therein. The only recourse is to have the drive mark the affected
regions unusable, or the drive must be replaced.


#### I/O Bus
the wires and data transfer protocol connecting the disk to the computer system

Common I/O busses you may have heard of include:
* IDE
* SATA
* SCSI
* USB
* Fibre Channel
* Firewire


# 10.1.2 Solid-State Drives

Nonvolatile RAM which is used as a secondary storage device. Broadly speaking
from a high-level perspective, they have many of the same characteristics as
traditional disk drives.

Pros:

* robust: no moving parts to wear out or break
* fast: no seek time for a disk arm, nor rotational latency
* energy efficient: no motors

Cons:

* cost: more expensive per GB
* shorter lifespan: limited number of read/write cycles per location

The SSD itself may be faster than the I/O bus it is connected to. Some SSDs
connect directly to the computer using the same bus which links the CPU to
other high-speed devices such as video cards or RAM.


# 10.1.3 Magnetic Tapes

Were always slower than magnetic disks, but have much larger capacities and far
lower costs. For this reason they are used for backup.

The reason a tape is slower than a disk is that random access requires spooling
the tape out to the desired position. Once the tape is in position read/write
speeds rivaling those of disks may be reached.

The closest many of you have come to a tape is with the Unix `tar` command.
`tar` stands for "Tape Archive", and was is designed to create archive files
suitable for backup to a tape device. If you read its man page you will find
some command-line arguments which make sense only for tape devices!


# 10.2 Disk Structure

As discussed before, disks transfer data by blocks of bytes instead of by
individual bytes. Most disks use a block size of 512 bytes.

#### Logical Block
The smallest unit of data a disk may transfer

Fun fact: Sector 0 of a magnetic disk drive is the 1st sector of the 1st track
on the outermost cylinder.

Each track on the disk is larger than the one that is closer to the center.
This leads to two possibilities:

1. Constant Linear Velocity (CLV) As we progress outward from the center each
   track encodes more data

   If the disk can slow its spinning as the read head moves outward, the head
   will observe that the speed of the disk beneath it is always the same.

   Tracks out from the center appear longer to the head, and contain more
   sectors. We can fit more data on the disk.

2. Constant Angular Velocity (CAV) Each track encodes the same amount of data
   regardless of its distance from the center
   
   In this scenario the rotational speed of the disk remains constant.

   Each track contains the same number of sectors, and each sector encodes the
   same number of bits. The sectors increase in size as we move away from the
   center. The density of bits per track decreases as we move away from the
   center. The head sees that the surface of the disk is moving faster when it
   is positioned over the outer tracks.



## 10.3.1 Host-Attached Storage

There are many options for how a disk may be connected to computer systems.

Connect disks directly to a single computer with a specialized disk I/O bus

Examples:
* SCSI
* IDE
* SATA



# 10.3.2 Network-Attached Storage (NAS)

Expose disks attached to a host using existing network infrastructure

Examples:
* Network File System (NFS) - used in Unix environments
* Server Message Block (SMB) - used on Wintendos
* Common Internet File System (CIFS) - a dialect of SMB

Because we're using an ordinary network, we can run into limitations of TCP
networking, and the NAS can impact the bandwidth of other users of the network.


# 10.3.3 Storage-Area Network (SAN)

Create a private, special-purpose network with specialized protocols optimized
for disk I/O.

Examples:
* Fibre Channel
* iSCSI
* InfiniBand


