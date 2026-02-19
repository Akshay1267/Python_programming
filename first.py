# print("Hello World")

rightAngle = int(input("Enter the right angle of triangle:"))
leftAngle = int(input("Enter the left angle of triangle:"))
bottomAngle = int(input("Enter the bottom angle of triangle:"))

if(rightAngle + leftAngle + bottomAngle == 180): 
    print("This is a triangle")
else:
    print("This is not a triangle")