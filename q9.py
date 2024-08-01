my_dict={
    'apple':3,
    'banana':5,
    'mango':2,
    'cherry':7,
    'grapes':15
}
print("Dictionary item with their index:")
for index,(key,value) in enumerate(my_dict.items()):
    print(f"Index:{index},Key:{key},Value:{value}")