def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    if n1<0:
        return -multiplication(-n1, n2)
    if n2<0:
        return -multiplication(n1, -n2)
    else:
        return n1 + multiplication(n1, n2-1)

print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))