num = int(input("Enter a number:"))
if num < 2:
    print("Not a prime number")
else:
    is_prime = True

for i in range(2,int(num/2)+1):
    if num % i == 0:
        is_prime = False
        break

if(is_prime):
    print("prime number")
else:
    print("not prime number")
