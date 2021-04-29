def insert_sort(data):
    for i in range(1, len(data)):
        a = data[i]
        while data[i-1] > a and i-1 >= 0:
            data[i] = data[i-1]
            i -= 1
        data[i] = a
    return data


l = [9, 4, 6, 8, 3, 7, 2]

print(insert_sort(l))
