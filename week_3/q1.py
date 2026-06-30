def count_vowels(text):
    count = 0
    vowels = "aeiou"

    for char in text.lower():
        if char in vowels:
            count += 1

    return count