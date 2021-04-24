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
### SDCC-libraries
```
# download sdcc-libraries package (version 3.5.0)
$ curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc-libraries_3.5.0+dfsg-2_all.deb -o sdcc-libraries_3.5.0+dfsg-2_all.deb

# download sdcc package (version 3.5.0)
$ curl -l -C- http://ftp.de.debian.org/debian/pool/main/s/sdcc/sdcc_3.5.0+dfsg-2+b1_amd64.deb -o sdcc_3.5.0+dfsg-2+b1_amd64.deb

# install sdcc-libraries
$ sudo dpkg -i sdcc-libraries_3.5.0+dfsg-2_all.deb

# install sdcc package
$ sudo dpkg -i sdcc_3.5.0+dfsg-2+b1_amd64.deb

# show version (optional) IT HAS TO BE 3.5.0
$ sdcc –version
```
### Installing RfCat
```
# clone repository
$ git clone https://github.com/atlas0fd00m/rfcat.git

# cd to rfcat
$ cd rfcat/

# install setup.py
$ sudo python3 setup.py install

# copy rules
$ sudo cp -v etc/udev/rules.d/20-rfcat.rules /etc/udev/rules.d

# refresh rules
$ sudo udevadm control --reload-rules

# cd to home directory
$ cd ~

# Test rfcat by showing the help menu
$ rfcat -h
```

## What Do You Need to Know Before Conducting the Brute Force Attack?
To conduct a brute force attack on a garage door opener, you need to know three things. These things are the frequency, baud rate, and how many bits the transmitter is using. 

### Knowing the Frequency
<img align="right" src="https://user-images.githubusercontent.com/78453901/115947862-8f3c2580-a498-11eb-8306-d425690fa1bf.jpg">
First, knowing the frequency used by the remote. If you have access to the remote or the receiver you want to attack, you can look at the label in the back of the device. What we are looking for is an FCC ID. 
Using this website: https://fccid.io/ you can type the FCC ID in the search area, and it will get you the frequency for that device. However, guessing the frequency isn’t that hard. Almost all garage door transmitter uses a range from 300 MHz – 390 MHz. That doesn’t mean you will have to try all the 90 MHz in between. Actually, there are only a few frequencies that you can guess in order to get the right one. According to the Garage Door Guide website, the most common frequencies are 300 MHz, 310 MHz, 315 MHz, 318 MHz, and 390 MHz (“Program garage door remotes,” 2019). So, it is only five frequencies that you can try in order to open any garage. !

### Knowing the Baud Rate.
<img align="right" src="https://user-images.githubusercontent.com/78453901/115948004-8009a780-a499-11eb-83c3-cdf02758e53f.png">
Baud rate is how long each pulse in a signal. For example, a 10-bit code has 10 pulses, and the baud rate is represented by how long each pulse lasts. If we assumed that the baud rate is 4800, that means it takes 1/4800 second for every bit. The following figure is a screenshot I took comparing two similar signals with different baud rates. The two baud rates are 2400 and 4800. You can clearly see that the pulse length in the 2400 signal is double the length of the 4800 signal. Getting the correct baud rate is extremely important for the garage to open. Receivers listen first to how long the pulse is. If it is too short or too long, the receiver will stop listening to that signal. However, you don’t need to capture a garage remote’s signal to determine the baud rate. Almost all garage door remotes are using either 1200, 2400, or 4800. So, trying these three configurations would get the door open no doubt. 

### Knowing How Many Bits
This part is going to be the easiest. As I explained earlier, garage door receivers use a bit shift register. That’s means if the garage you want to open is 8-bit, sending a 12-bit code would still open it. Since all garage openers containing DIP switches range from 8-bit to 12-bit, sending a 12-bit code would open every 8, 9, 10, 11, and 12-bit garage door. Note that every time the bits increase, the time for running all possible codes increases to. However, it is not that long to go through all the possible codes. A 12-bit code has two possible values for each bit, either 1 or 0. So, the total possible combinations are 2^12, which is 4096 possible combinations. Since we will be sending each code four times to ensure the receiver will capture it, that means the total codes we are sending is 16,384. If we send all these codes with a baud rate of 2400, it takes approximately 4.5 minutes. The time would decrease even more every time the baud rate increase. 

### Conducting the Brute Force Attack
