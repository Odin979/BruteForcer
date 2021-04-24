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
To conduct a brute force attack on a garage door opener, you need to know few things. These things are the nature of the attack, bit shif register, frequency, baud rate, and how many bits the transmitter is using. 

### Nature of the Attack
Brute force attacks involve trying every possible passphrase until getting the correct one. To explain it clearly, let’s assume that we have a password with two characters, and each character is either 1 or 0. To count the possible combinations, we need to calculate 2 to the 2nd power, which is four possible combinations. These combinations are 00, 01, 10,11. So, to brute force a 2-bit password, we will try these four combinations. In garage door openers, these characters are called bits, and they can be either 1 or 0. Almost all garage door openers are using 8-bit to 12-bit code. By applying the same formula above, we can conclude that the number of possible combinations is from 256 to 4096. So, the attack I will be conducting will involve writing a Python code that can go through all the possible combinations in less than 3 minutes. All the signals will be transmitted using a USB dongle called YARD Stick One, which is a sub-1 GHz transmitter. 

### Bit Shift Register
Most garage door receivers use something called a bit shift register, which works by taking a bit array and shifting it by one position to compare it with the correct password (“Shift register,” 2018). To explain this even more, assume we have a 5-bit code, and it is 01101. If we send an 8-bit code that is 11011011, the receiver will not throw it away as an incorrect code. However, it will analyze it using the shift register technique. This is how it will analyze it:
* **11011**011 – Incorrect *nothing will happen*
* 1**10110**11 - Incorrect *nothing will happen*
* 11**01101**1 – Correct *the door will open*
* 110**11011** - Incorrect *nothing will happen*

So, it doesn’t really matter how many bits you send unless it contains the correct code within it. Also, the hacker doesn’t need to know how many bits a garage door opener is using. They can just send a 12-bit code, and it will open all garages that use 8, 9, 10, 11, and 12-bit. This system is vulnerable to so many types of attacks, yet it is still used in many households worldwide.  

### Knowing the Frequency
<img align="right" src="https://user-images.githubusercontent.com/78453901/115947862-8f3c2580-a498-11eb-8306-d425690fa1bf.jpg">
First, knowing the frequency used by the remote. If you have access to the remote or the receiver you want to attack, you can look at the label in the back of the device. What we are looking for is an FCC ID. 
Using this website: https://fccid.io/ you can type the FCC ID in the search area, and it will get you the frequency for that device. However, guessing the frequency isn’t that hard. Almost all garage door transmitter uses a range from 300 MHz – 390 MHz. That doesn’t mean you will have to try all the 90 MHz in between. Actually, there are only a few frequencies that you can guess in order to get the right one. According to the Garage Door Guide website, the most common frequencies are 300 MHz, 310 MHz, 315 MHz, 318 MHz, and 390 MHz (“Program garage door remotes,” 2019). So, it is only five frequencies that you can try in order to open any garage. !

### Knowing the Baud Rate.
<img align="right" src="https://user-images.githubusercontent.com/78453901/115948004-8009a780-a499-11eb-83c3-cdf02758e53f.png">
Baud rate is how long each pulse in a signal. For example, a 10-bit code has 10 pulses, and the baud rate is represented by how long each pulse lasts. If we assumed that the baud rate is 4800, that means it takes 1/4800 second for every bit. The following figure is a screenshot I took comparing two similar signals with different baud rates. The two baud rates are 2400 and 4800. You can clearly see that the pulse length in the 2400 signal is double the length of the 4800 signal. Getting the correct baud rate is extremely important for the garage to open. Receivers listen first to how long the pulse is. If it is too short or too long, the receiver will stop listening to that signal. However, you don’t need to capture a garage remote’s signal to determine the baud rate. Almost all garage door remotes are using either 1200, 2400, or 4800. So, trying these three configurations would get the door open no doubt. 

### Knowing How Many Bits
This part is going to be the easiest. As I explained earlier, garage door receivers use a bit shift register. That’s means if the garage you want to open is 8-bit, sending a 12-bit code would still open it. Since all garage openers containing DIP switches range from 8-bit to 12-bit, sending a 12-bit code would open every 8, 9, 10, 11, and 12-bit garage door. Note that every time the bits increase, the time for running all possible codes increases to. However, it is not that long to go through all the possible codes. A 12-bit code has two possible values for each bit, either 1 or 0. So, the total possible combinations are 2^12, which is 4096 possible combinations. Since we will be sending each code four times to ensure the receiver will capture it, that means the total codes we are sending is 16,384. If we send all these codes with a baud rate of 2400, it takes approximately 4.5 minutes. The time would decrease even more every time the baud rate increase. 

## Conducting the Brute Force Attack
