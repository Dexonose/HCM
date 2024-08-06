#Prompt for input
print("Input Width + Height to calculate area of rectangle")
#Create a variable holding user input values
vals = input("x y\n").strip().split()
#Multiply values and output to console
print("Area of rectangle: " + str(float(vals[0]) * float(vals[1])))
