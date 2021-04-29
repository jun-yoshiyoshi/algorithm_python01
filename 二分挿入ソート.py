def binary_insert_sort(data):
    for i in range(1, len(data)):
        head, tail = data[i-1], data[i]
        start, end = 0, i
        if head > tail:

            if data[0] > tail:
                a = data.pop(i)
                data.insert(0, a)
                continue

            while start <= end:
                mid = (start + end) // 2
                if data[mid-1] <= tail and tail <= data[mid]:
                    a = data.pop(i)
                    data.insert(mid, a)
                    break

                elif data[mid] < tail and tail <= data[mid+1]:
                    a = data.pop(i)
                    data.insert(mid+1, a)
                    break

                elif data[mid] < tail:
                    start = mid

                else:
                    end = mid

    return data


l = [9, 4, 6, 5, 2, 1, 0, 5, 5, 100, 8, 5, 0, 1, 44, 3, 24, 1]
l1 = [9, 4, 6, 3, 31, 88, 76, 0, 4, 199, 3, 2, 1, 0, 4, 8]
l2 = [3, 2, 1, 0, 4]

print(binary_insert_sort(l1))
