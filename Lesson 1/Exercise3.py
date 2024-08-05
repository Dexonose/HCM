#Split data into an array for easier referencing
data = input("Input log file output:\n").split()
#Output the data.
print(f"On {data[0]} at {data[1]}, the IP address {data[2]} sent a request to the destination {data[3]}. A packet of the size {data[4]} was sent over the {data[5]} protocol.")
