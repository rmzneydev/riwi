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
            print(f"[ERROR] Invalid entry. Please enter data of type ({(data_type).__name__})")

    return value
