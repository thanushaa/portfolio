# The constants describing the multiplicative factor for finding a word in
# a particular direction.  These should be used in function get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4


def get_current_player(player_one_turn):
    """ (bool) -> str

    Return 'Player One' iff player_one_turn is True; otherwise, return
    'Player Two'.

    >>> get_current_player(True)
    'Player One'
    >>> get_current_player(False)
    'Player Two'
    """

    # Using ternary operators for one line
    # return 'Player One' if player_one_turn else 'Player Two';
    
    # Or written as:
    if player_one_turn :
        return 'Player One'
    else:
        return 'Player Two'
   
        
def get_winner(scoreOne, scoreTwo):
    """ (int, int) -> str
    
    Return "Player One Wins!" if Player Ones score is higher than Player Twos
    score; otherwise else return "Player Two Wins!' 
    """
    
    if scoreOne == scoreTwo:
        return "Tie Game!"
    elif scoreOne > scoreTwo:
        return "Player One Wins!"
    else:
        return "Player Two Wins!"


def get_factor(direction):
    """ (str) -> int
    
    Return corresponding factor.
    """
    
    if direction == 'up':
        return UP_FACTOR
    elif direction == 'down':
        return DOWN_FACTOR
    elif direction == 'forward':
        return FORWARD_FACTOR
    elif direction == 'backward':
        return BACKWARD_FACTOR
    

def get_points(direction, wordsRemaining):
    """ (str, int) -> int
    
    If the words remaining is equal or greater than 5 then points would be
    calculated by factor * 5. If it is less than 5, the points ould be
    calculated by 10 minus the words remaining (including guess) * factor
    And the last word found is 25 points extra.
    """
    
    # using ternary operator if the last word is found 
    # 25 points is added
    bonus = 25 if wordsRemaining == 1 else 0
    
    if wordsRemaining > 4:
        if direction == 'up':
            return UP_FACTOR * 5
        elif direction == 'down':
            return DOWN_FACTOR * 5
        elif direction == 'forward':
            return FORWARD_FACTOR * 5
        elif direction == 'backward':
            return BACKWARD_FACTOR * 5
    elif wordsRemaining < 5:
        if direction == 'up':
            return ((10 - wordsRemaining) * UP_FACTOR) + bonus
        elif direction == 'down':
            return ((10 - wordsRemaining) * DOWN_FACTOR) + bonus
        elif direction == 'forward':
            return ((10 - wordsRemaining) * FORWARD_FACTOR) + bonus
        elif direction == 'backward': 
            return ((10 - wordsRemaining) * BACKWARD_FACTOR) + bonus      
    

def calculate_score(puzzle, direction, guessedWord, num, wordsRemaining):
    """ (str, str, str, int, int) -> int
    
    Check if the guessed word exists within the direction and column or row.
    If it exists, calculate the points by calling get_points. If it does not
    exist then simply return 0;
    
    """
    
    # find the direction to classify if the word is located in a row or column
    if direction == 'up' or direction == 'down':
        puzzleLine = get_column(puzzle, num)
    elif direction == 'forward' or direction == 'backward':
        puzzleLine = get_row(puzzle, num)
        
    # if guessedWord is found in direction up or backward, reverse the word
    # in order to be found within the row or column
    if direction == 'up' or direction == 'backward':
        guessedWord = reverse(guessedWord)
    
    # check if guessed word exists within row or column
    if contains(puzzleLine, guessedWord):
        return get_points(direction, wordsRemaining)
    else:
        return 0
        

# Helper functions.  Do not modify these, although you are welcome to call
# them.

def get_row(puzzle, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle

    Return row row_num of puzzle.

    >>> get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """

    rows = puzzle.strip().split('\n')
    return rows[row_num]


def get_column(puzzle, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle

    Return column col_num of puzzle.
    >>> get_column('abcde\nefghi\nijklm\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def reverse(s):
    """ (str) -> str

    Return a reversed copy of s.

    >>> reverse('abc')
    'cba'
    """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed

    return s_reversed


def contains(s1, s2):
    """ (str, str) -> bool

    Return whether s2 appears anywhere in s1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return s2 in s1
