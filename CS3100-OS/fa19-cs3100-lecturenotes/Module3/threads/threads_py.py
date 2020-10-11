#!/usr/bin/python3

# You get really different results when this runs under Python2 vs. Python3
# Python 2.7.16
# Python 3.7.4


from __future__ import print_function
import threading, sys


# Global variable for referring to our "slow" I/O device
device = "/dev/sda"
BUFSIZ = 8192


# A function which increments the variable 'a' forever
def maths():
    a = 0;
    while True:
        a += 1


# A function which copies 8k from our slow I/O device to /dev/null
def slowio(dev):
    print("\n\nWasting time with a cutting-edge I/O-Bound algorithm on the slow data source", dev, ",\n", BUFSIZ, "bytes at a time.")
    
    while True:
        try:
            slow = open(dev, "rb")
            bytez = slow.read(BUFSIZ)
            slow.close()
            
            null = open("/dev/null", "wb")
            null.write(bytez)
            null.close()
        except:
            print("Failed to open", dev)


if (len(sys.argv) > 1):
    device = sys.argv[1]

# Create 6 thread objects running the the 'maths' function
tmaths = []
for i in range(6):
    tmaths.append(threading.Thread(target=maths, name='maths' + str(i)))
    tmaths[i].start()
    print("Spawned maths thread #" + str(i))

# Create a thread object running the 'slowio' function
tio = threading.Thread(target=slowio, name='slowio', args=(device,)).start()
print("Spawned Slow/IO thread on device ", device)

print("Press Ctrl-C or Ctrl-\\ to quit")

for i, t in enumerate(tmaths):
    t.join()
    print("Joined maths thread #" + str(i))
tio.join()
print("Joined Slow I/O thread")
