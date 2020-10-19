score = 0

print("Guess the animal!")


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct answer')
            score = score + 3 - score + 1
            still_guessing = False
        else:
            if attempt < score+1:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
    if attempt == score+1:
        print('The correct answer is ' + answer)


guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, 'polar bear')
guess = input('Mice are mammals. True or False? ')
check_guess(guess, 'True')
guess2 = input('Which is the fastest land animal? ')
check_guess(guess2, 'cheetah')
guess3 = input('Which is the largest animal? ')
check_guess(guess3, 'blue whale')
guess = input('Which one of these is a fish? \
A) Whale B) Dolphin C) Shark D) Squid. Type A, B, C, or D')
check_guess(guess, 'C')


print('Your score is ' + str(score))
