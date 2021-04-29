def binary_insert_sort(data):
    for i in range(1, len(data)):
        head, tail = data[i-1], data[i]
        start, end = 0, i
        if head > tail:
            while start <= end:
                mid = (start + end) // 2

                if tail < data[0]:
                    a = data.pop(i)
                    data.insert(0, a)
                    break

                elif data[mid-1] <= tail and tail <= data[mid]:
                    a = data.pop(i)
                    data.insert(mid, a)
                    break

                elif data[mid] < tail and tail <= data[mid+1]:
                    a = data.pop(i)
                    data.insert(mid+1, a)
                    break

                elif data[mid] < tail:
                    start += mid + 1

                elif tail < data[mid] and mid != 0:
                    end = mid + 1

                else:
                    break
    return data


l = [9, 4, 6, 2, 1, 0, 100, 8, 44, 3, 24]
l1 = [9, 4, 6, 3]
l2 = [3, 2, 1, 0, 4]

print(binary_insert_sort(l))
