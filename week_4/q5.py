def reverse_file_content(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    reversed_content = content[::-1]

    with open("reversed.txt", "w") as file:
        file.write(reversed_content)


reverse_file_content("example.txt")