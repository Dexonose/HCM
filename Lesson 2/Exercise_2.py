#Prompt user for input of chosen metric.
if(input("Convert Temp from (C/F):") == "C"):
    print(float(input("Enter Temperature in Celsius\n")) * 9/5 + 32)
else:
    print((float(input("Enter Temperature in Fahrenheit")) - 32) * 5/9)
