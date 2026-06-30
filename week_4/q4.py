def check_file_empty(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    if content == "":
        return True
    else:
        return False


print(check_file_empty("example.txt"))