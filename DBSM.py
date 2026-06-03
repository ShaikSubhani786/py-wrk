# Dictionary to store student details
students = {
    "Anil": {"Marks": 89, "Grade": "A"},
    "Priya": {"Marks": 95, "Grade": "A+"},
    "Rahul": {"Marks": 78, "Grade": "B"},
    "Sneha": {"Marks": 92, "Grade": "A"},
    "Kiran": {"Marks": 85, "Grade": "B+"}
}

# Display all student details
print("Student Details:")
for name, details in students.items():
    print("Name:", name)
    print("Marks:", details["Marks"])
    print("Grade:", details["Grade"])
    print()

# Find the student with the highest marks
top_student = max(students, key=lambda x: students[x]["Marks"])

print("Student with Highest Marks:")
print("Name:", top_student)
print("Marks:", students[top_student]["Marks"])
print("Grade:", students[top_student]["Grade"])