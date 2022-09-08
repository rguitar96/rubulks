# <Move definition>
'''
List of possible moves in the cube, including rotations, inverse and double moves.
- An inverse move is represented with a * (R', the inverse of R, is represented as R*)
- A double move is represented with a 2 (R2 is a double move)

Compound moves (M, E, S) are converted to their equivalent combination of basic moves and rotations.
'''
basic_moves = [
    'F', 'R', 'B', 'L', 'U', 'D', 'M','E','S', 'x', 'y', 'z'
]
compound_moves_dict = {
    'M': ['R', 'L*', 'x*'],
    'E': ['U', 'D*', 'y*'],
    'S': ['F*', 'B', 'z']
}
inverse_moves = [move + '*' for move in basic_moves]
double_moves = [move + '2' for move in basic_moves]
MOVE_LIST = basic_moves + inverse_moves + double_moves
# </Move definition>

# <Cube state>
'''
The cube state is defined by three lists (corners, edges and centers).

Indexes indicate the corresponding piece that should be located there in a solved cube,
and values indicate the piece in the current cube instance.
Therefore, a solved state will be a range list.

Pieces are defined using the usual Blindfolded order.
You can read about notation here:
https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-blindfolded-tutorial/
'''
CORNER_SOLVED_STATE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
EDGE_SOLVED_STATE = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
CENTER_SOLVED_STATE = [1,5,9,13,17,21]
SOLVED_STATE = {
    'corners': CORNER_SOLVED_STATE,
    'edges': EDGE_SOLVED_STATE,
    'centers': CENTER_SOLVED_STATE
}
# </Cube state>

# <Moving logic>
'''
Dictionary indicating which corners are connected (or will permute) after a move.
'''
AFFECTED_CORNERS = {
    'U': [
        [5,17,13,9],
        [6,18,14,10],
        [1,2,3,4]
    ],
    'L': [
        [1,9,21,19],
        [4,12,24,18],
        [5,6,7,8]
    ],
    'F': [
        [3,16,21,6],
        [4,13,22,7],
        [9,10,11,12]
    ],
    'R': [
        [2,20,22,10],
        [3,17,23,11],
        [13,14,15,16]
    ],
    'B': [
        [1,8,23,14],
        [2,5,24,15],
        [17,18,19,20]
    ],
    'D': [
        [7,11,15,19],
        [8,12,16,20],
        [21,22,23,24]
    ],
    'x': [
        [1,19,21,9],
        [4,18,24,12],
        [5,6,7,8],
        [2,20,22,10],
        [3,17,23,11],
        [13,16,15,14]
    ],
    'y': [
        [5,17,13,9],
        [6,18,14,10],
        [1,2,3,4],
        [7,19,15,11],
        [8,20,16,12],
        [21,24,23,22]
    ],
    'z': [
        [3,16,21,6],
        [4,13,22,7],
        [9,10,11,12],
        [1,14,23,8],
        [2,15,24,5],
        [17,20,19,18]
    ]
}

'''
Dictionary indicating which edges are connected (or will permute) after a move.
'''
AFFECTED_EDGES = {
    'U': [
        [5,17,13,9],
        [1,2,3,4]
    ],
    'L': [
        [4,12,24,18],
        [5,6,7,8]
    ],
    'F': [
        [3,16,21,6],
        [9,10,11,12]
    ],
    'R': [
        [2,20,22,10],
        [13,14,15,16]
    ],
    'B': [
        [1,8,23,14],
        [17,18,19,20]
    ],
    'D': [
        [7,11,15,19],
        [21,22,23,24]
    ],
    'x': [
        [4,18,24,12],
        [5,6,7,8],
        [2,20,22,10],
        [13,14,15,16],
        [1,19,21,9],
        [3,17,23,11]
    ],
    'y': [
        [5,17,13,9],
        [1,2,3,4],
        [7,19,15,11],
        [21,24,23,22],
        [6,18,14,10],
        [8,20,16,12]
    ],
    'z': [
        [3,16,21,6],
        [9,10,11,12],
        [1,14,23,8],
        [17,20,19,18],
        [2,15,24,5],
        [4,13,22,7]
    ]
}

'''
Dictionary indicating which centers are connected (or will permute) after a move.
'''
AFFECTED_CENTERS = {
    'U': [],
    'L': [],
    'F': [],
    'R': [],
    'B': [],
    'D': [],
    'M': [],
    'E': [],
    'S': [],
    'x': [1,5,6,3],
    'y': [2,5,4,3],
    'z': [1,4,6,2]
}

'''
Combination of affected pieces.
'''
AFFECTED_PIECES = {
    'corners': AFFECTED_CORNERS,
    'edges': AFFECTED_EDGES,
    'centers': AFFECTED_CENTERS
}
# </Moving logic>

# <Color schemes>
'''
List of predefined color schemes.

A scheme is defined as a list of colors, in the following orders:
U, L, F, R, B, D
'''
COLOR_SCHEMES = {
    # order: U, L, F, R, B, D
    'standard': ['W','O','G','R','B','Y'],
    'japanese': ['W','O','G','R','Y','B']
}
# </Color schemes>
