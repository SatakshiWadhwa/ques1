def read_lines():
    lines = []
    print("Enter your lines (press Enter on an empty line to stop):")

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\nYou entered:")
    for line in lines:
        print(line)

# Call the function
read_lines()