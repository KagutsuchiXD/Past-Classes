# How to connect to your RPi remotely

If you don't want to lug a TV and an extra mouse & keyboard around with you,
you can opt to leave your RPi at home and access it remotely over the internet.

## SSH connection

This is how I prefer to connect to my RPi.  The first step is to enable the SSH
service.  There are many ways to configure your Raspberry Pi. I'll show you how
to use the `raspi-config` program:

    $ sudo raspi-config

Enable the SSH server to run from bootup.  This will make your Raspberry Pi
available even without a mouse and keyboard, provided you know its IP address
or its domain name.

While you're in this program you should also change the default password for
the 'pi' user account.  If you don't bad people will be able to access your
Raspberry Pi the moment it goes online (and there are bad people scanning for
these all of the time).

You can discover your RPi's IP address with this command:

    $ ip addr


You may also try

    $ hostname -I


If your RPi is connected via WiFi, use the IP address listed on an interface
called `wlan0`.  If you have a wired Ethernet connection, the IP address is
associated with the `eth0` interface.

Now, if your RPi is connected to your Router at your home, this is the IP
address you give your SSH program on your laptop to connect to the RPi.  When
you connect and enter your username and password, you'll be put into a Bash
shell.

This IP address, however, won't be meaningful outside of your home network.  If
you want to connect to your RPi when you're away from home, you'll need to do a
little extra work.

1.  First, find your Router's IP address.  You can use your web browser to ask
    [DuckDuckGo](https://duckduckgo.com/?q=what+is+my+ip+address).  This is the
    IP address your RPi presents to the rest of the world.

2.  Set up "Port Forwarding" or "Virtual Server" on your router.  Read your
    router's instruction manual or help file to learn how to do this.  The idea
    is that you'll associate a port number on your router with port #22 on your
    Raspberry Pi: when a connection from outside your home comes to your
    router's port 22, the router will forward it to your RPi.

#### The SSH Port is 22



## VNC connection

You can also connect using a virtual desktop protocol.

From the desktop's Raspberry Menu ->
    Preferences ->
    Raspberry Pi Configuration ->
    -> Services

Enable VNC Server

You will need a VNCviewer application to connect to your RPi's desktop.  You'll
use your local IP address while in your own network.  If you want to use VNC to
connect to your RPi while you're out of the house, you'll need to set up "Port
Forwarding" in the same way as for SSH, but forward port #5900 instead.


#### The VNC Port is 5900

