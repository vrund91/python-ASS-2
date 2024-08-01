tuple1=(2,4,6,8,10)

print("using all operator in tupple")
result=all(num % 2 == 0 for num in tuple1)
print("The result is using all operator:",result)

print("using any operator in tu")
result1=any(num >= 5 for num in tuple1)
print("The result is using any operator:",result1)

print("using enumerate in tupple")
result=tuple(enumerate(tuple1))
print("The result is using enumerate operator:",result)
