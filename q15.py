my_list=[]
for i in range(10):
    value=(input("Enter a value:"))
    my_list.append(value)

my_list = list(set(my_list))
print("Removing duplicates:")
print(my_list)