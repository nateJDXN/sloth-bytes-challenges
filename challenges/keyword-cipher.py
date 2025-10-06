'''
September 30, 2025 Challenge


------ CHALLENGE ------

A Keyword Cipher replaces each letter of a message with a letter from a shifted alphabet built using a keyword.

Start with the keyword.

Add the remaining letters of the alphabet (A–Z) in order, skipping any that already appeared in the keyword.

Example keyword: "KEYWORD"

Cipher alphabet: KEYWORDABCFGHIJLMNPQSTUVXZ

Encrypt by replacing each letter in the message with the letter at the same position in the cipher alphabet.

Plain alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Cipher alphabet: KEYWORDABCFGHIJLMNPQSTUVXZ

Write a function that takes a key and a message, and returns the encrypted message.


------ SOLUTION ------

Time Complexity: 
Space Complexity
'''

def keyword(keyword, message):

    # initialize arrays
    plain = [0] * 26
    cipher = [0] * 26

    #create alphabets
    for index, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
        plain[index] = char

def main():

    if keyword_cipher("keyword", "abchij") == "keyabc":
        print("✔ - Passed\n")
    else:
    
    Output = "keyabc"

    keyword_cipher("purplepineapple", "abc")
    output = "pur"

    keyword_cipher("mubashir", "edabit")
    output = "samucq"

    keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "abc")
    Output = "eta"

    keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "xyz")
    Output = "qxz"

    keyword_cipher("etaoinshrdlucmfwypvbgkjqxz", "aeiou")
    Output = "eirfg"

    for test in tests:
        if tests[test] != validHexCode(test):
            print("✗ - Fail\n" + test + " not characterized correctly.")
            continue
        print("✔ - Passed\n")

if __name__ == "__main__":
    main()
