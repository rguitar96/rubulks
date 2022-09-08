import sys
from random import randrange
import warnings
import typing

import rubulks.util

class Cube:
    '''
    A class to represent a 3x3x3 cube.

    ...

    Attributes
    ----------
    cube_state : dict[str, list[int]]
        state of the cube, with three lists representing corners, edges and centers
    color_scheme : str
        key representing on of the keys defined in utils
    '''
    def __init__(self,
                 cube_state: typing.Dict[str, typing.List[int]] = rubulks.util.cube.SOLVED_STATE,
                 color_scheme='standard'):
        color_schemes = rubulks.util.cube.COLOR_SCHEMES
        default_scheme = color_schemes['standard']
        self.color_scheme = color_schemes[color_scheme] if color_scheme in color_schemes else default_scheme
        
        self.cube_state = cube_state

        self.possible_moves = rubulks.util.cube.MOVE_LIST
        self.compound_moves_dict = rubulks.util.cube.compound_moves_dict

        self.MOVES_CORNERS = rubulks.util.cube.AFFECTED_PIECES['corners']
        self.MOVES_EDGES = rubulks.util.cube.AFFECTED_PIECES['edges']
        self.MOVES_CENTERS = rubulks.util.cube.AFFECTED_PIECES['centers']
    
    def move(self, move: str):
        '''
        Performs a move or a sequence of moves to the instantiated cube.

                Parameters:
                        move (str): One or multiple moves separated by spaces and
                        defined in the possible moves list.
        '''
        # if multiple moves, divide them
        if len(move.split(' '))>1:
            for m in move.split(' '):
                self.move(m)
            return self

        # if movement is compound (an internal layer), change for equivalent combination
        for compound_move, equivalent in self.compound_moves_dict.items():
            if compound_move in move:
                sequence = ''
                for item in equivalent:
                    if '*' in move: item = (item.replace('*','') if '*' in item else item+'*')
                    if '2' in move: item = item.replace('*','')+'2'
                    sequence += item + ' '
                return self.move(sequence)

        # only allow moves
        if move not in self.possible_moves:
            warnings.warn('Ignoring unrecognized move: {0}'.format(move))
            return self
        
        # detect inerse or double movements
        direction = 1 if '*' in move else -1
        double = True if '2' in move else False
        move = move.replace('*','').replace('2','')

        # move affected centers
        centers_copy = list(self.cube_state['centers'])
        for i in range(len(self.MOVES_CENTERS[move])):
            self.cube_state['centers'][self.MOVES_CENTERS[move][i]-1] = centers_copy[self.MOVES_CENTERS[move][(i+direction)%len(self.MOVES_CENTERS[move])]-1]

        # move affected corners
        corners_copy = list(self.cube_state['corners'])
        for i in range(len(self.MOVES_CORNERS[move])):
            for j in range(len(self.MOVES_CORNERS[move][i])):
                self.cube_state['corners'][self.MOVES_CORNERS[move][i][j]-1] = corners_copy[self.MOVES_CORNERS[move][i][(j+direction)%len(self.MOVES_CORNERS[move][i])]-1]
        
        # move affected edges
        edges_copy = list(self.cube_state['edges'])
        for i in range(len(self.MOVES_EDGES[move])):
            for j in range(len(self.MOVES_EDGES[move][i])):
                self.cube_state['edges'][self.MOVES_EDGES[move][i][j]-1] = edges_copy[self.MOVES_EDGES[move][i][(j+direction)%len(self.MOVES_EDGES[move][i])]-1]

        # repeat double move
        if double:
            self.move(move.replace('2',''))
        
        return self
    
    def random_scramble(self,n_moves=20):
        '''
        Performs a defined number of random moves.

                Parameters:
                        n_moves (int): Number of random moves to perform
        '''
        for i in range(n_moves):
            # select a random possible move
            r = randrange(len(self.possible_moves))
            self.move(self.possible_moves[r])
    
    def reset_cube(self):
        '''
        Performs a defined number of random moves.

                Parameters:
                        n_moves (int): Number of random moves to perform
        '''
        self.cube_state = rubulks.util.cube.SOLVED_STATE
    
    def _get_color(self, index):
        return self.color_scheme[int((index-1)/4)]

    def __repr__(self):
        spacing = '      '
        new_line = '\n'

        ulb = self._get_color(self.cube_state['corners'][0])
        urb = self._get_color(self.cube_state['corners'][1])
        urf = self._get_color(self.cube_state['corners'][2])
        ulf = self._get_color(self.cube_state['corners'][3])
        
        lbu = self._get_color(self.cube_state['corners'][4])
        lfu = self._get_color(self.cube_state['corners'][5])
        lfd = self._get_color(self.cube_state['corners'][6])
        lbd = self._get_color(self.cube_state['corners'][7])

        flu = self._get_color(self.cube_state['corners'][8])
        fru = self._get_color(self.cube_state['corners'][9])
        frd = self._get_color(self.cube_state['corners'][10])
        fld = self._get_color(self.cube_state['corners'][11])
        
        rfu = self._get_color(self.cube_state['corners'][12])
        rbu = self._get_color(self.cube_state['corners'][13])
        rbd = self._get_color(self.cube_state['corners'][14])
        rfd = self._get_color(self.cube_state['corners'][15])
        
        bru = self._get_color(self.cube_state['corners'][16])
        blu = self._get_color(self.cube_state['corners'][17])
        bld = self._get_color(self.cube_state['corners'][18])
        brd = self._get_color(self.cube_state['corners'][19])

        dlf = self._get_color(self.cube_state['corners'][20])
        drf = self._get_color(self.cube_state['corners'][21])
        drb = self._get_color(self.cube_state['corners'][22])
        dlb = self._get_color(self.cube_state['corners'][23])

        ub = self._get_color(self.cube_state['edges'][0])
        ur = self._get_color(self.cube_state['edges'][1])
        uf = self._get_color(self.cube_state['edges'][2])
        ul = self._get_color(self.cube_state['edges'][3])
        
        lu = self._get_color(self.cube_state['edges'][4])
        lf = self._get_color(self.cube_state['edges'][5])
        ld = self._get_color(self.cube_state['edges'][6])
        lb = self._get_color(self.cube_state['edges'][7])
        
        fu = self._get_color(self.cube_state['edges'][8])
        fr = self._get_color(self.cube_state['edges'][9])
        fd = self._get_color(self.cube_state['edges'][10])
        fl = self._get_color(self.cube_state['edges'][11])
        
        ru = self._get_color(self.cube_state['edges'][12])
        rb = self._get_color(self.cube_state['edges'][13])
        rd = self._get_color(self.cube_state['edges'][14])
        rf = self._get_color(self.cube_state['edges'][15])
        
        bu = self._get_color(self.cube_state['edges'][16])
        bl = self._get_color(self.cube_state['edges'][17])
        bd = self._get_color(self.cube_state['edges'][18])
        br = self._get_color(self.cube_state['edges'][19])
        
        df = self._get_color(self.cube_state['edges'][20])
        dr = self._get_color(self.cube_state['edges'][21])
        db = self._get_color(self.cube_state['edges'][22])
        dl = self._get_color(self.cube_state['edges'][23])

        u = self._get_color(self.cube_state['centers'][0])
        l = self._get_color(self.cube_state['centers'][1])
        f = self._get_color(self.cube_state['centers'][2])
        r = self._get_color(self.cube_state['centers'][3])
        b = self._get_color(self.cube_state['centers'][4])
        d = self._get_color(self.cube_state['centers'][5])

        rep = ''

        rep += spacing + ulb + ' ' + ub + ' ' + urb
        rep += new_line
        rep += spacing + ul + ' ' + u + ' ' + ur
        rep += new_line
        rep += spacing + ulf + ' ' + uf + ' ' + urf
        rep += new_line

        rep += lbu + ' ' + lu + ' ' + lfu + ' '
        rep += flu + ' ' + fu + ' ' + fru + ' '
        rep += rfu + ' ' + ru + ' ' + rbu + ' '
        rep += bru + ' ' + bu + ' ' + blu + ' '
        rep += new_line

        rep += lb + ' ' + l + ' ' + lf + ' '
        rep += fl + ' ' + f + ' ' + fr + ' '
        rep += rf + ' ' + r + ' ' + rb + ' '
        rep += br + ' ' + b + ' ' + bl + ' '
        rep += new_line

        rep += lbd + ' ' + ld + ' ' + lfd + ' '
        rep += fld + ' ' + fd + ' ' + frd + ' '
        rep += rfd + ' ' + rd + ' ' + rbd + ' '
        rep += brd + ' ' + bd + ' ' + bld + ' '
        rep += new_line

        rep += spacing + dlf + ' ' + df + ' ' + drf
        rep += new_line
        rep += spacing + dl + ' ' + d + ' ' + dr
        rep += new_line
        rep += spacing + dlb + ' ' + df + ' ' + drb
        
        return rep
