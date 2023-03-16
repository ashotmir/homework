def duplicates(my_ls):
    seen = set()
    numbers = []
    for i in my_ls:
        if i in seen:
            numbers.append(i)
        else:
            seen.add(i)
    return print(numbers)


duplicates([1, 1, 3, 5, 6, 4, 3, 2])
