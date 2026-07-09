def to_title_case(sentence):
    words = sentence.split()
    result = []

    for word in words:
        result.append(word[0].upper() + word[1:].lower())

    return " ".join(result)