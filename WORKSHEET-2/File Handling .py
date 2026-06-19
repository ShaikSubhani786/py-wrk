# Store 5 student names in students.txt
with open("students.txt", "w") as file:
    file.write("Anil\n")
    file.write("Priya\n")
    file.write("Rahul\n")
    file.write("Sneha\n")
    file.write("Kiran\n")

# Read and display all names
with open("students.txt", "r") as file:
    students = file.readlines()

print("Student Names:")
for student in students:
    print(student.strip())

# Count the total number of students
count = len(students)
print("\nTotal Number of Students:", count)