# x = int(input("What's x? "))
# y = int(input("What's y? "))

# # elif & elif & else
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")


# # or operators
# x = int(input("What's x? "))
# y = int(input("What's y? "))
# if x < y or x > y:
#     print("x is not equal to y")

# x = 5
# y = 10
# if x < y and x > 0:
#     print("x is less than y and greater than 0")


# score = int(input("What is the score? "))

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# def main():
#     x = int(input("What's x? "))

#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")


# def is_even(n):
#     return n % 2 == 0  # or    return True if n % 2 == 0 else False


# main()

# Match case (Python 3.10+)
name = input("What is your name? ").strip().title()

match name:
    case "Alice" | "Bob" | "Charlie" | "David" | "Eve":
        print(f"Hello, {name}!")
    case _:
        print("Hello, stranger!")
