# for i in [0, 1, 2]:
#     print("Hello, World!")
# # OR
# for i in range(3):
#     print("Hello, World!")

# # OR
# for _ in range(3):
#     print("Hello, World!")
# # OR
# print("Hello, World!\n" * 3, end="")


# Create a list and loop through it
# employees = ["Sarah", "Mary", "John", "Smith"]

# for employee in employees:
#     print(employee)

# # OR
# for i in range(len(employees)):
#     print(employees[i])

# # OR
# for i, employee in enumerate(employees):
# print(i + 1, employee)  # to avoid starting from 0, use i + 1 instead of i

# Use for loop on dictionary

data = {"name": "Alice", "age": 30, "city": "New York"}
for i in data:
    print(i, data[i])
