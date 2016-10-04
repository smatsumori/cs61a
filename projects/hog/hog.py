"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact
import sys

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    total, i = 0, 0
    while i < num_rolls:
        tmp = dice()
        i += 1
        total += tmp
        if tmp == 1:
            while i < num_rolls:
                tmp = dice()
                i += 1
            return 1
    return total
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    fd = opponent_score // 10
    sd = opponent_score % 10
    return fd + 1 if fd >= sd else sd + 1
    # END PROBLEM 2


# Write your prime functions here!

def is_prime(num):
    assert type(num) == int, 'type int'
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def next_prime(start):
    assert type(start) == int, 'type int'
    for i in range(start + 1, sys.maxsize):
        if is_prime(i):
            return i
    return 0


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    um_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        score = free_bacon(opponent_score)
    else:
        score = roll_dice(num_rolls, dice)
    if is_prime(score):
        return next_prime(score)
    return score
    # END PROBLEM 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    return four_sided if (score + opponent_score) % 7 == 0 else six_sided
    # END PROBLEM 3


def max_dice(score, opponent_score):
    """Return the maximum number of dice the current player can roll. The
    current player can roll at most 10 dice unless the sum of SCORE and
    OPPONENT_SCORE ends in a 7, in which case the player can roll at most 1.
    """
    # Hog Tied
    # BEGIN PROBLEM 3
    return 1 if (score + opponent_score) % 10 == 7 else 10
    # END PROBLEM 3


