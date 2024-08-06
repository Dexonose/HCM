#Solution without the use of the counter library

#Dictionary list of ips
ips = {'ID_1': '198.168.1.2',
'ID_2': '192.168.5.32',
'ID_3': '192.168.5.32',
'ID_4': '242.168.33.43',
'ID_5': '192.34.1.2',
'ID_6': '198.168.1.2',
'ID_7': '192.168.5.32'}

#Initialize empty list for later
ipList = [] 

#Get an unsorted count of each ip in the dictionary and add to list
for ip in ips.values():
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
