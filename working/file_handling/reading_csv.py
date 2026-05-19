import csv

with open("employees.csv") as file:
    for line in file:
        name, department = line.strip().split(",")
        # print(f"{name} works in {department}")


# Use a dictionary to store the data and sort the data by names
employees = []

with open("employees.csv") as file:
    reader = csv.reader(file)
    for name, department in reader:
        employees.append({"name": name, "department": department})


# Sort the employees by name
# def get_name(employee):
#     return employee["name"]


for employee in sorted(
    employees, key=lambda employee: employee["name"], reverse=False
):  # OR key=get_name
    print(f"{employee['name']} works in {employee['department']}")


with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']} is in  {row['grade']} grade")
