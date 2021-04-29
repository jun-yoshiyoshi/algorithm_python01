def quick_sort(data):
    n = len(data)
    if n <= 1:
        return data

    pivot, right, left = data[0], [], []

    for i in range(1, n):

        if data[i] < pivot:
            left.append(data[i])

        else:
            right.append(data[i])

    return quick_sort(left)+[pivot]+quick_sort(right)


l = [9, 4, 6, 5, 2, 1, 0, 5, 5, 100, 8, 5, 0, 1, 44, 3, 24, 1]
l1 = [9, 4, 6, 3, 31, 88, 76, 0, 4, 199, 3, 2, 1, 0, 4, 8]
l2 = [3, 2, 1, 0, 4, 5, 9, 7, 8, 11, 10]
l3 = [10, 5, 6, 3]

print(quick_sort(l2))
