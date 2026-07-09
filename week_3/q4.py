def largest_word(sentence):
    words = sentence.split()

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(largest_word("Python programming is awesome"))