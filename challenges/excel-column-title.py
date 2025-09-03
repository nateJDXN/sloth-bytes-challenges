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


Time Complexity: 
Space Complexity:
'''

def convert_to_title(num):
    return

def main():

    tests = {
        "1" : "A",
        "18" : "R",
        "28" : "AB",
        "52" : "AZ",
        "701" : "ZY",
        "229704" : "MATT",
        "209380622941" : "ZATOICHI",
    }

    for test in tests:
        result = convert_to_title(test)
        if tests[test] != convert_to_title(test):
            print("✗ - Fail\nGot " + result + " but expected" + tests[test] + ".")
            continue
        print("✔ - Passed\n")

if __name__ == "__main__":
    main()