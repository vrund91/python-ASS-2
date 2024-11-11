n=int(input("Enter a number:"))
user_input= []
for i in range(n):
    number=int(input(f"Enter number {i+1}:"))
    user_input.append(number)

result=tuple(user_input)
print(result)
print("\n1.Max and min value from list.")
print("2.Length of the list")
print("3.Sorting a list")
print("4.sum of a list")

choice=int(input("Enter a your choice:"))

if choice == 1:
    max_val=max(result)
    min_val=min(result)
    print("Maxium and minimum value are:",max_val,min_val)

elif choice == 2:
    len_val=len(result)
    print("length of value is:",len_val)

elif choice == 3:
    sorted_val=sorted(result)
    print("sorted value is:",sorted_val)

elif choice == 4:
    #int_result=tuple(map(int,result))
    sum_val=sum(result)
    print("sum of list item:",sum_val)

else:
    print("Invalid choice")
    
