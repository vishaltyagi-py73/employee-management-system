import os

FILE_NAME = "employees.txt"


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def to_string(self):
        return f"{self.emp_id},{self.name},{self.department},{self.salary}\n"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employee = Employee(emp_id, name, department, salary)

    with open(FILE_NAME, "a") as file:
        file.write(employee.to_string())

    print("✅ Employee added successfully!")


def view_employees():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No employee records found.")
        return

    print("\n--- Employee List ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            emp_id, name, department, salary = line.strip().split(",")
            print(f"ID: {emp_id} | Name: {name} | Dept: {department} | Salary: {salary}")


def delete_employee():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No employee records found.")
        return

    emp_id = input("Enter Employee ID to delete: ")
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if line.startswith(emp_id + ","):
                found = True
            else:
                file.write(line)

    if found:
        print("🗑️ Employee deleted successfully!")
    else:
        print("❌ Employee ID not found.")


def menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
