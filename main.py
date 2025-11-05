import sys
import os

TARGET_HASH = 1397
MULTIPLIER = 31
MODULUS = 10007

msg1 = """

 Quiz 3

 Date: 11/5/2025 (Wednesday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""

msg2 = """

 Quiz 3

 Date: 11/3/2025 (Monday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""

msg3 = """

 Quiz 3

 Date: 11/10/2025 (Monday), during Class, for 20 minutes. 

 Topics:

 Classes: Getters and Setters, Static Methods, Class Methods, Inheritance, Operator Overloading

 Files: Reading, Writing, pathlib Module, JSON Files

 Exceptions 

 Cryptography: Hashing, Encoding/Decoding

 Lectures:

 11 - 18

"""

def quiz_hash(message):
    hash_value = 0

    for i, char in enumerate(message):
        char_ascii = ord(char)
        
        hash_value = (hash_value * MULTIPLIER + char_ascii) % MODULUS
            
        
    return hash_value

def solve_quiz_hash():
    messages = {
        "msg1": msg1,
        "msg2": msg2,
        "msg3": msg3
    }
    
    matching_message = None
    
    for name, message in messages.items():
        computed_hash = quiz_hash(message)
        
        print(f"Hash for {name}: {computed_hash}")
        
        if computed_hash == TARGET_HASH:
            matching_message = name

    if matching_message:
        print(f"The correct message is {matching_message}")
        
        print("\nContent of the correct message:\n")
        print(messages[matching_message])



solve_quiz_hash()