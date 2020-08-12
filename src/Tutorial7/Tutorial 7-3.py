secret = 'python'
turns = 6
guesses = ''

print("Let's play Guess the Word")
print("You have", turns, "turns to guess the word!")
print(" _ " * 6)

while turns > 0:
    print()
    guess = str(input("Please guess the letter: "))
    guesses = guesses + guess
    turns = turns - 1
    for letter in secret:
        if letter in guesses:
            print('', letter, '', end='')
        else:
            print(' _ ', end='')
    if missed <= 0:
        break

print()
print("End of Game")
