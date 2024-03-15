""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""
# You can use the data structures in collections for functional programming
# import collections

def check_int(string, one_or_zero):
    """ Parameters: string: String to check.
                    one_or_zero: Boolean if string needs to be a 1 or 0.

        Return: Boolean if string is an integer

        This function returns True or False if the string is an int.
    """
    try:
        int(string)
    except ValueError:
        if one_or_zero:
            print("You did not type in one or zero")
        else:
            print("You did not enter an integer!")
        return False
    return True

def user_input():
    """ Parameters: None
        Return: 3-tuple of the input text, shift for caesar cipher and
        whether to encrypt or decrypt the text.

        This function reads in input from the user and returns those
        values.
    """
    text = input("Please type in your text: ")
    shift = input("Please type in your shift: ")
    while not check_int(shift, False):
        shift = input("Please type in your shift: ")
    shift = int(shift)
    encryption = input("Please type in 1 for encryption and 0 for decryption: ")
    while not check_int(encryption, True) and (encryption != "1" or encryption != "0"):
        encryption = input("Please type in 1 for encryption and 0 for decryption: ")
    encryption = bool(int(encryption))
    return text, shift, encryption

def encrypt(plaintext, shift):
    """ Parameters: plaintext: String of plaintext.
                    shift: Integer of the amount to shift alphabet by.
        Return: String of ciphertext.

        This function takes in a string and a shift and outputs the 
        corresponding ciphertext.
    """
    def to_cipher_char(char, shift):
        alphabet_size = 26
        if not char.isalpha():
            return char
        start_letter = "A" if char.isupper() else "a"
        return chr((ord(char) - ord(start_letter) + shift) %
                    alphabet_size + ord(start_letter))
    return "".join([to_cipher_char(char, shift) for char in plaintext])

def decrypt(ciphertext, shift):
    """ Parameters: ciphertext: String of ciphertext.
                    shift: Integer of the amount to shift alphabet by.
        Return: String of ciphertext.

        This function takes in a string and a shift and outputs the 
        corresponding ciphertext.
    """
    def to_plain_char(char, shift):
        alphabet_size = 26
        if not char.isalpha():
            return char
        start_letter = "A" if char.isupper() else "a"
        return chr((ord(char) - ord(start_letter) - shift) % alphabet_size + ord(start_letter))
    return "".join([to_plain_char(char, shift) for char in ciphertext])

def main():
    """ Parameters: None
        Return: None

        This function runs the code for the program.
    """
    text, shift, encryption = user_input()
    if encryption:
        ciphertext = encrypt(text, shift)
        print(f"Ciphertext: {ciphertext}")
    else:
        plaintext = decrypt(text, shift)
        print(f"Plaintext: {plaintext}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program Interrupted!")
