# Control Structures in Python:

## Exercise 1:
In Lesson 1 Exercise 1, you wrote a program that calculated
and printed the area of a rectangle when given user input of length and
width.
In this exercise, you will add code to that program to check whether the
rectangle forms a square and output that as part of the print statement. 

### Examples:
```
Enter shape dimensions: (X Y)
4 4
Area of square: 16.0
```
```
Enter shape dimensions: (X Y)
5 7
Area of rectangle: 35.0
```
```
Enter shape dimensions: (X Y)
6 9
Area of rectangle: 54.0
```

## Exercise 2:
In Lesson 1 Exercise 2, you wrote a program named TemperatureConversion.py that
converted Celsius to Fahrenheit using the formula F = C * 9/5 + 32.
In this exercise, you write a program that asks the users for their unit of
measurement and converts the temperature either from Celsius to
Fahrenheit or Fahrenheit to Celsius depending on the user input. 

### Examples:
```
Convert from Celcius or Fahrenheit? (C/F)
C
Enter number to convert:
23
73.4
```
```
Convert from Celcius or Fahrenheit? (C/F)
F
Enter number to convert:
90
32.22222222222222
```
 
## Exercise 3:

In lesson 1, you wrote a script to automate the process of outputting log files into a more user friendly format. The format of the log was as follows:


`<date> <time> <source_ip> <destination_ip> <protocol> <size>`


The script prompted the user for the log file output and then spits out the
result in the following format:

`On <date> at <time>, the IP address <source_ip> sent a request to the
destination <destination_ip>. A packet of the size <size> was sent over the
<protocol> protocol.`

In this exercise, you will modify your code to return suspicious activity. Suspicious activity is defined as the following:

 - Any traffic with a source IP of 192.168.1.2
 - Any use of the RDP protocol
 - Any packet with a size greater or equal to 1500.

If a packet is suspicious, modify your script to output:

`Suspicious Activity was Detected on <date> at <time>, the IP address <source_ip> sent a request to the
destination <destination_ip>. A packet of the size <size> was sent over the
<protocol> protocol.`

Otherwise if a packet input does not meet any of the requirements, output:

`No suspicious activity was detected`

### Examples:
```
Input Log:
2024-06-01 10:23:45 192.168.1.2 192.168.1.10 TCP 100
Suspicious Activity was Detected on 2024-06-01 at 10:23:45, the IP address 192.168.1.2 sent a request to the destination 192.168.1.10. A packet of the size 100 was sent over the TCP protocol.
```
```
Input Log:
2024-06-01 10:20:11 192.168.5.32 192.168.1.10 RDP 22
Suspicious Activity was Detected on 2024-06-01 at 10:20:11, the IP address 192.168.5.32 sent a request to the destination 192.168.1.10. A packet of the size 22 was sent over the RDP protocol.
```
```
Input Log:
2024-06-01 10:10:02 192.168.8.24 192.168.1.10 HTTPS 1600
Suspicious Activity was Detected on 2024-06-01 at 10:10:02, the IP address 192.168.8.24 sent a request to the destination 192.168.1.10. A packet of the size 1600 was sent over the HTTPS protocol.
```
```
Input Log:
2024-06-01 09:43:55 242.168.33.43 192.168.1.10 TCP 100
No suspicious activity was detected
```
