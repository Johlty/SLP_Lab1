history = []  
decimal_places = 2  
def add_to_history(expression, result):
   
    history.append(f"{expression} = {result:.{decimal_places}f}")

def print_history():
   
    if history:
        print("History of calculations:")
        for record in history:
            print(record)
    else:
        print("History is empty.")

def clear_history():
    
    global history
    history = []
    print("History cleared.")

def change_decimal_places():
    
    global decimal_places
    while True:
        try:
           
            new_decimal_places = int(input("Enter number of decimal places (0-10): ").strip())
            if 0 <= new_decimal_places <= 10:
                decimal_places = new_decimal_places
                print(f"Decimal places set to {decimal_places}")
                break
            else:
                print("Error: Please enter a number between 0 and 10.")
        except ValueError:
            print("Error: Please enter a valid number.")
