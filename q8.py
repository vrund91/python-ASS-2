n=int(input("Enter a number:"))
user_input=[]
for i in range(n):
    number=int(input(f"Enter number {i+1}:"))
    user_input.append(number)

result=tuple(user_input)
print(result)

print("1.All")
print("2.any")
print("3.enumerate")

choice=int(input("Enter a your choice:"))

if choice == 1:
    print(all(result))

elif choice == 2:
    print(any(result))

elif choice == 3:
    enumerate_val=list(enumerate(result))
    print(enumerate_val)

else:
    print("invalid choice")
