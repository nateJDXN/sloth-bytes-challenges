'''
September 3, 2025 Challenge


------ CHALLENGE ------

Given a positive integer, return its corresponding column title displayed in Excel sheets.

For example:

1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
...


------ SOLUTION ------



26 -> Z
27 -> AA
...
52 -> 26 * 2 -> AZ
53 -> 26 * 3 - 25 BA


ASCII
1 -> 64 + num = 65 = A
2 -> 64 + num = 66 = B
...
27 -> int(27/26) = 1, 27 % 26 = 1 -> 1 1 = AA



Time Complexity: 
Space Complexity:
'''

def convert_to_title(num):

    num1 = int(num/26)    # get leading digit (amount of alphabet rotations)
    num2 = num % 26       # get remainder (alphabet character)

    char1 = chr(64 + num1)
    char2 = chr(64 + num2)

    result = char1 + char2
    result = result.replace("@", "")

    return result


def main():

    tests = {
        1 : "A",
        18 : "R",
        28 : "AB",
        52 : "AZ",
        701 : "ZY",
        229704 : "MATT",
        209380622941 : "ZATOICHI"
    }

    for test in tests:
        result = convert_to_title(test)
        if tests[test] != convert_to_title(test):
            print("✗ - Fail\nGot " + result + " but expected " + tests[test] + ".")
            continue
        print("✔ - Passed\n")

if __name__ == "__main__":
    main()