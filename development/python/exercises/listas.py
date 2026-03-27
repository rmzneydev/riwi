

lista1 = []

n = int(input("Ingese tamaño de la lista: "))
m = int(input("Ingese tamaño de la sublista: "))

for i in range(0, n, 1):
    sublista = []
    for j in range(0, m, 1):
        value = input(f"Ingrese letra en posicion {i},{j}: ")
        sublista.append(value)
    lista1.append(sublista)


print("\nLISTA:")
for i in range(0, len(lista1), 1):
    sub = "|"
    for item in lista1[i]:
        sub +=f" {item} |"
    print("-"*len(sub))
    print(sub)
print("-"*len(sub))