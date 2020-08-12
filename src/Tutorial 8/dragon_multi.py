import random
import time


def display_intro():
    print("""You are in the Kingdom of Dragons. In front of you,
        you see two caves. In one cave, the dragon is friendly
        and will share his treasure with you. The other dragon
        is hungry and will eat you on sight.""")
    print()


def choose_cave():
    cave = ''  # local variable with empty string
    while cave != '1' and cave != '2' and cave != '3' and cave != '4':
        print('Which cave will you go into? (1, 2, 3 or 4)?')
        cave = input()
    return cave


def check_cave(cave_number):
    friendlyCave = random.randint(1, 4)
    if cave_number == str(friendlyCave):
        print('You approach the cave...')
        time.sleep(2)
        print('Gives you his treasure!')
    else:
        print('You approach the cave...')
        time.sleep(2)
        print('A large dragon jumps out in front of you! ')
        print('He opens his jaws and...')
        time.sleep(2)
        print('Gobbles you down!')


play_again = 'y'
while play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)
    print()
    play_again = str(input("Do you want to play again?(y/n)"))
