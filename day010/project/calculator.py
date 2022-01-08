import calc
import helper

operations = {
    "+" : calc.add,
    "-" : calc.subtract,
    "*" : calc.multiply,
    "/" : calc.divide
}

def is_valid_operation(operation_to_check):
    for operation in operations:
        if operation_to_check == operation:
            return True
    return False

def get_number(message):
    number = 0
    while True:
        user_input = input("{}".format(message))
        try:
            number = float(user_input)
            if number.is_integer():
                number = int(number)
            return number
        except ValueError:
            print("\tThat is not a valid number. Try again.")

def get_operation():
    is_valid = False
    operation = ""
    while not is_valid:
        operation = input("\tPick an operation: ")
        is_valid = is_valid_operation(operation)
        if not is_valid:
            print("\tInvalid Operation. Pick an operation from the list above.")
    
    return operation

def display_operations():
    for operation in operations:
        print(f"\t{operation}")

def start_calculator():
    helper.clear_console()
    helper.print_art("logo.txt")
    print("\n\n")
    first_number = get_number("\tWhat is the first number? ")
    display_operations()
    is_new_calculation = False
    while not is_new_calculation: 
        operation = get_operation()
        second_number = get_number("\tWhat is the next number? ")
        result = operations[operation](first_number, second_number)
        if isinstance(result, float) and result % 1 == 0:
            result = int(result)
        print(f"\t{first_number} {operation} {second_number} = {result}")
        user_response = input(f"\tType 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type any key to exit calculator: ").lower()    
        if user_response == 'n':
            is_new_calculation = True
            start_calculator()
        elif user_response == 'y':
            first_number = result
            continue
        else:
            print("\tThanks for using the calculator.\n\n")
            return