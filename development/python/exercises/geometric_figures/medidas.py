from figuras import get_figuras
operaciones = ["Perimetro", "Area", "Angulo", "Volumen"]

figuras = get_figuras()

salir = False

def selectec_figure(num_fig, figura):
    print(f"\nFigura Seleccionada: (#{num_fig}. {figura})")
    
    print("MENU DE OPERACIONES")
    
    if num_fig == 1:
        print(operaciones[1])
    elif num_fig == 2:
        print(operaciones)
    elif num_fig == 3:
        print("")
    elif num_fig == 4:
        print("")
    elif num_fig == 5:
        print("")
    elif num_fig == 6:
        print("")
    elif num_fig == 7:
        print("")
    elif num_fig == 8:
        print("")
    elif num_fig == 9:
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