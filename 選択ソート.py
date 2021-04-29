def min_serch(data):
    min = data[0]
    for i in data:
        if i < min:
            min = i
    print(min)


d = [6, 15, 4, 5, 8, 5, 11, 9, 7, 13]
min_serch(d)
