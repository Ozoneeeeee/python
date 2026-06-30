def find_longest_word(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    words = content.split()

    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(find_longest_word("example.txt"))