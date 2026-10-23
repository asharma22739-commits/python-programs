def fibonacci(n):
    a, b, seq = 0, 1, []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

n = int(input("Enter n: "))
print(fibonacci(n))
