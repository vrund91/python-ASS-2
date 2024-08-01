number=input("Enter a three-digit number:")
r = 0
sum = 0

while(num!=0):
     r = num % 10
     sum = sum + r
     num = num//10
    
print("Sum of digits is:",sum)
