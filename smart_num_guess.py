# rules
# set a timer for how many numbers they can guess correctly with clues
# max attempts per number is 7
# create function called tests failed for every guess.
import random
from math import sqrt

test_num: int = 500

# stores all numbers within the range 1 to test_num
one_to_num: list[int] = []
for num in range(1, test_num):
    one_to_num.append(num)

divisors: list[int] = []
not_divisible: list[int] = []

for num in one_to_num:  # can't we just do range here?
    if test_num % num == 0:
        divisors.append(num)
    else:
        not_divisible.append(num)


# gives hint the hidden number is between x and y
def create_range():
    low: int = random.randint(1, test_num - 1)
    buffer: int = random.randint(1, round(test_num + 1, -3))  # plus one eliminates round down
    high: int = random.randint(test_num, test_num + buffer)
    print(f'The hidden number is between {low} and {high} 🧐')


# reveals digit _3_ in number
def reveal_digit():
    string_hidden_num: str = str(test_num)
    max_idx: int = len(string_hidden_num) - 1
    random_idx: int = random.randrange(max_idx)
    print(f'The hidden number contains the digit {string_hidden_num[random_idx]} 🥲')


# gives hint on what the number is divisible by
def reveal_divisible_by():
    divisible_by = random.choice(divisors)
    print(f'The hidden number is divisible by {divisible_by} 🥹')


# gives hint on what the number is not divisible by
def reveal_not_divisible_by():
    sqrt_not_divisible_by: [int] = []
    sqrt_test_num = sqrt(test_num)
    for number in range(1, int(sqrt_test_num)):
        if int(test_num) % number != 0:
            sqrt_not_divisible_by.append(number)

    not_divisible_by = random.choice(sqrt_not_divisible_by)
    print(f'The hidden number is not divisible by {not_divisible_by} 😔')


def reveal_length():
    print(f'The hidden number has a length of {len(str(test_num))}. 👀')


def game_play():
    instructions: str = input(''' 
The hidden number is selected. @_@
You will get 7 hints. <_<
Beat the clock to get a new number and higher score. =_=
Click a key to begin. -> 
''')

    counter: int = 0
    reveal_divisible_by()
    while counter < 7:
        guess: int = int(input('Guess the hidden number >_>/ : '))

        if guess != test_num:
            counter += 1

            print(f'\nIncorrect. Current guesses {counter}/7.')
            match counter:
                case 1:
                    reveal_not_divisible_by()
                case 2:
                    create_range()
                case 3:
                    reveal_divisible_by()
                case 4:
                    reveal_not_divisible_by()
                case 5:
                    print('Uh oh. 5/7. Revealing digit. :[')
                    reveal_digit()
                case 6:
                    print('Last chance *_*')
                    reveal_length()
                case 7:
                    print(F'YOU LOSE. HIDDEN NUMBER WAS {test_num}!!!! :( O_o')

        else:
            print(f'You won! It was {test_num}!! :) [:')
            break


game_play()
#
# # when did this happen?????
# weight: int
# age: int
# weight, age = 10, 12
# print(age)
