# While loop example

i = 0
while i < 3:
    print("Hello, World!")
    i += 1  # i = i + 1


# Get the number of times to print the quote on the screen

while True:
    n = int(input("How many times you want to print the quote? "))
    if n > 0:
        break

for _ in range(n):
    print("To be or not to be, that is the question.")


# Write a function to to print the quote n times


# Call the function in the main function
def main():
    number = get_number()
    print_quote(number)


# Get the number of times from the user and return it
def get_number():
    while True:
        n = int(input("How many times you want to print the quote? "))
        if n > 0:
            break
    return n


# Print the quote n times
def print_quote(n):
    for _ in range(n):
        print("To be or not to be, that is the question.")


main()
