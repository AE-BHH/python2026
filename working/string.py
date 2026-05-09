# Ask user for their  name and remove any extra spaces
first_name = input("What is your name? ").strip()
last_name = input("What is your last name? ").strip()

# Combine first and last name
full_name = first_name + " " + last_name

# Say hello to the user
print("Hello, " + full_name + "!")


x = int(input("What's x?"))
y = int(input("What's y?"))
print(x + y)
