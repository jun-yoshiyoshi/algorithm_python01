def hash_data(data, hash_key=13):
    hash_array = [False for _ in range(hash_key)]
    for i in data:
        k = i % hash_key
        while hash_array[k] is True:
            k += 1
        hash_array[k] = i
    data_array = hash_array
    return (data_array)


def hash_search(data_name, a, hash_key=13):
    k = a % hash_key
    while data_name[k] is not False:
        if data_name[k] == a:
            return k
        else:
            k+1


l = [31, 42, 115, 64, 92, 98, 75, 211]
# print(hash_data(l))
l = hash_data(l)
print(hash_search(l, 64))
