def fibonacci(n):
    u = [None, 1, 1]
    i = 2
    while len(u) <= n:
        i = i + 1
        u.append(u[i-2] + u[i-1])
    return u[n]