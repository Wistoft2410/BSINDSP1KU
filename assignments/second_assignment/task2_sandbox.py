list = [["Hello", 123, 231], ["Hej", 654, 866], ["Davs", 345, 234],["Goddag", 534, 765], ["Møjn", 657, 456]]
print(list[0][0])

# find ud af hvordan man tager længden af en 2D list
def length():
    rows = len(list)
    columns = len(list[0])

    total_length = rows * columns
    print(columns)

def main():
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
    length()

if __name__ == "__main__":
	# Executes only if run as a script
	main()