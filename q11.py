name=(input("Enter a name:"))
rollno=int(input("Enter a roll no:"))
email=(input("Enter a email:"))
phone=int(input("Enter a phone number:"))
blood=(input("Enter your blood group:"))

my_dict={
    'Name':name,
    'Rollno':rollno,
    'Email':email,
    'Phone':phone,
    'Blood':blood
}
ur_dict1={
    'Name':name,
    'Rollno':rollno,
    'Email':email,
    'Phone':phone
}

print(my_dict.items())
print("\n",ur_dict1.items())

print("\n1.Delete")
print("2.compare")
print("3.remove")

choice=int(input("Enter your choice:"))

if choice == 1:
    del_key=input("Enter key to delete:")
    if del_key in my_dict:
        del my_dict[del_key]
        print(f"Deleted Successfully{del_key}.")
        print(my_dict.items())
    else:
        print("key not found")

elif choice == 2:
    if my_dict == ur_dict1:
        print("Both dictionary are equal")
    else:
        print("Dictionary are not equal")

elif choice == 3:
    ur_dict1.clear()
    print("remove the dictionary")

else:
    print("Invalid choice")