def is_swap(score):
    """Returns whether the SCORE contains only one unique digit, such as 22.
    """
    # BEGIN PROBLEM 4
    dig3 = score % 10
    dig2 = (score % 100) // 10
    dig1 = (score % 1000) // 100
    # dig1 dig2 dig3
    if dig1 == dig2 == dig3:
        return True
    elif dig1 == 0 and dig2 == dig3:
        return True
    elif dig1 == 0 and dig2 == 0:
        return True
    return False
    # END PROBLEM 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    opponent = other(player)
    # BEGIN PROBLEM 5
    score = [score0, score1]
    strategy = [strategy0, strategy1]
    turn = 1
    while score[0] < goal and score[1] < goal:
        dice = select_dice(score[player], score[opponent])

        num_rolls_str = strategy[player](score[player], score[opponent])
        num_rolls_max = max_dice(score[player], score[opponent])
        num_rolls = min(num_rolls_str, num_rolls_max)

        temp_score = take_turn(num_rolls, score[opponent], dice)

        # Add Player Score
        score[player] += temp_score

        if is_swap(score[player]):
            score[player], score[opponent] = score[opponent], score[player]

        # Change Player
        player, opponent = opponent, player
        turn += 1

    return score[0], score[1]
    # END PROBLEM 5


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    @check_strategy
    def strategy(score, opponent_score):
        return n

    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid strategy
    output. All strategy outputs must be non-negative integers less than or
    equal to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy retuns an invalid
    output.

    >>> always_roll_5 = always_roll(5)
    >>> always_roll_5 == check_strategy(always_roll_5)
    True
    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> fail_15_20 == check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (invalid number of rolls)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> fail_102_115 == check_strategy(fail_102_115)
    True
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    for i in range(goal):
        for j in range(goal):
            check_strategy_roll(i, j, strategy(i, j))
    # END PROBLEM 6
    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """

    # BEGIN PROBLEM 7
    def average(*args):
        result, x = 0, 1
        while x <= num_samples:
            result, x = fn(*args) + result, x + 1
        return result / num_samples

    return average
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    maximum = 0
    for i in range(1, 11):
        # temp is an average score you get when you call a roll dice 1000 times with num_rolls = i
        temp = make_averaged(roll_dice, num_samples)(i, dice)
        if maximum < temp:
            maximum = temp
            dice_to_roll = i
    return dice_to_roll
    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

@check_strategy
def bacon_strategy(score, opponent_score, margin=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # Yujin
    # BEGIN PROBLEM 9
    if is_prime(free_bacon(opponent_score)):
        # if Prime Hop
        score = next_prime(free_bacon(opponent_score))
    else:
        score = free_bacon(opponent_score)
    # score is a result of executing bacon

    if score >= margin:
        num_rolls = 0
    return num_rolls

    # END PROBLEM 9


@check_strategy
def swap_strategy(score, opponent_score, margin=5, num_rolls=6):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points and doesn't trigger a
    swap. Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    if opponent_score > (score + free_bacon(opponent_score)):
        return 0
    else:
        return num_rolls
        # END PROBLEM 10


def roll_to_pig(dice):
    """
    return the number to get pigout
    :param dice:
    :return:
    """
    i = 1
    while i <= 10:
        if roll_dice(i, dice) == 1:
            return i
    return 11


def get_total_score(score, opponent_score, num_dice):
    if num_dice == 0:
        if is_prime(free_bacon(opponent_score)):
            # if Prime Hop
            score = next_prime(free_bacon(opponent_score))
        else:
            score = free_bacon(opponent_score)
    if num_dice == 10:
        if is_prime(score + 1):
            score = next_prime(free_bacon(opponent_score))
        else:
            score += 1

    if is_swap(score):
        return opponent_score

    return score


H_num_roll_4 = max_scoring_num_rolls(four_sided)
H_num_roll_6 = max_scoring_num_rolls(six_sided)
H_margin_4 = make_averaged(four_sided)()
H_margin_6 = make_averaged(six_sided)()


@check_strategy
def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    Two thing is completely under ctrl which is
    1. Free Bacon
    2. Pig Out

    *** YOUR DESCRIPTION HERE ***
    """
    # # BEGIN PROBLEM 10
    # # Constant
    #
    # # Hypo Score
    # h_num_roll = H_num_roll_4 if (score + opponent_score) % 7 == 0 else H_num_roll_6
    # h_margin = H_margin_4 if (score + opponent_score) % 7 == 0 else H_margin_6
    # max_num_roll = max_dice(score, opponent_score)
    #
    # # hog score is a total score for a player
    # mar_score = h_margin + score
    # hog_score = get_total_score(score, opponent_score, 0)
    # pig_score = get_total_score(score, opponent_score, 10)
    #
    # if max_num_roll == 1:
    #     return 10 if pig_score > mar_score else 1
    #
    # print(hog_score, pig_score, mar_score)
    #
    # # Bet Win
    # if hog_score > GOAL_SCORE:
    #     return 0
    # elif pig_score > GOAL_SCORE:
    #     return 10
    # elif score + h_margin > GOAL_SCORE:
    #     return h_num_roll
    #
    # if score < opponent_score:
    #     return swap_strategy(score, opponent_score, h_margin, h_num_roll)
    # else:
    #     return bacon_strategy(score, opponent_score, h_margin, h_num_roll)
    #
    # # hm_num_roll = max_scoring_num_rolls(dice, num_samples)
    # #    h_pig = roll_to_pig(dice)
    # #    h_bacon = take_turn(0, opponent_score, dice)
    #
    # # return swap_strategy(score, opponent_score, h_margin, hm_num_roll)
    #
    # return num_dice  # Replace this statement
    x = free_bacon(opponent_score)
    if is_prime(x):
        x = next_prime(x)
    if x + score >= 100:
        return 0
    if is_swap(score + x):
        if score + x < opponent_score:
            return 0
    if is_swap(score + 1) and opponent_score > score:
        return 10
    if x > 7 and score > opponent_score and not is_swap(score + x):
        return 0

    if (score + opponent_score + x) % 10 == 7 and score < opponent_score:
        return 0
    if opponent_score > score and (score + opponent_score + 1) % 10 == 7:
        return 10
    if (score + opponent_score + x) % 7 == 0 and score < opponent_score:
        return 0
    if opponent_score > score and (score + opponent_score + 1) % 7 == 0:
        return 10
    if select_dice(score, opponent_score) == four_sided:
        return 4

    return 8  # Replace this statement
    # return the num_dice to roll
    # END PROBLEM 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
