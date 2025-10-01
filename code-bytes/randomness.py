#shuffling numbers in an array
import random
deck = [1,2,3,4]
#Yep the random package has a shuffle method.
random.shuffle(deck)


# no matter how many times you run it, it will always output [2, 1, 5, 4, 4]
random.seed(42)  
print([random.randint(1, 10) for _ in range(5)])

# Fisher-Yates Shuffle
def shuffle(numbers: list[int]) -> list[int]:
    for i in range(len(numbers) - 1, 0, -1):
        #IMPORTANT PART!
        j = random.randint(0, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers