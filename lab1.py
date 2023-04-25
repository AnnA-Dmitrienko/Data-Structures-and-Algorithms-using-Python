
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function 1:
# Name: wins_rock_scissors_paper
# Parameters: 2 strings
# Return: a boolean value
# Description: This function is passed two strings. Each of the two strings is going to be one of 3 values:
# rock
# paper
# scissors
# The strings may have any casing. Rock, ROCK, roCK are all possible and valid.
# The first string represents what the player threw in a game of rocks paper scissors. The second string represents what the opponent threw.
# This function returns true, if the player won, and false if it was a tie or a loss.
# In a game of rock, paper, scissors, each player  "throws" one of the 3 items. The winner is determined by the following rules
# rock beats scissors
# paper beats rock
# scissor beats paper


def wins_rock_scissors_paper(player, opponent):
    validChoice = {'rock', 'paper', 'scissors'}
    # player = player.lower()
    # opponent = opponent.lower()

    # imitate .Lower() function
    def to_lower_case(string):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        result = ''
        for character in string:
            for pos in range(52):
                if alphabet[pos] == character:
                    i = pos
            if character not in alphabet or i >= 26:
                result += character
            else:
                result += alphabet[i+26]
        return result

    # convert input to lower case
    player = to_lower_case(player)
    opponent = to_lower_case(opponent)

    # determine the winner
    if player not in validChoice or opponent not in validChoice:
        return 'please choose a valid option (rock, paper, scissors)'
    elif player == 'rock' and opponent == 'scissors' or \
            player == 'paper' and opponent == 'rock' or \
            player == 'scissors' and opponent == 'paper':
        return True
    else:
        return False


# TESTING :
print(wins_rock_scissors_paper('rock', 'rock'))
print(wins_rock_scissors_paper('rock', 'scissors'))
print(wins_rock_scissors_paper('rock', 'paper'))
print(wins_rock_scissors_paper('scissors', 'rock'))
print(wins_rock_scissors_paper('scissors', 'scissors'))
print(wins_rock_scissors_paper('scissors', 'paper'))
print(wins_rock_scissors_paper('paper', 'rock'))
print(wins_rock_scissors_paper('paper', 'scissors'))
print(wins_rock_scissors_paper('paper', 'paper'))

# print(wins_rock_scissors_paper('papER', 'ROCK'))  # True
# print(wins_rock_scissors_paper('papER', 'rock'))  # True
# print(wins_rock_scissors_paper('Rock', 'paper'))  # False
# print(wins_rock_scissors_paper('papER', 'ROCK'))  # True
# print(wins_rock_scissors_paper('scissors', 'ROCK'))  # False
# print(wins_rock_scissors_paper('papER', 'sciSSors'))  # False
# print(wins_rock_scissors_paper('Rock', 'ROCK'))  # False
# print(wins_rock_scissors_paper('PAPER', 'PAper'))  # False
# # please choose a valid option (rock, paper, scissors)
# print(wins_rock_scissors_paper('Spark', 'ScissoRs'))
# # please choose a valid option (rock, paper, scissors)
# print(wins_rock_scissors_paper('Paper', 'LIZARD'))
# # please choose a valid option (rock, paper, scissors)
# print(wins_rock_scissors_paper('LIZARD', 'spark'))


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function 2:
# Name: factorial
# Parameters: a number (int)
# Return: a number (int)
# Description: This function is passed a non-negative integer, that we will call n in this description. the function returns n! (pronounced n factorial).
#  n! = n * (n-1) * (n-2)... * 1 Thus, 3! = 3 * 2 * 1. Note that 0! is 1 by definition.

def factorial(n):
    rc = 1

    if (n > 1):
        rc = n * factorial(n-1)

    return rc
    # try:
    #     n = int(n)
    # except ValueError:
    #     return 'value must be an int'

    # if n < 0:
    #     return 'number cannot be negative'
    # elif n is 0:
    #     return 1
    # else:
    #     num = 1
    #     for i in range(1, n+1):
    #         num = num * i
    #     return num


# TESTING :
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(5))  # 120
print(factorial(7))  # 5040
# print(factorial('7.3'))  # value must be an int
# print(factorial('$$'))  # value must be an int
# print(factorial('-3'))  # number cannot be negative


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function 3:
# Name: Fibonacci
# Parameters: a number (int)
# Return: a number (int)
# Description: This function is passed a non-negative integer, that we will call n in this description. the function returns the nth Fibonacci number in the Fibonacci sequence.
# The nth Fibonacci number is the sum of the 2 previous Fibonacci numbers. Here is a sample of the Fibonacci series
# 1, 1, 2, 3, 5, 8, 13, 21, ..
# This means that your function should return 13 if the parameter sent to it is 6 and 1 if the parameter is 2

def Fibonacci(n):
    # try:
    #     n = int(n)
    # except ValueError:
    #     return 'value must be an int'

    # if n <= 0:
    #     return 'number cannot be negative'
    # elif n is 0 or n is 1:
    #     return 1
    # else:
    #     return Fibonacci(n-1)+Fibonacci(n-2)
    rc = 1

    if (n > 1):
        rc = Fibonacci(n-1)+Fibonacci(n-2)

    return rc


# TESTING :
print(Fibonacci(0))  # 1
print(Fibonacci(1))  # 1
print(Fibonacci(2))  # 2
print(Fibonacci(3))  # 3
print(Fibonacci(4))  # 5
print(Fibonacci(5))  # 8
print(Fibonacci(6))  # 13
print(Fibonacci(7))  # 21
print(Fibonacci(8))  # 34
# print(Fibonacci(-5))  # number cannot be negative
# print(Fibonacci('Anna'))  # value must be an int
