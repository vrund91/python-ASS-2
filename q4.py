num1=int(input("Enter a first number:"))
num2=int(input("Enter a second number:"))
num3=int(input("Enter a Third number:"))

greatest=0

if (num1 >= num2) and (num1 >= num3):
    greatest = num1
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2
else:
    greatest = num3

print("The greatest number is: ",greatest)