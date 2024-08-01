user_input=(input("Enter a value:"))

data=tuple(map(int,user_input.split(',')))   #map is a function  all items in a list (or any iterable)

max_val=max(data)

min_val=min(data)

len_val=len(data)

sorted_val=tuple(sorted(data))

sum_val=sum(data)

print(f"The original value is:{data}")

print(f"The Maximum value is:{max_val}")

print(f"The Minimum value is:{min_val}")

print(f"The length of list:{len_val}")

print(f"The sorted of list:{sorted_val}")

print(f"The sum of list:{sum_val}")
