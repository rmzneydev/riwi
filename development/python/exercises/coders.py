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
            print(f"[ERROR] No ingreso un tipo de dato valido, ingrese un dato tipo ({(data_type).__name__})")

    return value

coder_list = {1: {'id': 1143, 'Nombre': 'jen', 'Apellido': 'rmz', 'Edad': 29, 'nvlIngles': 'b1'}, 
            2: {'id': 1234, 'Nombre': 'jesus', 'Apellido': 'vid', 'Edad': 23, 'nvlIngles': 'c1'}}

def coder_data():
    coder_id = getNumInput("Ingrese id: ", int)
    name = input("Ingrese nombre: ")
    last_name = input("Ingrese apellido: ")
    age = getNumInput("Ingrese edad: ", int)
    eng_lvl = input("Ingrese nivel de ingles: ")
    coder = {"id":coder_id,
             "Nombre": name,
             "Apellido": last_name,
             "Edad": age,
             "nvlIngles": eng_lvl
            } 
    return coder


def add_coder():
    selection = "1"
    num_coder = len(coder_list) + 1
    while selection == "1":
        coder_list[num_coder] = coder_data()
        print("Coder agregado.")
        print("Opciones\n(1) Agregar otro coder\n(Anything) Volver al menu")
        selection = input("Ingrese # de opcion:").strip()
        if selection == "1":
            num_coder+=1
        
def search_coder():
    
    if coder_list:
        coder_found = None
        print("Busqueda por id")
        search_id = getNumInput("Ingrese el id a buscar: ", int)
        for num_coder, coder in coder_list.items():
            if coder.get("id") == search_id:
                coder_found = num_coder
                break
            
        if coder_found:
            print(f"Coder encontrado: {coder_list[coder_found]}")
        else:
            print(f"No se encontro Coder con id {search_id}")
            
    else:
        print("No hay resgistro de coders")

def delete_coder():
    
    if coder_list:
        coder_found = None
        print("Busqueda por id")
        search_id = getNumInput("Ingrese el id a buscar: ", int)
        for num_coder, coder in coder_list.items():
            if coder.get("id") == search_id:
                coder_found = num_coder
                break
            
        if coder_found:
            print(f"Eliminando coder: {coder_found}")
            del coder_list[coder_found]
        else:
            print(f"No se encontro Coder con id {search_id}")
            
    else:
        print("No hay resgistro de coders")
        
def showlist():
    print("CODERS LIST")
    for coder in coder_list.items():
        print(f"Coder: {coder}")
    
    
    
def menu():
    selection = ""
    while selection !="4":
        print("MENU")
        print("Opciones:")
        print("(1) Agregar\n(2) Buscar\n(3) Eliminar\n(4) Salir")
        selection = input("Ingrese # de opcion:")
        if selection == "1":
            add_coder()
        elif selection == "2":
            search_coder()
        elif selection == "3":
            delete_coder()
        elif selection == "4":
            print("Saliendo...")
        else:
            print("Opcion no valida!")
            selection = ""
    
showlist()
menu()
showlist()