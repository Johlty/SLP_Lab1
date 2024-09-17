import math

memory = 0
history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def print_history():
    if history:
        print("History of calculations: ")
        for record in history:
            print(record)
    else:
        print("History is empty")

def calculator():
    global memory
    result = None
    while True:

        if result is None:
            try:
                user_input = input("Type first number or 'exit': ").lower()
                if user_input == 'exit':
                    print("bye-bye")
                    break
                elif user_input == 'mr':
                    num1 = memory
                    print(f"Value from memory: {num1}")
                else:
                    num1 = float(user_input)
            except ValueError:
                print("Eror: type a number")
                continue
        else:
            num1 = result
            print(f"Previous result: {num1}")

        
        operator = input("Enter the operator (+, -, *, /, ^, %, √, MS, MR, M+, MC, H) or 'restart': ").lower()

        if operator == 'restart':
            result = None  
            continue
        elif operator == 'exit':
            print("Exit")
            break
        elif operator == 'h':
            print_history()
            continue
        elif operator == 'mr':
            num2 = memory
            print(f"Value from memory: {num2}")
        elif operator == 'mc':
            memory = 0
            print("Memory is set to 0")
            continue
        elif operator == 'ms':
            memory = num1
            print(f"Value {num1} is saved in memory")
            continue
        elif operator == 'm+':
            try:
                add_value = float(input("type a number to add to the memory value: "))
                memory += add_value
                print(f"Now memory value is: {memory}")
            except ValueError:
                print("Eror: type a number")
            continue
        elif operator == '√':
            result = math.sqrt(num1)
            print(result)
            add_to_history(f"√{num1}", result)
            continue

        if operator not in ['√', 'mr']:
            try:
                user_input = input("Type second nuber: ").lower()
                if user_input == 'mr':
                    num2 = memory
                    print(f"Value in memory: {num2}")
                else:
                    num2 = float(user_input)
            except ValueError:
                print("Eror: type a number")
                continue
        else:
            num2 = None

    
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Eror: division by zero!")
                result = None
                continue
        elif operator == '^':
            result = num1 ** num2
        elif operator == '%':
            result = num1 % num2
        else:
            print("Wrong operator")
            result = None
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")
        add_to_history(f"{num1} {operator} {num2}", result)

calculator()
