import enchant
import time

start_time: float = time.time()
dictionary: dict = enchant.Dict("en_US")
encryption_file: any = open("encrypted.txt", "r")
decryption_file: any = open("decrypted.txt", "w")
file_content = encryption_file.readlines()

def check_if_word_is_english(dictionary: enchant.Dict, word: str) -> bool:
    return dictionary.check(word)

for shift in range(26): # all possible ascii characters
    decrypted_trial: str = ""
    for word in file_content:
        for char in word:
            shifted_ascii: int = ord(char) + shift
            # Keep it confined to alphabet (uppercase & lowercase)
            if char.islower():
                if(shifted_ascii > ord("z")):
                    shifted_ascii -= 26
            elif char.isupper():
                if shifted_ascii > ord("Z"): 
                    shifted_ascii -= 26
            decrypted_trial += chr(shifted_ascii)

    words: list = decrypted_trial.split(":")
    final_decrypted: list = []

    # Check if each word is english and push it to array
    for decrypted in words: 
        if(check_if_word_is_english(dictionary, decrypted)):
            final_decrypted.append(decrypted)

    # Assume that decryption is correct if more than half of words are english words
    if(len(final_decrypted) >= len(words) / 2):
        end_time: float = time.time()
        execution_time: float = (end_time - start_time) * 1000
        print(f"{' '.join(words)}\n({shift} trials, execution time: {execution_time} ms)\n")
        decryption_file.write(f"{' '.join(words)}\n({shift} trials, execution time: {execution_time} ms)\n")


encryption_file.close()
decryption_file.close()