import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')

word = random.choice(someWords)
chances = len(word) + 2

if __name__ == '__main__':
    print('Hangman Game: Guess the word!')
    print('HINT: The word is name of a fruit')
    
    userAnswer = []
    fruit = []
    for i in word:
        fruit.append('_')

    while chances > 0:
        print(f'\nYou have {chances} chances to guess')
        
        for i in fruit:
            print(i , ' ', end='')
        print('\n')
        
        userAnswer = (input(f'Enter a letter: '))
        chances -= 1
        
        for i in range(len(word)):
            if userAnswer == word[i]:
                fruit[i] = userAnswer

        print(word, fruit, userAnswer)

        space = len(word)
        for i in word:
            if i != '_':
                space -= 1
        
        if space == 0:
            print('You WIN!')
            break

    if chances == 0:
        print('You LOSE!')