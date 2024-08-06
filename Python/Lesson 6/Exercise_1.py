ips = []
ipList = []
alerts = 0
file = open("./network_log.txt")

for line in file:
    #Split data into an array for easier referencing
    data = line.split()
    #Check for suspicious activity
    if data[2] == "192.168.1.10" or data[4] == "RDP" or int(data[5]) >= 1400:
        #Output the data.
        alerts += 1
        print(f"Suspicious Activity On {data[0]} at {data[1]}, the IP address {data[2]} sent a request to the destination {data[3]}. A packet of the size {data[5]} was sent over the {data[4]} protocol.")
        ips.insert(len(ips), data[2])

file.close()

#Sort through the identified suspicious IPs
#Get an unsorted count of each ip in the dictionary and add to list
for ip in ips:
    if ip in ipList:
        ipList[int(ipList.index(ip))+1] += 1 #Increment count
    else:
        ipList.insert(len(ipList), ip)
        ipList.insert(len(ipList), 1)
        
#Loop through and output each result
i = 0
while(i < len(ipList)):
    print(str(ipList[i]) + ", Occurrances: " + str(ipList[i+1]))
    i += 2; 

print(f"Total Alerts: {alerts}")
