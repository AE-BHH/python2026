import csv

with open("employees.csv", "a") as file:
    file.write("Name,Department\n")
    file.write("Sam,Engineering\n")
    file.write("Alex,Marketing\n")
    file.write("John,Engineering\n")
    file.write("Emily,Sales\n")
file.close()

name = input("What's your name? ")
grade = input("What's your grade? ")


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "grade"])
    writer.writerow({"name": name, "grade": grade})

file.close()
