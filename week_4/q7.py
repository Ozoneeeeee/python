def filter_even_length_words(words):
    result = list(filter(lambda x: len(x) % 2 == 0, words))
    return result


print(filter_even_length_words(["cat", "dog", "python", "code"]))