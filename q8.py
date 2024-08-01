user_input=(input("Enter a values:"))
fruits=[fruit.strip() for fruit in user_input.split(',')]
print("1.enumerate")
print(fruits)
for index,fruit in enumerate(fruits):
   print(f"index:{index},fruits:{fruit}")

user_input=(input("Enter a value:"))
vv=tuple(user_input)
result=all(int(i) % 2 == 0 for i in vv)
print("using all operator")
print(f"All element are even:{result}")

user_input=(input("Enter a value:"))
vv=list[user_input]
print("using any operator")
result=any(vv)
print(f"Result using any:{result}")