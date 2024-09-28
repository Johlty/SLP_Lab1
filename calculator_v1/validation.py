def is_valid_operator(operator):
    valid_operators = ['+', '-', '*', '/', '^', '√', '%', 'mr', 'ms', 'mc', 'm+', 'exit', 'restart', 'settings']
    if operator not in valid_operators:
        print("Invalid operator! Please enter a valid operator.")
        return False
    return True
