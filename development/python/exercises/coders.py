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

coder_list = {1: {'id': 1143, 
                  'Name': 'jen', 
                  'Lastname': 'rmz', 
                  'Age': 29, 
                  'EnglishLVL': 'b1'}, 
            2: {'id': 1234, 
                'Name': 'jesus', 
                'Lastname': 'vid', 
                'Age': 23, 
                'EnglishLVL': 'c1'}
            }

def coder_data():
    coder_id = getNumInput("Enter id: ", int)
    name = input("Enter name: ")
    last_name = input("Enter lastname: ")
    age = getNumInput("Enter age: ", int)
    eng_lvl = input("Enter englihs level: ")
    coder = {"id":coder_id,
             "Name": name,
             "Lastname": last_name,
             "Age": age,
             "EnglishLVL": eng_lvl
            } 
    return coder


def add_coder():
    selection = "1"
    num_coder = len(coder_list) + 1
    while selection == "1":
        coder_list[num_coder] = coder_data()
        print("Coder added.")
        print("Options\n(1) Add another coder\n(Anything) Back to menu")
        selection = input("Enter option #:").strip()
        if selection == "1":
            num_coder+=1
        
def search_coder():
    
    if coder_list:
        coder_found = None
        print("Search by id")
        search_id = getNumInput("Enter Id: ", int)
        for num_coder, coder in coder_list.items():
            if coder.get("id") == search_id:
                coder_found = num_coder
                break
            
        if coder_found:
            print(f"Coder found: {coder_list[coder_found]}")
        else:
            print(f"Coder whith id {search_id} wasn't found")
            
    else:
        print("There is no record of coders")

def delete_coder():
    
    if coder_list:
        coder_found = None
        print("Search by id")
        search_id = getNumInput("Enter Id: ", int)
        for num_coder, coder in coder_list.items():
            if coder.get("id") == search_id:
                coder_found = num_coder
                break
            
        if coder_found:
            print(f"Deleting coder: {coder_found}")
            del coder_list[coder_found]
        else:
            print(f"Coder whith id {search_id} wasn't found")
            
    else:
        print("There is no record of coders")
        
def showlist():
    print("CODERS LIST")
    for coder in coder_list.items():
        print(f"Coder: {coder}")
    
    
    
def menu():
    selection = ""
    while selection !="4":
        print("MENU")
        print("Options:")
        print("(1) Add\n(2) Search\n(3) Delete\n(4) Exit")
        selection = input("Enter option #:")
        if selection == "1":
            add_coder()
        elif selection == "2":
            search_coder()
        elif selection == "3":
            delete_coder()
        elif selection == "4":
            print("leaving...")
        else:
            print("Invalid option!")
            selection = ""
    
showlist()
menu()
showlist()