'''
Basic front-end for the game engine.

Can be invoked as is, or with 4 integer arguments for the answer.
'''

import sys
import engine

MAX_ROUND = 10

def take_input(round_num):
    '''Return a list representing user input.  Tries common delimeters.

    `round_num` is the round of the game (to display to the user).
    Uses `raw_input` - caveats here about that.'''

    # tries half-heartedly until input is okay
    OK = False
    while not OK:
        guess = raw_input("Round %d: " % int(round_num))
        if len(guess.split(' ')) == engine.SPACES:
            guess = [int(i) for i in guess.split(' ')]
            OK = True
        elif len(guess.split(',')) == engine.SPACES:
            guess = [int(i) for i in guess.split(',')]
            OK = True
        elif len(guess.split(', ')) == engine.SPACES:
            guess = [int(i) for i in guess.split(', ')]
            OK = True

    return list(guess)

def make_or_get_answer(args=None):
    '''Either takes/returns a list as an answer or gets a random one'''

    if args and len(args) == engine.SPACES:
        answer = list(int(i) for i in args)
        print("Using prompted answer")
    else:
        answer = engine.make_answer()

    return answer

def main():
    '''Make a game happen!  Run me in a console!!'''

    answer = make_or_get_answer(sys.argv[1:])

    print("Guess %d numbers from 1 - %d" % (engine.SPACES, engine.COLORS))
    for round_num in range(MAX_ROUND):
        guess = take_input(round_num + 1)
        pegs = engine.check_guess(answer, guess)
        if pegs[0] == 4:
            print("You win!  " + str(answer))
            break
        else:
            print("%d black; %d white" % pegs)
    else:
        print("You lose: " + str(answer))


main()

