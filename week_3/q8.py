def char_count(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


print(char_count("hello"))