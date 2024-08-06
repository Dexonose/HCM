#Split data into an array for easier referencing
data = input("Input log file output:\n").split()
#Check for suspicious activity
if data[2] == "192.16.1.2" or data[4] == "RDP" or int(data[5]) >= 1500:
    #Output the data.
    print(f"Suspicious Activity On {data[0]} at {data[1]}, the IP address {data[2]} sent a request to the destination {data[3]}. A packet of the size {data[5]} was sent over the {data[4]} protocol.")
else:
    print("No suspicious activity detected :D")
