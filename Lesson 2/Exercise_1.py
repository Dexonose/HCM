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
