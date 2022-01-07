import calculator
import helper

helper.clear_console()
print("\n\n\tWelcome to the Calculator App\n\n")
user_response = input("\tPress any key to start the calculor, or type 'x' to exit: ").lower()
if user_response == 'x':
    exit()
else:
    calculator.start_calculator()