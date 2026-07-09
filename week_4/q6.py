def convert_to_uppercase(strings):
    result = list(map(lambda x: x.upper(), strings))
    return result


print(convert_to_uppercase(["hello", "python", "world"]))