def write_to_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


write_to_file("example.txt", "Hello Python")