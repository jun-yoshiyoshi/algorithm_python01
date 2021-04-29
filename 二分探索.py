def binary_serch(data, value):
    s = 0
    end = len(data)-1
    while s <= end:
        mid = (s+end)//2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            s += mid + 1
        else:
            end = mid - 1
    return -1


l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_serch(l, 30))
