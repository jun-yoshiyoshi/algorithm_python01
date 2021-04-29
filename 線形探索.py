def liner_serch(data, value):

    for i in data:
        if i == value:
            return i
    return -1


data = [50, 30, 90, 10, 20, 70, 60, 40, 80]
print(liner_serch(data, 10))
