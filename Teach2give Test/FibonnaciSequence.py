# question 2: Fibonacci sequence
a, b = 0, 1
n = 10

print(a, b)
for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c