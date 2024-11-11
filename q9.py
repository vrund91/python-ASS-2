n=int(input("Enter a number of dict:"))
user_input=[]
for i in range(n):
    name=input("Enter a name:")
    age=int(input("Enter a age:"))
    roll=int(input("Enter a roll no:"))
    course=input("Enter your course:")
    div=input("Enter your division:")

    my_dict={
        'Name':name,
        'Age':age,
        'Roll':roll,
        'Course':course,
        'Div':div 
    }
    user_input.append(my_dict)

for index,student in enumerate(user_input):
    print(f"\nstudent:{index + 1}:")
    for key,value in student.items():
        print(f"Key: {key},Value: {value}")
