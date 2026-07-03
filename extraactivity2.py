def employee_details(name, emp_id, department, salary):
    print("\nEmployee Details")
    print("----------------------")
    print("Employee name: ", name)
    print("Employee ID: ", emp_id)
    print("Employee Department: ", department)
    print("Employee Salary: ", salary)

employee_name = input("Enter Employee name: ")
emp_id = input("Enter employee ID: ")
department = input("Enter department ")
salary = float(input("Enter salary: "))

employee_details(employee_name, emp_id,department, salary )