""" Caesar Cipher

This program encrypts and decrypts text using the Caesar cipher.
"""

def user_input():
    text = input("Please type in your text: ")

    return text, None, None

def main():
    text, shift, encrypt = user_input()
    print(text)

if __name__ == "__main__":
    main()
