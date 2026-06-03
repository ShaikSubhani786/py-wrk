class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)
        print()


# Creating three employee objects
emp1 = Employee(101, "Anil", 50000)
emp2 = Employee(102, "Priya", 60000)
emp3 = Employee(103, "Rahul", 55000)

# Displaying employee details
emp1.display_details()
emp2.display_details()
emp3.display_details()