"""Day 4: Bingo! With a giant squid.
Part 1: A series of numbers are called. Find the forst board out of a series
of options to win. A win is when a full vertical or horizontal row/column has
been called.
"""

def get_winning_board_score(numbers, boards):
    """Finds the first board to win bingo and returns its score, i.e. the sum
    of the remaining numbers on that board and multiplied by the last number
    called.
    Args:
        numbers (list): list of integers of the numbers that will be called.
        boards (list): a list of lists of integers of 5x5 bingo boards.
    Returns:
        score (int): sum of the remaining numbers on the bingo board multiplied
            by the last number called.
    """
    for i in range(5,len(numbers)):
        numbers_called = numbers[:i]
        for board in boards:
            horizontal = board
            vertical = list(map(list, zip(*board)))
            for row, col in zip(horizontal, vertical):
                if (all(item in numbers_called for item in row) or
                all(item in numbers_called for item in col)):
                    on_board = [item for sublist in board for item in sublist]
                    remaining = [x for x in on_board if x not in numbers_called]
                    score = sum(remaining)*numbers_called[-1]
                    return score

"""
Part 2: Actually, maybe we should let the squid win... Let's choose the last
board to win to guarantee that even with all the squids arms, we will lose.
"""

def get_losing_board_score(numbers, boards):
    """Finds the last board to win bingo and returns its score, i.e. the sum
    of the remaining numbers mulitplied by the last number called.
    Args:
        numbers (list): list of integers of the numbers that will be called.
        boards (list): a list of lists of integers of 5x5 bingo boards.
    Returns:
        score (int): sum of the remaining numbers on the bingo board multiplied
            by the last number called.
    """
    for i in range(5,len(numbers)):
        numbers_called = numbers[:i]
        for board in boards:
            horizontal = board
            vertical = list(map(list, zip(*board)))
            for row, col in zip(horizontal, vertical):
                if (all(item in numbers_called for item in row) or
                all(item in numbers_called for item in col)):
                    if board in boards:
                        boards.remove(board)
                    if len(boards)==0:
                        on_board = [item for sublist in board for item in sublist]
                        remaining = [x for x in on_board if x not in numbers_called]
                        score = sum(remaining)*numbers_called[-1]
                        return score


with open('inputs/input_day_4_boards.txt') as f, open('inputs/input_day_4_numbers.txt') as g:
    boards_file = f.read()
    boards_file = boards_file.splitlines()
    boards_file = [x.split() for x in boards_file if x]
    boards_file = [list(map(int, item)) for item in boards_file]
    boards = [boards_file[i:i+5] for i in range(0,len(boards_file),5)]

    numbers_file = g.read()
    numbers_file  = numbers_file.split(',')
    numbers = [int(x) for x in numbers_file]
    print(f'The answer to Part 1 is: {get_winning_board_score(numbers, boards)}.')
    print(f'The answer to Part 2 is: {get_losing_board_score(numbers, boards)}.')