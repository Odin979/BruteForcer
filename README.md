# BruteForcer

BruteForcer is a program that uses rfpwnon.py which is writing by ExploitAgency. The two rfpwnon codes have been slightly modified to make them combatible with Python3 and to include the features included in the BruteForcer tool. 
## Features
* Uses Graphical User Interface (GUI).
* Can brute force all frequencies and baud rates with one click of a button. 
  * Frequincies supported: 300MHz, 310MH, 315MHz, 318MHz, and 390MHz.
  * Baud Rates supported: 1200, 2400, and 4800 

## Requirements
* Hardware
  * YARD Stick One 
  * Antenna
* Software (Will be listed in the Toturial)
  * RfCat
  * SDCC-libraries

## Tutorial
In this installation, I would assume you have a freshly installed Kali or Ubuntu. So, I would go through every necessary package that needs to be installed. If your operating system has some packages installed, it’s no harm to install them again just to make sure everything is working properly.
Note that all the following commands are run as a superuser. To run commands as superuser, write the following command in the terminal, ``` sudo su ``` ten write your password.
### Requirements Before Installing Rfcat.
```
# curl
$ apt-get install curl

# git
$ sudo apt install git

# Development tools
$ apt install build-essential

# libusb-1.0-0
$ sudo apt-get install libusb-1.0-0

# pip3
$ sudo apt install python3-pip

# PySide2
$ pip install PySide2

# pyusb
$ pip install pyusb

# python3 packages
$ sudo apt install -y python3-pip python3-usb
```
