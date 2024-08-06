#Counts the occurrances of each event type	
counter = []
#Lists the event types that have appeared in the log
event_types = []
#Initializes a list per log type (these will then be written to a file)
events = []
#Open the main log file
file = open("./Logs.txt")

for line in file:
    #split the log into each component
    comps = line.split()
    #Check if the event hasn't been seen before
    if not comps[2] in event_types:
        #Add the event type to the list
        event_types.insert(len(event_types), comps[2])
        #Create a counter for the new event type
        counter.insert(len(counter), 0)
        #Insert an empty list for the new event type
        events.insert(len(events), [])        
    #Create a variable for easier referencing
    event_index = event_types.index(comps[2])
    #Increment the occurrance counter
    counter[event_index] += 1
    
    #Add the prepend depending on log type
    if "ERROR" in comps[2]:
        line = "- " + line
    elif "WARNING" in comps[2]:
        line = "! " + line
    elif "INFO" in comps[2]:
        line = "+ " + line
    else:
        line = "# " + line
    print(line.strip())
    
    #Add the event its associated event list
    events[event_index].insert(len(events[event_index]), line)

#Output final results
print("\nLogs Recorded: ")

#Output each of the logs to a file
for ind, log_type in enumerate(events):
    #Output number of occurances 
    print(f"{event_types[ind].lower()} {counter[ind]}")
    #Create file with naming convention logtype_log.txt
    file = open(f"./{event_types[ind][0:len(event_types[ind])-1].lower()}_log.txt", "x")
    for log in log_type:
        file.write(log)
    file.close()
