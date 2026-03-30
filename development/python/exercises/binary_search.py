array = [15,35,56,70,72,85,90,105]

b = int(input("Ingrese numero a buscar: "))

izq = 0
der = len(array)-1

sw = False
while izq <= der and not sw:
        
    med = (izq+der)//2
    if array[med]==b:
        print("bingo")
        sw = True
    elif array[med] > b:
        der = med - 1
    else:
        izq = med + 1
        
    if izq>der:
        print("Elemento no encontrado")
        
        
    
