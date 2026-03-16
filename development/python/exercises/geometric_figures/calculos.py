def get_figuras():
    figuras = ["Triángulo",
        "Triángulo rectángulo",
        "Rectángulo",
        "Hexágono",
        "Círculo",
        "Cubo",
        "Esfera",
        "Cilindro",
        "Prisma rectangular"]
    return figuras

def get_calculos():
    calculos = ["Perimetro", "Ángulos", "Area", "Volumen", "Circunferencia"]
    return calculos

def calculate(num_figura, nombre_calculo):
    nombre_figura = get_figuras()[num_figura-1]
    print("=" *50)
    print(f"[FIGURA] -> ({nombre_figura})\n[CALCULAR] -> ({nombre_calculo}) ")
    print("=" *50)
    
    num_calculo = get_calculos().index(nombre_calculo)
    result = ""

    if num_calculo == 0:
        perimetro = get_perimetro(num_figura)
        result = f"El Perimetro es: {perimetro:.1f} cm"
    elif num_calculo == 1:
        angulos = get_angulo(num_figura)
        result = angulos
    elif num_calculo == 2:
        area = get_area(num_figura)
        result = f"El Area es: {area:.1f} cm"
    elif num_calculo == 3:
        volumen = get_volumen(num_figura)
        result = f"El Volumen es: {volumen:.1f} cm³"
    elif num_calculo == 4:
        circunferencia = get_circunferencia(num_figura)
        result = f"La Circunferencia es: {result:.1f}"

    print("=" *15, "RESULTADO", "=" *15)
    print(result)
    print("="*41)

def get_area(num_figura):
    
    PI = 3.14159

    area = None

    if num_figura == 1 or num_figura == 2: # Triángulo / Triángulo rectángulo
        base = float(input("Ingrese la base (Float): "))
        altura = float(input("Ingrese la altura (Float): "))
        area = (base * altura) / 2
    
    elif num_figura == 3: # Rectangulo
        base = float(input("Ingrese la base (Float): "))
        altura = float(input("Ingrese la altura (Float): "))
        area = base * altura

    elif num_figura == 4: # Hexagono
        lado = float(input("Ingrese la longitud del lado (Float): "))
        raiz_3 = 3 ** 0.5
        area = ((3 * raiz_3) / 2) * (lado ** 2)
    
    elif num_figura == 5: # Circulo
        radio = float(input("Ingrese el radio del Circulo (Float): "))
        area = PI * (radio ** 2)

    elif num_figura == 6: # Cubo
        lado = float(input("Ingrese la longitud del lado del cubo (Float): "))
        area = 6 * (lado ** 2)

    elif num_figura == 7: # Esfera
        radio = float(input("Ingrese el radio de la Esfera (Float): "))
        
        area = 4 * PI * (radio ** 2)
    
    elif num_figura == 8: # Cilindro
        radio = float(input("Ingrese el radio del cilindro (Float): "))
        altura = float(input("Ingrese la altura del cilindro (Float): "))
        area = 2 * PI * radio * (radio + altura)
    
    elif num_figura == 9: # Prisma rectangular
        largo = float(input("Ingrese el largo del Prisma (Float): "))
        ancho = float(input("Ingrese el ancho del Prisma (Float): "))
        alto = float(input("Ingrese el alto del Prisma (Float): "))
        area = 2 * ((largo * ancho) + (largo * alto) + (ancho * alto))
    
    return area

