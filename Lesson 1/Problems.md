# Introduction to Python and basic syntax:

## Exercise 1: 
Write a program that calculates and prints the area of a rectangle when given user
input of length and width. Name the file AreaRectangle.py

### Examples:
```
Enter rectangle dimensions: (X Y)
4 4
Area of rectangle: 16.0
```
```
Enter rectangle dimensions: (X Y)
5 7
Area of rectangle: 35.0
```
```
Enter rectangle dimensions: (X Y)
6 9
Area of rectangle: 54.0
```

## Exercise 2:
Write a program that converts Celsius to Fahrenheit.
The formula is F = C * 9/5 + 32.

### Examples:
```
Enter number to convert:
23
73.4
```
```
Enter number to convert:
50
122.0
```
```
Enter number to convert:
40
104.0
```

## Exercise 3:
In your work as a Vulnerability analyst, you might need to automate the process of
reading log files and outputting them into a more readable format.
In this exercise, you are given the Log file output of
2024-06-01 10:23:45 198.147.1.2 192.168.1.10 TCP 1500
Which is in the format of
<date> <time> <source_ip> <destination_ip> <protocol> <size>
Write a script (Log_file.py) that prompts the user for the log file output and then
spits out the result in the following format:
“On <date> at <time>, the IP address <source_ip> sent a request to the destination
<destination_ip>. A packet of the size <size> was sent over the <protocol>
protocol.”

### Examples:
```
Enter log file:
2024-06-01 10:23:45 198.147.1.2 192.168.1.10 TCP 1500
On 2024-06-01 at 10:23:45, the IP address 198.147.1.2 sent a request to the destination 192.168.1.10. A packet of the size 1500 was sent over the TCP protocol.
```
```
Enter log file:
2023-06-01 05:23:45 198.147.3.2 192.168.1.20 HTTP 500
On 2023-06-01 at 05:23:45, the IP address 198.147.3.2 sent a request to the destination 192.168.1.20. A packet of the size 500 was sent over the HTTP protocol.
```
```
Enter log file:
2024-03-01 10:03:25 192.147.5.2 192.68.1.10 TLS 300
On 2024-03-01 at 10:03:25, the IP address 192.147.5.2 sent a request to the destination 192.68.1.10. A packet of the size 300 was sent over the TLS protocol.
```
