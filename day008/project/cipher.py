#Encrypts a message using caesar cipher
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                # get the decimal equivalent of the letter
                # subtract that by 65 then add the shift number.
                # Get the remainder of the sum divided by 26.
                # Add 65 to the remainder and convert the decimal
                # back to it's character equivalent
                dec_equivalent = ord(char)
                new_letter = chr((((dec_equivalent - 65) + shift) % 26) + 65)
                encrypted_message += new_letter
            else:
                # get the decimal equivalent of the letter
                # subtract that by 97 then add the shift number.
                # Get the remainder of the sum divided by 26.
                # Add 97 to the remainder and convert the decimal
                # back to it's character equivalent
                dec_equivalent = ord(char)
                new_letter = chr((((dec_equivalent - 97) + shift) % 26) + 97)
                encrypted_message += new_letter
        else:
            encrypted_message += char
    
    return encrypted_message

#Decrypts an encrypted message using caesar cipher
def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                # get the decimal equivalent of the letter
                # subtract that by 65 then add the shift number.
                # Get the remainder of the sum divided 26.
                # Add 65 to the remainder and convert the decimal
                # back to it's character equivalent
                dec_equivalent = ord(char)
                new_letter = chr((((dec_equivalent - 65) - shift) % 26) + 65)
                decrypted_message += new_letter
            else:
                # get the decimal equivalent of the letter
                # subtract that by 97 then add the shift number.
                # Get the remainder of the sum divided 26.
                # Add 97 to the remainder and convert the decimal
                # back to it's character equivalent
                dec_equivalent = ord(char)
                new_letter = chr((((dec_equivalent - 97) - shift) % 26) + 97)
                decrypted_message += new_letter
        else:
            decrypted_message += char
    
    return decrypted_message