from random import *

class TilePuzzle():
    def __init__(self, first_row, second_row, third_row):
        '''
        (TilePuzzle, list of int, list of int, list of int) -> None
        Note the TilePuzzle in the solved solution is:
        first_row = [0, 1, 2]
        second_row = [3, 4, 5]
        third_row = [e, 6, 7]
        where e is the empty spot
        '''
        self._state = [first_row, second_row, third_row]

    def __repr__(self):
        result = ''
        for i in range(3):
            for e in range(3):
                result += str(self._state[i][e]) + ', '
            result = result[:-2] + '\n'
        return result[:-1]

    def show_solution(self):
        #moving first piece 0 to (0, 0) aka first_row[0]
        #moving the empty piece to the middle
        #if piece 0 is in the middle
        if self._state[1][1] == 0:
            #if middle piece does not have an empty spot adjacent
            adj_to_mid = ['01', '13', '15', '26']
            empt = self.find_empty()
            if not empt in adj_to_mid:
                #this will create an opening for the middle piece
                swap_list = ['01', '10', '12', '21']
                stop = False
                for e in swap_list:
                    if not stop and self.swap(e):
                        stop = True
            self.swap('11')
        #swapping a non zero tile into the middle
        if self._state[0][1] == '0':
            self.swap('10')
        else:
            self.swap('01')
        #rotating tiles until 0 is in position (0, 0)
        perimeter = ['00', '01', '02', '12', '22', '21', '20', '10']
        while self._state[0][0] != 0:
            for e in perimeter:
                if not self._state[0][0] == 0:
                    self.swap(e)
        #building columns
        cols =[[self._state[i][e] for e in range(1, 3)] for i in range(0, 3)]
        print(cols)
        #making tiles 1 and 2 and e appear in columns 1 and 2
        if not (1 in str(cols) and 2 in str(cols) and 'e' in str(cols)):
            pass
        else:
            pass

    def bfs_solution(self):
        corners = ['00', '02', '20', '22']
        mid = ['11']
        sides = ['01', '10', '12', '21']
        tiles = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        if self.is_solved():
            result = None
        else:
            pass


    def is_solved(self):
        return self._state == [[0, 1, 2], [3, 4, 5], ['e', 6, 7]]

    def swap(self, tile, show=True):
        #finding empty must be within one row and within one column
        empt = self.find_empty()
        col_dif = int(tile[0]) - int(empt[0])
        row_dif = int(tile[1]) - int(empt[1])
        allowed_state = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        if (col_dif, row_dif) in allowed_state:
            self._state[int(tile[0])][int(tile[1])], self._state[int(empt[0])][int(empt[1])] = 'e', self._state[int(tile[0])][int(tile[1])]
            x = print('Swapping tile ' + tile) if show else None
            result = True
        else:
            result = False
        return result

    def find_empty(self):
        if 'e' in self._state[0]:
            result = '0' + str(self._state[0].index('e'))
        elif 'e' in self._state[1]:
            result = '1' + str(self._state[1].index('e'))
        else:
            result = '2' + str(self._state[2].index('e'))
        return result

    def randomize(self):
        counter = 0
        while counter <= 50:
            if self.swap(str(randint(0, 2)) + str(randint(0, 2)), False):
                counter += 1
