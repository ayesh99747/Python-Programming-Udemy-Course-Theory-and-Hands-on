secret = 'computer'
turns = len(secret)
guesses = ''

print("Let's play Guess the Word")
print("You have", turns, "turns to guess the word!")
print(" _ " * 6)

while turns > 0:
    missed = 6
    found = 0
    print()
    guess = str(input("Please guess the letter: "))
    guesses = guesses + guess.lower()

    for letter in secret:
        if letter in guesses:
            print('', letter, '', end='')
            missed = missed - 1
        else:
            print(' _ ', end='')

    for letter in guess.lower():
        found = secret.find(letter)
        if found < 0:
            turns = turns - 1
            print()
            print("You have", turns, "turns to guess the word!")
            continue
        else:
            break

    if missed == 0:
        break

print()
print("End of Game")
