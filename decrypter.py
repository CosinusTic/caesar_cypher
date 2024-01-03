import enchant

def check_if_word_is_english(dictionary: dict, word: str) -> bool:
    for i in range(len(26)):
        if(dictionary.check(word)):
            return True

dictionary: dict = enchant.Dict("en_US")
encryption_file: any = open("encrypted.txt", "r")
decryption_file: any = open("decrypted.txt", "w")



file_content = encryption_file.readlines()
if len(file_content) > 0:
    print(file_content[0])


print(dictionary.check("Hello".lower()))

encryption_file.close()
decryption_file.close()