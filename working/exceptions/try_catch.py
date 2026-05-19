# Get an integer input from the user and print it on the screen
# while True:
#     try:
#         x = int(input("Waht's x? "))
#     except ValueError:
#         print("Input is not a valid integer.")
#     else:
#         break
# print(f"x is {x}")


# Do the same thing but with a function


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            break  # OR you can do return x here and remove the break statement or you can write return int(input("What's x? ")) directly in the try block and remove the break statement
        except ValueError:
            print(
                "Input is not an integer."
            )  # if you want to be a little friendly with user you can just use "pass" instead of print statement in except block

    return x


main()
