def CalculateArea():
    #Prompt for input
    print("Input Width + Height to calculate area of rectangle")
    #Create a variable holding user input values
    vals = input("x y\n").strip().split()
    #Compare values to check if the shape is a square
    if vals[0] == vals[1]:
        #Output first value squared, no need to fetch the second value again. 
        print("Area of square: " + str(pow(float(vals[0]), 2)))
    else:
        #Multiply values and output to console 
        print("Area of rectangle: " + str(float(vals[0]) * float(vals[1])))
    

def ConvertTemperature():
    #Prompt user for input of chosen metric.
    if(input("Convert Temp from (C/F):") == "C"):
        print(float(input("Enter Temperature in Celsius\n")) * 9/5 + 32)
    else:
        print((float(input("Enter Temperature in Fahrenheit")) - 32) * 5/9)

def OutputLog():
    #Split data into an array for easier referencing
    data = input("Input log file output:\n").split()
    #Check for suspicious activity
    if data[2] == "192.16.1.2" or data[4] == "RDP" or int(data[5]) >= 1500:
        #Output the data.
        print(f"Suspicious Activity On {data[0]} at {data[1]}, the IP address {data[2]} sent a request to the destination {data[3]}. A packet of the size {data[5]} was sent over the {data[4]} protocol.")
    else:
        print("No suspicious activity detected :D")


option = input("Choose what you would like to do:\n1 - Calculate Area\n2 - Convert Temperature\n3 - Output Logs\n")
if option == "1":
    CalculateArea()
elif option == "2":
    ConvertTemperature()
else:
    OutputLog()
