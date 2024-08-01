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

print("Original Dictionary:")
print(my_dict)

print("copy dictionary:")
copy=my_dict.copy()
print(copy)

key_update='Rollno'
key_val=202201619010141

if key_update in my_dict:
    my_dict[key_update]=key_val
    print(f"updated {key_update} to {key_val}")
else:
    print(f"{key_update} Not Found")
    print("Dictionary after update:")

print("After updated:")
print(my_dict)

print("using get method to return value")
result=my_dict.get('Name','Not Found')
print(result)

result=my_dict.get('course','Not Found')
print(result)