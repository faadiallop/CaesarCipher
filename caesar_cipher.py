""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""
import os
import argparse

def process_args():
    """ Parameters: None
        Return: The arguments from the argparse.Namespace object.

        This function takes in arguments from the user and returns them. 
    """
    parser = argparse.ArgumentParser(
        description="Runs caesar cipher on given text."
    )
    parser.add_argument(
        "text_or_file",
        type=str,
        help="A string or file to implement the cipher on."
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
    return args.text_or_file, args.shift, not args.decrypt

def char_mapping(char, shift, run_encryption):
    """ Parameters: char: String of a single character.
                    shift: Integer of the amount to shift alphabet by.
                    run_encryption: Boolean of whether to run encryption
                    or not.
        Return: The corresponding encrypted or decrypted character.
        
        This function maps between characters for the caesar cipher.
    """
    alphabet_size = 26
    if not char.isalpha():
        return char
    start_letter = "A" if char.isupper() else "a"
    right_shift = 1 if run_encryption else -1
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

def output(text, run_encryption, file):
    """ Parameters: text: String that is either some text or a
                    run_encryption: Boolean of whether the program 
                    encrypted or not.
                    file: Boolean of whether the text is from a file 
                    or not.
        Return: String to print to the screen.

        This functions returns the output of the users program call.
    """
    if file:
        file_name = "encryption_text" if run_encryption else "decryption_text"
        with open(file_name, "w+", encoding="utf-8") as f:
            f.write(text)
        return f"Output has been written to {file_name}!"
    else:
        return f"{'Ciphertext' if run_encryption else 'Plaintext'}: {text}"

def to_text(text_or_file):
    """ Parameters: text_or_file: String that is either some text or a
        file path.
        Return: String of the original text or the text within the file.

        This function outputs the text of a file or the string itself.
    """
    if os.path.exists(text_or_file):
        with open(text_or_file, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = text_or_file
    return text

def main():
    """ Parameters: None
        Return: None

        This function runs the code for the program.
    """
    text_or_file, shift, run_encrypt = process_args()
    text = to_text(text_or_file)
    output_text = encrypt(text, shift) if run_encrypt else decrypt(text, shift)
    print(output(output_text, run_encrypt, os.path.exists(text_or_file)))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program Interrupted!")
