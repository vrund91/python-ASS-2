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
print("\n")

print("copy dictionary:")
dict2=my_dict.copy()
print(dict2)
print("\n")

print("update dictionary:")
my_dict['Rollno']="202201619010141"
dict2.update(my_dict)
print(dict2)
print("\n")

print("using get method to return value")
result=my_dict.get('Name','Not Found')
print(result)

result=my_dict.get('course','Not Found')
print(result)
