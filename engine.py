"""
Mastermind Engine

Defines:
    COLORS (the number of colors that pegs can come in: 1-N)
    SPACES (the number of spaces for guesses/answers: 1-N)
    make_answer(): generate a random answer to test against
    check_guess(): checks a user's guess
"""

from random import randint

COLORS = 6
SPACES = 4

def make_answer():
    '''Return a random list of ints'''
    return [randint(1, COLORS) for i in range(SPACES)]


def check_guess(answer, guess):
    '''Return a tuple of (int, int) for (right, almost_right)

    Correlates to black and white pegs in the game.
    Answer and guess should both be tuples or lists.'''

    answer = list(answer)
    guess = list(guess)
    # count all the right answers first
    right_answers = [
        same[0] for same in zip(answer, guess)
        if same[0] == same[1]
    ]

    # Don't count any peg twice!
    # Remove the exact answers...
    for ans in right_answers:
        answer.pop(answer.index(ans))
        guess.pop(guess.index(ans))

    # ... and then figure out the almost-right answers
    almost_right = 0
    for peg in list(guess):
        if peg in answer:
            answer.pop(answer.index(peg))
            guess.pop(guess.index(peg))
            almost_right += 1

    return len(right_answers), almost_right

