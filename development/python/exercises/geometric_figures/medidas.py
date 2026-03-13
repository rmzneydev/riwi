from figuras import get_figuras
operaciones = ["Perimetro", "Area", "Angulo", "Volumen"]

figuras = get_figuras()

salir = False

def selectec_figure(num_fig, figura):
    print(f"\nFigura Seleccionada: (#{num_fig}. {figura})")
    
    print("MENU DE OPERACIONES")
    
    if num_fig == 1: # Triángulo
        print(operaciones[1])
        print(operaciones[2])
        print(operaciones[0])
    elif num_fig == 2:# Hexágono
        print(operaciones[1])
        print(operaciones[2])
        print(operaciones[0])
    elif num_fig == 3:# Rectángulo
        print(operaciones[1])
        print(operaciones[2])
        print(operaciones[0])
    elif num_fig == 4:# Círculo
        print(operaciones[1])
        print(operaciones[2])
        print(operaciones[0])
    elif num_fig == 5:# Triángulo rectángulo
        print("")
    elif num_fig == 6:# Cubo
        print("")
    elif num_fig == 7:# Esfera
        print("")
    elif num_fig == 8:# Cilindro
        print("")
    elif num_fig == 9:# Prisma rectangular
        print("")
    
while not salir:
    
    print("MENU DE FIGURAS:\nLista de Figuras")
    for i in range(0, len(figuras), 1):
        
        print(f"{i+1}. {figuras[i]}")
    
    valid_sel = False
    while not valid_sel:
        try:
            seleccion = input("Digite: (numero de figura / salir): ")
            seleccion = seleccion.lower().strip()
            if seleccion != "salir":
                seleccion = int(seleccion)
                if (seleccion-1) in range(len(figuras)):
                    valid_sel = True
                    selectec_figure(seleccion, figuras[seleccion-1])
                else:
                    print(f"No existe la figura numero {seleccion}")
            else:
                valid_sel = True
                salir = True
        except ValueError:
            print("Se esperaba un dato entero")