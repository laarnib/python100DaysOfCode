import cipher

def encode_decode():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    result = ""

    if direction == "encode":
        result = cipher.encrypt(message, shift)
        print(f"\nHere's your encoded message: {result}")
    elif direction == "decode":
        result = cipher.decrypt(message, shift)
        print(f"\nHere's your decoded message: {result}")
    else:
        print("That is an invalid command.")


while True:
    encode_decode()
    another_message = input("\nDo you have another message? Type 'y' for yes, type 'n' for no.\nAn invalid response will exit the application.\n").lower()
    if another_message == 'y':
       continue
    else:
        break;