user_input=input("Enter a string:")
str_tup=tuple(user_input)
replicated = str_tup * 3
print("using Replicating tuple:")
print(replicated)

print("using slicing tuple:")
result=str_tup[1:6]
print(result)

print("Search an item with index:")
index=input("Enter a index to search:")
result=str_tup.index(index)
print(result)