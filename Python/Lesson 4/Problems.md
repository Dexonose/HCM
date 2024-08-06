# Data Structures
## Exercise 1
Given a dictionary of IP addresses, a script to count occurrences of suspicious activities per IP address and
summarise the total number of entries found. Print these in a readable format.

This can be done using Counter from the library collections, try to write this script without this to further challenge yourself.

The following data will be used as the test data set
```
{'ID_1': '198.168.1.2',
'ID_2': '192.168.5.32',
'ID_3': '192.168.5.32',
'ID_4': '242.168.33.43',
'ID_5': '192.34.1.2',
'ID_6': '198.168.1.2',
'ID_7': '192.168.5.32'}
```
### Example output
```
python ./Exercise_1.py
198.168.1.2, Occurrances: 2
192.168.5.32, Occurrances: 3
242.168.33.43, Occurrances: 1
192.34.1.2, Occurrances: 1
```
