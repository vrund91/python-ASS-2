list=['RED','BLUE','GREEN']

print("original list:")
print(list)

print("\n1.append")
print("2.extend")
print("3.sort")

choice=int(input("Enter your choice:"))

if choice == 1:
    value=input("Enter value to append in list:")
    list.append(value)
    print(list)

elif choice == 2:
    list2=['1','2','3']
    list.extend(list2)
    print(list)

elif choice == 3:
    result=sorted(list)
    print("sorted:",result)

else:
    print("Invalid choice")
