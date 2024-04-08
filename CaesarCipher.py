# Caesar Cipher Program

def main():
    text = input("Enter a text to be encrypted: ")

    encryptedText = encryptCaesarCipher(text)
    decryptedText = decrpytCaesarCipher(encryptedText)
    
    print("\nEncrypted Text: ", encryptedText)
    print("\nDecrypted Text: ", decryptedText)

# encrypts text
def encryptCaesarCipher(text):
    translation_table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"
    )
    return text.translate(translation_table)

# decrypts text
def decrpytCaesarCipher(text):
    translation_table = str.maketrans(
        "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC",
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    )
    return text.translate(translation_table)


if __name__ == "__main__":
    main()