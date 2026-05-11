# Write a function that greets a user by name
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


# Write a function a nested function
def main():
    x = int(input("What's x? "))
    print("x squared is: ", square(x))


def square(n):
    return n * n  #  OR     return n ** 2    OR return pow(n, 2)


# Write a function with a default argument
def greet_default(name="World"):
    print(f"Hello, {name}!")


greet_default()  # Uses default greeting
greet_default("Bob")  # Uses default greeting

main()