def get_angulo(num_figura):

    if num_figura == 1: # Triángulo
        angulo1 = float(input("Ingrese el ángulo lado A (Float): "))
        angulo2 = float(input("Ingrese el ángulo lado B (Float): "))
        tercer_angulo = 180 - (angulo1 + angulo2)
        return f"El Ángulo C = {tercer_angulo}"
    
    elif num_figura == 2: # Triángulo rectángulo
        opuesto = float(input("Ingrese longitud del lado A (Opuesto) (Float): "))
        adyacente = float(input("Ingrese longitud del lado B (Adyacente) (Float): "))
        angulo = angulo_op_ady(opuesto, adyacente)
        angulo_b = str(f"{90-angulo:.2f}")
        angulo = str(f"{angulo:.2f}")
        
        return f"Ángulo lado A: {angulo}°\nÁngulo lado B: {angulo_b}°\nÁngulo lado C: 90°"
    
    elif num_figura == 3: # Rectangulo
        return "Los Ángulos son de: 90° en cada lado"

    elif num_figura == 4: # Hexagono
        return "Los Ángulos son de: 120° cada lado"
    
    elif num_figura == 5: # Circulo
        return "El Ángulo es de: 360° en total"


def get_perimetro(num_figura):

    perimetro = None

    if num_figura == 1: # Triángulo
        lado1 = float(input("Ingrese longitud (cm) del lado 1 (Float): "))
        lado2 = float(input("Ingrese longitud (cm) del lado 2 (Float): "))
        lado3 = float(input("Ingrese longitud (cm) del lado 3 (Float): "))
        perimetro = lado1 + lado2 + lado3
    
    elif num_figura == 2: # Triángulo rectángulo
        cateto1 = float(input("Ingrese el primer cateto (Float): "))
        cateto2 = float(input("Ingrese el segundo cateto (Float): "))
        hipotenusa = (cateto1**2 + cateto2**2)**0.5
        perimetro = cateto1 + cateto2 + hipotenusa

    elif num_figura == 3: # Rectangulo
        base = float(input("Ingrese la base (cm) del rectángulo (Float): "))
        altura = float(input("Ingrese la altura (cm) del rectángulo (Float): "))
        perimetro = 2 * (base + altura)
    
    elif num_figura == 4: # Hexágono
        lado = float(input("Ingrese la medida del lado del hexágono (Float): "))
        perimetro = 6 * lado

    return perimetro

def get_volumen(num_figura):

    PI = 3.14159

    volumen = None
    
    if num_figura == 6: # Cubo
        lado = float(input("Ingrese la longitud (cm) del lado del cubo (Float): "))
        volumen = lado ** 3

    elif num_figura == 7: # Esfera
        radio = float(input("Ingrese el radio de la esfera (Float): "))
        volumen = (4/3) * PI * (radio ** 3)
    
    elif num_figura == 8: # Cilindro
        radio = float(input("Ingrese el radio del cilindro (Float): "))
        altura = float(input("Ingrese la altura del cilindro (Float): "))
        volumen = PI * (radio**2) * altura
    
    elif num_figura == 9: # Prisma rectangular
        largo = float(input("Ingrese el largo (cm) del Prisma (Float): "))
        ancho = float(input("Ingrese el ancho (cm) del Prisma (Float): "))
        alto = float(input("Ingrese el alto (cm) del Prisma (Float): "))
        volumen = largo * ancho * alto
    
    return volumen

def get_circunferencia(num_figura):
    PI = 3.14159

    if num_figura == 5: # Circulo
        radio = float(input("Ingrese el radio del circulo (Float): "))
        circunferencia = 2 * PI * radio
        return circunferencia

def angulo_op_ady(opuesto, adyacente):
    
    PI = 3.14159
    
    if opuesto == adyacente:
        return 45.0
    
    x = opuesto / adyacente

    invertido = False
    
    if x > 1:
        x = (1 / x)
        invertido = True
    
    x3 = (x**3) / 3
    x5 = (x**5) / 5
    x7 = (x**7) / 7
    x9 = (x**9) / 9
    x11 = (x**11) / 11
    x13 = (x**13) / 13
    x15 = (x**15) / 15
    
    arctan_x = x - x3 + x5 - x7 + x9 - x11 + x13 - x15
    
    if invertido:
        radianes = (PI / 2) - arctan_x
    else:
        radianes = arctan_x

    grados = radianes * (180 / PI) 
    return grados
