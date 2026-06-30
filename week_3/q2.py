def find_maximum(list1):
    maximum = list1[0]

    for num in list1:
        if num > maximum:
            maximum = num

    return maximum


print(find_maximum([10, 25, 5, 80, 30]))