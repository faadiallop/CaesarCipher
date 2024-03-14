""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""

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
    encrypt = input("Please type in 1 for encryption and 0 for decryption: ")
    while not check_int(encrypt, True) and (encrypt != "1" or encrypt != "0"):
        encrypt = input("Please type in 1 for encryption and 0 for decryption: ")
    encrypt = bool(int(encrypt))
    return text, shift, encrypt

def main():
    """ Parameters: None
        Return: None

        This function runs the code for the program.
    """
    text, shift, encrypt = user_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program Interrupted!")
