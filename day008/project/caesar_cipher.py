import cipher
import os

def encode_decode():
    direction = input("\033[0;32m\n\nType 'encode' to encrypt, type 'decode' to decrypt:\n\033[0;37m").lower()
    message = input("\033[0;32mType your message:\n\033[0;37m")
    shift = int(input("\033[0;32mType the shift number:\n\033[0;37m"))
    result = ""

    if direction == "encode":
        result = cipher.encrypt(message, shift)
        print(f"\033[0;32m\nHere's your {direction}d message: \033[0;37m{result}")
    elif direction == "decode":
        result = cipher.decrypt(message, shift)
        print(f"\033[0;32m\nHere's your {direction}d message: \033[0;37m{result}")
    else:
        print(f"\033[0;31m{direction} is an invalid command.")


os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1;32m\n╔═╗┌─┐┌─┐┌─┐┌─┐┬─┐  ╔═╗┬┌─┐┬ ┬┌─┐┬─┐\n║  ├─┤├┤ └─┐├─┤├┬┘  ║  │├─┘├─┤├┤ ├┬┘\n╚═╝┴ ┴└─┘└─┘┴ ┴┴└─  ╚═╝┴┴  ┴ ┴└─┘┴└─")
while True:
    encode_decode()
    another_message = input("\033[0;32m\nDo you have another message? Type 'y' for yes, type 'n' for no.\nAn invalid response will exit the application.\n").lower()
    if another_message == 'y':
       continue
    else:
        break;