def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return(data)


l = [1, 2, 15, 4, 2, 8, 5, 11, 9, 7, 13, 99, 67, 43, 76]

print(bubble_sort(l))
