# Intermediate Python
## Exercise 1
Create a script to parse the data from the file logs.txt and output the number of logs of each severity. 

You are to prepend each line with the following format:
 - Errors: \-
 - Warnings: \!
 - Info: \+
 - Other: \#

The data parsed will appear as the following:
```
2024-07-17 08:00:00 INFO: Starting system service
2024-07-17 08:05:12 ERROR: Disk full, operation failed
2024-07-17 08:10:30 INFO: System backup initiated
2024-07-17 08:12:45 INFO: System backup completed successfully
2024-07-17 08:20:03 WARNING: High CPU usage detected
```

Once you have processed the data, you are to write a file for each kind of log. (error.log, info.log, warning.log)

### Example output
```diff
+ 2024-07-17 08:00:00 INFO: Starting system service
- 2024-07-17 08:05:12 ERROR: Disk full, operation failed
+ 2024-07-17 08:10:30 INFO: System backup initiated
+ 2024-07-17 08:12:45 INFO: System backup completed successfully
! 2024-07-17 08:20:03 WARNING: High CPU usage detected

Logs Recorded:
INFO: 3
WARNING: 1
ERROR: 1
```
*Note that depending on your terminal application, color formatting may not work using the provided example.*
