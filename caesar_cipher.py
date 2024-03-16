""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""
import os
import heapq
import string
import argparse
from functools import reduce
from collections import namedtuple, Counter
from frequencies import letter_frequencies

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
        Return: String of plaintext.

        This function takes in a string and a shift and outputs the 
        corresponding plaintext.
    """
    return "".join([char_mapping(char, shift, False) for char in ciphertext])

def get_dictionary(path):
    words = set()
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            words.add(line.rstrip("\n").upper())
    return words

def decrypt_freq_analysis(ciphertext, letter_freqs, dictionary):
    """ Parameters: ciphertext: String of ciphertext.
                    letter_freqs: Dictionary of letter frequencies. 
        Return: NamedTuple of plaintext and shift.

        This function takes in a string and outputs the corresponding
        plaintext and shift using frequency analysis.
    """
    letter_count = Counter([l for l in ciphertext.upper() if l.isalpha()])
    # Returns the most frequent letter from the cipher text
    most_freq_text = reduce(lambda k1, k2: k1 if letter_count[k1] > letter_count[k2] else k2, letter_count)
    heap = [(-value, key) for key, value in letter_freqs.items()]
    heapq.heapify(heap)
    while True:
        _, most_freq, = heapq.heappop(heap)
        shift = abs(ord(most_freq_text) - ord(most_freq))
        plaintext = decrypt(ciphertext, shift)

        table = str.maketrans("", "", string.punctuation)
        plaintext_iter = plaintext.upper().split()
        count = 0
        for word in plaintext_iter:
            if word in dictionary:
                count += 1
        if count / len(plaintext_iter) >= .5:
            break
        
    result_shift = namedtuple("result_shift", ["plaintext", "shift"])
    result = result_shift(plaintext, shift)
    return result


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
    path = "/usr/share/dict/words"
    dictionary = get_dictionary(path)
    result = decrypt_freq_analysis(open("input_to_decrypt", "r", encoding="utf-8").read(), letter_frequencies, dictionary)
    print(result.plaintext, result.shift)
    return
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
