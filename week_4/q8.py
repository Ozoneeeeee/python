def process_file_with_lambda(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()

    processed_lines = []

    for line in lines:
        words = line.split()

        uppercase_words = list(
            map(lambda word: word.upper(), words)
        )

        processed_lines.append(" ".join(uppercase_words))

    with open(file_name, "w") as file:
        for line in processed_lines:
            file.write(line + "\n")


process_file_with_lambda("example.txt")