name=(input("Enter a name:"))
rollno=int(input("Enter a roll no:"))
email=(input("Enter a email:"))
phone=int(input("Enter a phone number:"))

my_dict={
    'Name':name,
    'Rollno':rollno,
    'Email':email,
    'Phone':phone
}
print(type(my_dict.keys()))
print(my_dict.keys())

print(type(my_dict.values()))
print(my_dict.values())

print(type(my_dict.items()))
print(list(my_dict.items()))