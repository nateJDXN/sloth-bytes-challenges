'''
August 26, 2025 Challenge


------ CHALLENGE ------

Create a function that determines whether a string is a valid hex code.

A hex code must begin with a pound key # and is exactly 6 characters in length.

Each character must be a digit from 0-9 or an alphabetic character from A-F. All 
alphabetic characters may be uppercase or lowercase. 


------ SOLUTION ------
I chose to convert the characters of the hex code to their ASCII values, which allowed me
to compare them to the bounds of the ASCII ranges 0-9, A-F, and a-f. A cleaner approach would
have been to directly compare all of the non-# characters to a string of valid characters, which
has the same time and space complexity as the solution below. 

Time Complexity: O(1)
Space Complexity: O(1)
'''

def validHexCode(code):

    # If code does not start with '#' automatically reject
    # If code is not 7 characters long automatically reject
    if code[0] != '#' or len(code) != 7:
        return False
    
    # Start from 1 index (code already starts with '#')
    for char in code[1:]:
        
        # convert char to its ascii value and compare to ascii values of 0-9, A-F, and a-f
        if ord(char) < 48 or (ord(char) > 57 and ord(char) < 65) or (ord(char) > 70 and ord(char) < 97) or ord(char) > 102:
            return False
    
    return True

def main():

    tests = {
        "#CD5C5C" : True,
        "#EAECEE" : True,
        "#eaecee" : True,
        "#CD5C58C" : False,
        "#CD5C5Z" : False,
        "#CD5C&C" : False,
        "CD5C5C" : False
    }

    for test in tests:
        if tests[test] != validHexCode(test):
            print("✗ - Fail\n" + test + " not characterized correctly.")
            continue
        print("✔ - Passed\n")

if __name__ == "__main__":
    main()