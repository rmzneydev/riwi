inventario = []

def getNumInput(message: str, data_type: type) -> float | int:
    """input validation to securely collect numeric data from the user.
    It ensures that the input provided matches a specific data type (integer or decimal) 
    before returning the value.
    
    Parameters
    -
    message (str)
        The prompt shown to the user.
    data_type (type)
        The expected numeric type (int or float).
    
    Returns
    -
    int or float
    """

    valid_input = False
    
    while not valid_input:
        
        user_input = input(message).lower().strip()
        if data_type == float:
            user_input = user_input.replace(",",".")
        
        try:
            value = data_type(user_input)
            valid_input = True
                
        except ValueError:
            print(f"[ERROR] No ingreso un dato valido, ingrese un dato de tipo ({(data_type).__name__})")

    return value

def agregar_producto(): # funcion para agregar productos
    
    agregar = ""
    while agregar == "":
        print("\n[Agregando producto]")
        # solicitar datos del producto
        nombre = input("Ingrese nombre: ") 
        precio = getNumInput("Ingrese el precio: ", float)
        cantidad = getNumInput("Ingrese cantidad: ", int)
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        inventario.append(producto)
        print("> Producto agregado corectamente")
        agregar = input("> presione enter para agregar otro producto / ingrese cualquier otro dato para finalizar: ")
        agregar = agregar.strip()
    
def mostrar_inventario():
    if inventario: # si existe el inventario
        print("\n[Productos del inventario]")
        for producto in inventario: # recorre cada item en el inventario y imprime los datos nombre, precio y cantidad
            print(f"Producto: {producto["nombre"]} | precio: {producto["precio"]} | cantidad: {producto["cantidad"]}")
    else:
        print("\nEl inventario esta vacio!")
        
def calcular_estadisticas(): # obtener estadisticas
    if inventario:
        print("\n[Estadísticas básicas]")
        valor_total = 0.0
        cantidad_productos = 0
        for producto in inventario: # recorre cada item en el inventario
            valor_total += (producto["precio"] * producto["cantidad"]) # operacion basica producto * cantidad y se suma al valor total
            cantidad_productos += producto["cantidad"] # suma de cantidades
        print(f"Valor total del inventario: {valor_total}")
        print(f"cantidad total de productos resgistrados: {cantidad_productos}")
            
    else:
        print("\nNo hay productos para calcular estadisticas!")

def menu(): # Menu principal
    option = ""
    while option == "":
        print("\n[Menu de opciones]")
        print("(1) Agregar producto\n(2) Mostrar inventario\n(3) Calcular estadísticas\n(4) Salir")
        option = input("Ingrese el numero de acción a arealizar: ")
        option = option.strip() # eliminar espacios en blanco y saltos de linea
        if option == "1":
            agregar_producto()
        elif option == "2":
            mostrar_inventario()
        elif option == "3":
            calcular_estadisticas()
        elif option == "4":
            option = "salir" # asignar "salir" a la variable opcion cuando el usuario ingrese "4"
        else:
            print("La opción ingresada no es válida!")
            option = ""
    return option


def main():
    user_choise = ""
    while user_choise != "salir": # loop principal hasta que se reciva "salir" desde el menu
        user_choise = menu()

main()