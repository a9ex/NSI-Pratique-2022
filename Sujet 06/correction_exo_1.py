def maxi(tab):
    max = tab[0]
    pos = 0
    for i in range(len(tab)):
        if tab[i] > max:
            max = tab[i]
            pos = i
    return max, pos

print(maxi([1,5,6,9,1,2,3,7,9,8]))