import sys

# using sys module, print the path of the current script
print(sys.path)

# using sys module, print the name of the the person who is running the script
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print(arg)
