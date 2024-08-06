# Revision
## Exercise 1
Your job is to write a Python script to analyse log files based off the following:

 - Open and read the file network_log.txt
 - Filter for suspicious activities
 - Count the number of suspicious activities that occur (by source IP)
 - Output the total number of suspicious activities which occurred
 - Output all results to the terminal

Suspicious Data is defined as the following:

 - Traffic from or to 192.168.1.10
 - Traffic with a size above 1400 bytes
 - Traffic using the RDP protocol

### Example output
```
./Exercise_1.py
Suspicious Activity On 2024-06-01 at 10:20:11, the IP address 192.168.5.32 sent a request to the destination 192.168.1.10. A packet of the size 22 was sent over the RDP protocol.
Suspicious Activity On 2024-06-01 at 10:10:02, the IP address 192.168.5.32 sent a request to the destination 192.168.1.10. A packet of the size 1600 was sent over the HTTP protocol.
Suspicious Activity On 2024-05-30 at 06:04:37, the IP address 192.168.1.2 sent a request to the destination 192.168.1.10. A packet of the size 220 was sent over the RDP protocol.
192.168.5.32, Occurrances: 2
192.168.1.2, Occurrances: 1
Total Alerts: 3
```
