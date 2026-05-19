with open("names.txt", "r") as file:
    for (
        name
    ) in (
        file
    ):  # We can sort the file and then loop through it to print the names in order using sorted(file)
        print(name.strip().capitalize())
