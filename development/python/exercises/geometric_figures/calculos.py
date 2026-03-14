def get_figuras():
    figuras = ["Triángulo", "Hexágono", "Rectángulo", "Círculo", "Triángulo rectángulo", "Cubo", "Esfera", "Cilindro", "Prisma rectangular"]
    return figuras

def get_calculos():
    calculos = ["Perimetro", "Angulo", "Area", "Volumen", "Circunferencia"]
    return calculos

def calculate(num_figura, nombre_calculo):
    
    nombre_figura = get_figuras()[num_figura-1]
    print(f"\nCalcular -> {nombre_calculo} de la figura: ({nombre_figura}) <-")
    
    num_calculo = get_calculos().index(nombre_calculo)
    result = ""
    if num_calculo == 0:
        result = get_perimetro(num_figura)
    if num_calculo == 1:
        result = get_angulo(num_figura)
    if num_calculo == 2:
        result = get_area(num_figura)
    if num_calculo == 3:
        result = get_volumen(num_figura)
    if num_calculo == 4:
        result = get_circunferencia(num_figura)
    
    
    if result == None:
        print("Aun no implementado =)")
    else:
        print(f"\n[RESULTADO] El {nombre_calculo} de su ({nombre_figura}) es {result}")

def get_area(num_figura):
    
    if num_figura == 1: # Triángulo
        base = float(input("Introduce la base (Float): "))
        altura = float(input("Introduce la altura (Float): "))
        area = (base * altura) / 2
        return area

def get_angulo(num_figura):
    print("")

def get_perimetro(num_figura):
    print("")

def get_volumen(num_figura):
    print("")

def get_circunferencia(num_figura):
    print("")


    
    # if num_fig == 1: # Triángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 2:# Hexágono
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 3:# Rectángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 4:# Círculo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])        
    # elif num_fig == 5:# Triángulo rectángulo
    #     print(calculos[0])
    #     print(calculos[1])
    #     print(calculos[2])  
    # elif num_fig == 6:# Cubo
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 7:# Esfera
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 8:# Cilindro
    #     print(calculos[2])
    #     print(calculos[3])  
    # elif num_fig == 9:# Prisma rectangular
    #     print(calculos[2])
    #     print(calculos[3])