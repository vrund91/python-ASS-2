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

print("My dictionary:",my_dict.items())
print("ur dictionary:",ur_dict1.items())

del_key='Blood' 
if del_key in my_dict:
    del my_dict[del_key]
    print(f"After deleted:{del_key}.",my_dict)
else:
    print("Not found")

print("My dictionary:",my_dict.items())

if my_dict == ur_dict1:
    print("Dictionary 1 and Dictionary 2 are equal")
else:
    print("Dictionary are not equal")

ur_dict1.clear()
print("Remove dictionary successfully")