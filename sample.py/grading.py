marks=int(input("enter your marks:"))
if (marks >=90 and marks <=100):
    grade="A"
elif (90>marks>=80):
    grade="B"
elif (80>marks>=70):
    grade="C"
elif (70>marks>=60):
    grade = "D"
else:
    grade = "F"
print("your grade is ->:",grade)