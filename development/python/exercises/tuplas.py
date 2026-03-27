tupla = (1, "a", "d", 1.5, "d", "x", 1, 4, 5, True, False, "22", 4.5, 1, 5 ,6)

print(tupla.count(1))
print(tupla.index("x"))

i, *j, k = tupla
print(i, j, k)

*j, k = tupla
print(j, k)

i, *j = tupla
print(i, j)

i, j, *k, l = tupla
print(i, j, k, l)



