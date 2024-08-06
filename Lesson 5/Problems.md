# File Handling

## Exercise 1:
Using the supplied logs.txt, create a script which opens and prints its contents line by line.

### Examples:
```
./Output.py
2024-06-01 10:23:45 198.168.1.2 192.168.1.10 TCP 100
2024-06-01 10:20:11 192.168.5.32 192.168.1.10 RDP 22
2024-06-01 10:10:02 192.168.8.24 192.168.1.10 HTTP 1600
2024-06-01 09:43:55 242.168.33.43 192.168.1.10 TCP 100
2024-06-01 08:22:40 192.34.1.2 192.168.1.10 TCP 800
2024-05-30 06:04:37 192.168.1.2 192.168.1.10 RDP 220
2024-05-28 00:12:52 142.168.1.2 192.168.1.10 TCP 100
```

## Exercise 2:
Using the script from Lesson 2, Exercise 3, create a script which loops through each line of the file and analyses for suspicious behaviour.

### Examples:
```
./Output.py
No suspicious activity detected
Suspicious Activity On 2024-06-01 at 10:20:11, the IP address 192.168.5.32 sent a request to the destination 192.168.1.10. A packet of the size 22 was sent over the RDP protocol.
Suspicious Activity On 2024-06-01 at 10:10:02, the IP address 192.168.8.24 sent a request to the destination 192.168.1.10. A packet of the size 1600 was sent over the HTTP protocol.
No suspicious activity detected
No suspicious activity detected
Suspicious Activity On 2024-05-30 at 06:04:37, the IP address 192.168.1.2 sent a request to the destination 192.168.1.10. A packet of the size 220 was sent over the RDP protocol.
No suspicious activity detected
```

## Exercise 3:
Take the previous script and modify it to output the results to Results.txt

### Examples:
```
./Output.py
No suspicious activity detected
Suspicious Activity On 2024-06-01 at 10:20:11, the IP address 192.168.5.32 sent a request to the destination 192.168.1.10. A packet of the size 22 was sent over the RDP protocol.
Suspicious Activity On 2024-06-01 at 10:10:02, the IP address 192.168.8.24 sent a request to the destination 192.168.1.10. A packet of the size 1600 was sent over the HTTP protocol.
No suspicious activity detected
No suspicious activity detected
Suspicious Activity On 2024-05-30 at 06:04:37, the IP address 192.168.1.2 sent a request to the destination 192.168.1.10. A packet of the size 220 was sent over the RDP protocol.
No suspicious activity detected
Wrote results to Results.txt
```
