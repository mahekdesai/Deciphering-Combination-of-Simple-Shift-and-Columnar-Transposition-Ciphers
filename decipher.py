#MAHEK DESAI
#COMP424
#ASSIGNMENT 1

#All print statements except the final one are commented to make the process speedy.

import os
from collections import defaultdict

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#ref: https://www.w3schools.com/python/python_file_open.asp
def read_dictionary(list_of_words):
    os.chdir("C:\\Users\\md494536\\Desktop\\COMP424\\CIPHER")
    dictionary_path = "Dictionary.txt"

    try:
        with open(dictionary_path, 'r') as file:
            for line in file:
                list_of_words.append(line.strip().upper())
        # print("LIST OF WORDS IN DICTIONARY")
        # print(list_of_words)
    except FileNotFoundError:
        print("FILE NOT FOUND")
        exit(-1)

def word_exists(list_of_words, word_to_search):
    return word_to_search in list_of_words

def word_count(s):
    count = 1
    for i in range(len(s) - 1):
        if s[i] == ' ' and s[i + 1] != ' ':
            count += 1
    return count

#ref: https://www.geeksforgeeks.org/columnar-transposition-cipher/
def columnar_transposition_decipher(cipher_text, key):
    key_len = len(key)
    remainder = len(cipher_text) % key_len
    flag = remainder
    row_ct = -(-len(cipher_text) // key_len)
    arranged_keys = arrange_key(key)
    grid = [['' for _ in range(key_len)] for _ in range(row_ct)]
    new_str = ""
    for col in range(key_len):
        for int_key in arranged_keys:
            if int_key == col:
                if flag <= key_len and flag != 0:
                    for i in range(key_len - 1, remainder - 1, -1):
                        if arranged_keys[i] == col:
                            new_str = cipher_text[:row_ct - 1] + 'X'
                            flag += 1
                            cipher_text = cipher_text[row_ct - 1:]

                if new_str == "":
                    new_str = cipher_text[:row_ct]
                    cipher_text = cipher_text[row_ct:]

                for row in range(row_ct):
                    grid[row][col] = new_str[row]
                new_str = ""

    message = ""
    for r in range(row_ct):
        for int_key in arranged_keys:
            message += grid[r][int_key]
    # print(message)
    return message

#ref: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
def simple_shift_decipher(shift, cipher_text):
    plain_text = ""
    for ch in cipher_text:
        alpha_in = ALPHABETS.index(ch)
        if (alpha_in - shift) < 0:
            remainder = abs(alpha_in - shift) % 26
            plain_text += ALPHABETS[26 - remainder]
        else:
            plain_text += ALPHABETS[alpha_in - shift]
    return plain_text

#ref: https://stackoverflow.com/questions/53380551/python-caesar-cipher-program-with-no-key
def no_of_shifts(ordered_chars):
    potential_shifts = set()
    common_chars = ['E', 'A', 'I', 'R', 'O', 'T', 'N', 'S'] #ref: https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    
    for ordered_char in ordered_chars:
        index = ALPHABETS.index(ordered_char)
        finished = False
        shift = 1
        
        while not finished:
            if (index - shift) < 0:
                remainder = abs(index - shift) % 26
                shifted_character = ALPHABETS[26 - remainder]
            else:
                shifted_character = ALPHABETS[index - shift]
            
            for ch in common_chars:
                if shifted_character == ch:
                    potential_shifts.add(shift)
                    finished = True
            shift += 1
    # print("POTENTIAL NUMBER OF SHIFTS FOR SIMPLE SHIFT SUBSTITUTION")
    # print(potential_shifts)
    return potential_shifts

#ref: https://stackoverflow.com/questions/32877531/splitting-strings-in-python-without-split
def split_string(new_string, list_of_words):
    for i in range(1, len(new_string) + 1):
        prefix = new_string[:i]
        if word_exists(list_of_words, prefix):
            suffix = new_string[i:]
            split_suffix = split_string(suffix, list_of_words)
            if split_suffix is not None:
                return prefix + " " + split_suffix
            else:
                return suffix
    return None

#ref: https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
def freq_chars(cipher_text):
    freq = defaultdict(int)
    
    for alphabet in ALPHABETS:
        count = sum(1 for ch in cipher_text if ch == alphabet)
        if count > 3:
            freq[alphabet] = count
    # print('MOST FREQUENT CHARACTERS : RESPECTIVE FREQUENCIES')
    # print(freq, count)
    return freq

#ref: https://stackoverflow.com/questions/4131123/finding-the-most-frequent-character-in-a-string
def odered_freq_chars(freq):
    potential_keys = []
    max_value = max(freq.values())
    
    for max_count in range(max_value, -1, -1):
        for key, value in freq.items():
            if value == max_count:
                potential_keys.append(key)
    # print("DESCENDING ORDERED CHARS WRT RESPECTIVE FREQUENCIES")
    # print(potential_keys)
    return potential_keys

def combine(list_of_words, c):
    res = []
    for s in list_of_words:
        for i in range(len(s) + 1):
            ps = s[:i] + c + s[i:]
            res.append(ps)
    return res

#ref: https://stackoverflow.com/questions/33312532/generate-all-permutations-of-a-string-in-python-without-using-itertools
def permute(s):
    res = []
    if len(s) == 1:
        res.append(s)
    elif len(s) > 1:
        last_char = s[-1] 
        rest = s[:-1]
        res = combine(permute(rest), last_char)
    return res

def arrange_key(key):
    potential_keys = sorted(key)
    num = [potential_keys.index(c) for c in key]
    return num

def main():
    cipher_text = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"
    list_of_words = []
    read_dictionary(list_of_words)
    freq = freq_chars(cipher_text)
    ordered_chars = odered_freq_chars(freq)
    potential_shifts = no_of_shifts(ordered_chars)
    potential_strings = set()

    for shift in potential_shifts:
        potential_strings.add(simple_shift_decipher(shift, cipher_text))
    # print("POTENTIAL STRINGS AFTER SIMPLE SHIFT DECRYPTION")
    # print(potential_strings)

    potential_keys = []
    for i in range(8):
        for potential_key in permute(ALPHABETS[:i]):
            potential_keys.append(potential_key)
    # print("POTENTIAL KEYS FOR COLUMNAR TRANSPOSITION CIPHER")
    # print(potential_keys)
    # print("POTENTIAL DECIPHERED TEXTS AFTER COLUMNAR TRANSPOSITION WRT PTENTIAL SHIFTS")
    # print('DECIPHERED TEXT AFTER SPLITTING')
    for candidiate_string in potential_strings:
        for candidate_key in potential_keys:
            deciphred_text = columnar_transposition_decipher(candidiate_string, candidate_key)
            # print(candidate_key, candidiate_string, deciphred_text)
            split_message = split_string(deciphred_text, list_of_words)
            # print(split_message)
            if split_message is not None and word_count(split_message) > 5:
                print("FINAL DECIPHERED TEXT")
                print(split_message)

if __name__ == "__main__":
    main()
