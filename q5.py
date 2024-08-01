number=input("Enter a three-digit number:")

if len(number)!=3 or not number.isdigit():
    print("please enter three-digit number.")
else:
    digit1 = int(number[0])
    digit2 = int(number[1])
    digit3 = int(number[2])

    total_sum = digit1 + digit2 + digit3

print(f"The sum of digit is: {total_sum}")       