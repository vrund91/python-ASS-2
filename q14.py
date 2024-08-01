user_input=(input("Enter a value:"))
list1=[item.strip() for item in user_input.split(',')]

print("original list")
print(list1)

append1=input("Enter a value:")
list1.append(append1)
print("using append method")
print(list1)

user_input=(input("Enter a value:"))
list2=[item.strip() for item in user_input.split(',')]

print("extend list:")
list1.extend(list2)
print(list1)

result=sorted(list1)
print("sorted list:")
print(result)