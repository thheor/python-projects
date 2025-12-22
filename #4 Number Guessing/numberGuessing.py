import random

print('Number Guessing Game')

lower = int(input('Enter the lower bound number: '))
upper = int(input('Enter the upper bound number: '))

chance = int(input('Enter answer\'s chances: '))

print(f'You have {chance} chances to guess a number between {lower} and {upper}. Let\'s start!\n')

num = random.randint(lower, upper)

attempts = 0

while attempts < chance:
    answer = int(input('Enter a number: '))

    if answer < num:
        attempts += 1
        print('Too Low!')
    elif answer > num:
        attempts += 1
        print('Too High!')
    else:
        print('You Right!')
        break
print(f'The number is {num}')
