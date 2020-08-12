alphabet = 'abcdefghijklmnopqrstuvwxyz'  # This will store the letters of the alphabet
secret = 'python'  # This is the secret word
turns = len(secret)  # This will make the no. of turns equal to the length of the secret word
guesses = ''  # This stores the guessed characters
missed = 0  # This is a counter for the number of letters that are still missing
found = 0  # This will store the index of the letter if found

print("Let's play Guess the Word")
print("You have ", turns, "turns to guess the word!")  # This statement prints out the number of turns at the begining
print(" _ " * 11)  # This displays the dashes which should be replaced

while turns > 0:
    missed = len(secret)  # This will initialise the no. of missed letter to 11
    found = 0
    verify = 0

    print()
    guess = str(input("Please guess a letter: "))  # This prompts the user and gets the guessed letter
    guesses = guesses + guess.lower()  # This concatonates all the guessed letters together
    for letter in guess.lower():
        verify = alphabet.find(letter)
        if verify >= 0:
            guesses = guesses + guess.lower()  # This concatonates all the guessed letters together
            for letter in secret:  # This will print the output
                if letter in guesses:  # A letter will be printed if the correct letter was guessed
                    print('', letter, '', end='')
                    missed = missed - 1  # This will count the number of letters that are still missing
                else:  # A dash will be printed if the letter was not guessed
                    print(' _ ', end='')

            for letter in guess.lower():  # if a wrong letter is entered, the no. of turns will be deducted
                found = secret.find(letter)
                if found < 0:
                    turns = turns - 1
                    print("You have", turns,
                          "turns to guess the word!")  # This statements will print the no. of remaining turns
                    continue
                else:
                    break

            if missed == 0:
                break
        elif verify < 0:
            print("A false character has been entered into guess")  # If a false character is entered, this will be printed.

print()
print("End of Game")  # This statement will be printed at the end of the game
print("The secret word is: 'westminster'")
