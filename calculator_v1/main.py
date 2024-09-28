
from input_handler import get_number_input
from operations import add, subtract, multiply, divide, power, square_root, modulo
from validation import is_valid_operator
from error_handler import handle_division_error, handle_value_error
from memory_manager import save_to_memory, recall_memory, clear_memory, add_to_memory
from settings_manager import add_to_history, print_history, clear_history, change_decimal_places

def settings_menu():
    while True:
        print("\nSettings Menu:")
        print("1. Change decimal places")
        print("2. Show history")
        print("3. Clear history")
        print("4. Go back to calculator")

        choice = input("Select an option (1-4): ").strip()
        if choice == '1':
            change_decimal_places()
        elif choice == '2':
            print_history()
        elif choice == '3':
            clear_history()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def calculator():
    result = None
    while True:
        if result is None:
            try:
                user_input = input("Enter first number, 'exit' or 'settings': ").lower().strip()
                if user_input == 'exit':
                    print("Goodbye!")
                    break
                elif user_input == 'settings':
                    settings_menu()
                    continue
                elif user_input == 'mr':
                    num1 = recall_memory()
                else:
                    num1 = float(user_input)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue
        else:
            num1 = result
            print(f"Previous result: {num1}")

        operator = input("Enter operator (+, -, *, /, ^, %, √) or memory command (MS, MR, MC, M+): ").lower().strip()
        if operator == 'exit':
            print("Exiting...")
            break
        elif operator == 'settings':
            settings_menu()
            continue
        elif operator == 'ms':
            save_to_memory(num1)
            continue
        elif operator == 'mr':
            num2 = recall_memory()
            continue
        elif operator == 'mc':
            clear_memory()
            continue
        elif operator == 'm+':
            add_to_memory(float(input("Enter number to add to memory: ").strip()))
            continue
        elif operator == '√':
            result = square_root(num1)
            add_to_history(f"√{num1}", result)
            print(f"Result: {result:.2f}")
            continue

        if operator not in ['√', 'mr']:
            try:
                num2 = get_number_input("Enter second number: ")
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

        try:
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            elif operator == '^':
                result = power(num1, num2)
            elif operator == '%':
                result = modulo(num1, num2)
            else:
                print("Invalid operator.")
                continue
            add_to_history(f"{num1} {operator} {num2}", result)
            print(f"Result: {result:.2f}")
        except ZeroDivisionError:
            handle_division_error()
        except ValueError as ve:
            handle_value_error(str(ve))

if __name__ == "__main__":
    calculator()
