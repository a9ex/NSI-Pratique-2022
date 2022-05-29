def convertir(T):
    decimal = 0
    for i in range(len(T)):
        decimal += T[i] * 2**(len(T)-i-1)
    return decimal

print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))
