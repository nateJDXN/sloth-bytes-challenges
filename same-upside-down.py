'''
August 19, 2025 Challenge


------ CHALLENGE ------

The number 6090609 has a special property: if you turn the number upside down (imagine rotating 
your screen 180 degrees), you get 6090609 again.

Write a function that takes a string on the digits 0, 6, 9 and returns true if the number is 
the same upside down or false otherwise.


------ SOLUTION ------

The algorithm uses two pointers starting from opposite ends of the string and moving toward 
the center. For each pair of digits, it checks if the left digit equals the upside-down version 
of the right digit using a mapping dictionary. 

For odd-length strings, there's a special check ensuring the middle digit is 0 (since only 0 
looks the same upside down when in the center).

Time Complexity: O(n)
Space Complexity O(1)
'''


def sameUpsideDown(num):

    # base case
    if num == "0" or num == "":
        return True

    # create dict to stored flipped values
    dict = {
        "6" : "9",
        "9" : "6",
        "0" : "0"
    }

    # create two pointers
    p1 = 0
    p2 = len(num) - 1

    # pointer 1 moves forward, pointer 2 moves backward
    while p1 < p2:
        # pointer 1 should be the flipped value of pointer 2
        if num[p1] != dict[num[p2]]:
            # print("Expected " + dict[num[p2]] + ", but got " + num[p2])
            return False
        
        # increment pointers
        p1 += 1
        p2 -= 1

    # middle value reached, middle value must be 0
    if p1 == p2 and num[p1] != '0':
        # print("Expected 0, but got " + num[p1])
        return False
    
    return True

def main():

    tests = {
        "6090609" : "True",
        "9669" : False,
        "6" : False,
        "9" : False,
        "0" : True,
        "6090609" : True,
        "60906096090609" : True,
        "966909669" : False,
        "96666660999999": False
    }

    for test in tests:
        if tests[test] != sameUpsideDown(test):
            print("✗ - Fail\n" + test + " is not the same upside down.")
            continue
        print("✔ - Passed\n")

if __name__ == "__main__":
    main()