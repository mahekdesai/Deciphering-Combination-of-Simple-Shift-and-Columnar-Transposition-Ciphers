## Overview

Welcome to the repository for my COMP424 Assignment 1 project! This project focuses on deciphering a combination of simple shift and columnar transposition ciphers applied to a given ciphertext. The decryption process is designed to determine if a student is prepared for a test based on selected features.

## Project Structure

### Files

1. **decipher.py**: The main Python script containing the implementation of the deciphering process.
   
2. **dictionary.txt**: A text file containing a list of words used for reference in the deciphering process.

### How to Run

1. Ensure that you have Python installed on your system.
   
2. Clone this repository to your local machine.

3. Navigate to the project directory.

4. Run the Python script.

5. The final deciphered text will be displayed if the criteria for test preparedness are met.

## Project Details

### Cryptographic Techniques Used

- **Simple Shift Cipher Decryption**: Deciphers the initial text using a simple shift cipher with a variable number of shifts.

- **Columnar Transposition Cipher Decryption**: Applies decryption using a columnar transposition cipher with multiple potential keys.

### Algorithmic Approach

1. **Read Dictionary**: Loads a list of words from the provided "Dictionary.txt" file.

2. **Frequency Analysis**: Identifies the most frequently occurring characters in the ciphertext to determine potential shifts for the simple shift cipher.

3. **Deciphering Attempts**: Conducts deciphering attempts using potential shifts and keys for both the simple shift and columnar transposition ciphers.

4. **Word Splitting**: Applies word splitting techniques to evaluate the validity of potential deciphered texts.

5. **Output**: Displays the final deciphered text that meets the specified criteria for test preparedness.

## Note

- The script is designed to be versatile, and you can modify the ciphertext and the list of common characters according to your specific use case.

- Feel free to explore and enhance the project based on your cryptographic interests and requirements!

Happy deciphering! 🕵️‍♂️🔐
