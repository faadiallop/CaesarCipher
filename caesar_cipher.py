""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""

def check_int(string, one_or_zero):
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
    text, shift, encrypt = user_input()
    print(text, type(shift), shift, type(encrypt), encrypt)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Program Interrupted!")
