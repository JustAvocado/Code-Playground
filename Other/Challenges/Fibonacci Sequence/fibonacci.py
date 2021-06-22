def fibonacci(n):
    n1, n2, temp = 0, 1, 0
    for i in range (0, n):
        print(n1)
        temp = n1
        n1 += n2
        n2 = temp

fibonacci(5);
