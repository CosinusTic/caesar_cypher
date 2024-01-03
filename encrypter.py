user_input: str = input("Please enter a word or sentence to encrypt: ")
user_key: str = input("Please enter your key (must be an int): ")
encryption_file: any = open("encrypted.txt", "w")
def caesar_encrypt(entry: str, key: int) -> str:
    encrypted: str = ""
    for char in entry:
        ascii_char: int = ord(char)
        ascii_char += key
        encrypted += chr(ascii_char)

    return encrypted



if(user_key.isnumeric == False):
    print("Please enter a numeric value (integer) for your encryption key")
else:
    print("Encrypted output: " + caesar_encrypt(user_input, int(user_key)))
    encryption_file.write(caesar_encrypt(user_input, int(user_key)))

encryption_file.close()