n=100
prime = {i for i in range(2, n)}
for i in range(2,n):
    if i in prime:
        for j in range(i*2, n, i):
            if j in prime:
                prime.remove(j)
print(prime)