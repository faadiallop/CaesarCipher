""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""
import argparse

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

def process_args():
    """ Parameters: None
        Return: argparse.Namespace object with the arguments. 

        This function takes in arguments from the user and returns them. 
    """
    parser = argparse.ArgumentParser(
        description="Runs caesar cipher on given text."
    )
    parser.add_argument(
        "text",
        type=str,
        help="A string to implement the cipher on."
    )

    def raise_(exception):
        """Raises the given exception. Used in a lambda function."""
        raise exception

    parser.add_argument(
        "shift",
        type=lambda s: int(s) if 0 <= int(s) < 26
                       else raise_(ValueError("Invalid shift value.")),
        help=("An integer of the amount to shift alphabet by. "
              "This value must be in the range [0...26)")
    )
    parser.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help=("An boolean of whether to decrypt or not. "
              "This is set to False by default.")
    )
    args = parser.parse_args()
    return args.text, args.shift, not args.decrypt

def char_mapping(char, shift, encryption):
    """ Parameters: char: String of a single character.
                    shift: Integer of the amount to shift alphabet by.
        Return: The corresponding encrypted or decrypted character.
        
        This function maps between characters for the caesar cipher.
    """
    alphabet_size = 26
    if not char.isalpha():
        return char
    start_letter = "A" if char.isupper() else "a"
    right_shift = 1 if encryption else -1
    return chr((ord(char) - ord(start_letter) + (shift * right_shift)) %
                alphabet_size + ord(start_letter))

def encrypt(plaintext, shift):
    """ Parameters: plaintext: String of plaintext.
                    shift: Integer of the amount to shift alphabet by.
        Return: String of ciphertext.

        This function takes in a string and a shift and outputs the 
        corresponding ciphertext.
    """
    return "".join([char_mapping(char, shift, True) for char in plaintext])

def decrypt(ciphertext, shift):
    """ Parameters: ciphertext: String of ciphertext.
                    shift: Integer of the amount to shift alphabet by.
        Return: String of ciphertext.

        This function takes in a string and a shift and outputs the 
        corresponding ciphertext.
    """
    return "".join([char_mapping(char, shift, False) for char in ciphertext])

def output(text, encryption):
    """ Parameters: text: String of text to output.
                    encrytion: Boolean of whether the program encrypted 
                    or not.
        Return: None

        This functions returns the output of the users program call.
    """
    return f"{'Ciphertext:' if encryption else 'Plaintext:'} {text}"

def main():
    """ Parameters: None
        Return: None

        This function runs the code for the program.
    """
    text, shift, run_encrypt = process_args()
    output_text = encrypt(text, shift) if run_encrypt else decrypt(text, shift)
    print(output(output_text, run_encrypt))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program Interrupted!")
