from numpy import array

ELEMENTS = {'WALL': '*', 'PLACE': '◻', 'BOX': '■', 'CHARACTER': '◉'}

class Sokoban:
    def __init__(self):
        self.restart()
        self.signs = {'w': [-1, 0], 'a': [0, -1], 's': [1, 0], 'd': [0, 1]}
        while True:
            if not self.choose_level():
                break
            while True:
                self.show_field()
                if self.check_end():
                    break
                if not self.move():
                    self.restart()
                    break
                self.redraw_field()

    def choose_level(self):
        while True:
            level = input('Enter level or exit: ')
            if level == 'exit':
                return False
            elif not level.isdigit():
                print('Incorrect input!')
            elif level.isdigit():
                with open('levels.txt', 'r') as file:
                    while True:
                        lvl = file.readline().rstrip('\n')
                        if level == lvl:
                            if self.init_params(file):
                                break
                        else:
                            while True:
                                if file.readline().rstrip('\n') == 'end':
                                    break
                    break
        return True
                    
    def init_params(self, file):
        line1 = self.get_line(file)
        self.field = array([['.']*int(line1[0])]*int(line1[1]))
        line2 = self.get_line(file)
        row = 0
        for el in line2:
            if el == '|':
                row += 1
            else:
                self.save_el('WALL', row, int(el))
        self.place_and_box(self.get_line(file), 'PLACE')
        self.place_and_box(self.get_line(file), 'BOX')
        line5 = self.get_line(file)
        self.save_el('CHARACTER', int(line5[0]), int(line5[1]))
        return True

    def get_line(self, file):
        return file.readline().rstrip('\n').split()

    def place_and_box(self, n_line, el):
        n_line = [int(n) for n in n_line]
        for i in range(0, len(n_line), 2):
            self.save_el(el, n_line[i], n_line[i+1])

    def save_el(self, el, x, y):
        self.coordinates[el].append([x, y])
        self.field[x][y] = ELEMENTS[el]

    def move(self):
        while True:
            sign = input('Write W/A/S/D(↑/←/↓/→) to move or R(restart): ').lower()
            if sign == 'r':
                return False
            if sign in ['w', 'a', 's', 'd']:
                if self.check_move(sign):
                    break
                else:
                    print('Please try again!')
            else:
                print('Incorrect input!')
        return True

    def check_move(self, sign):
        c_coord = [a + b for a, b in zip(self.coordinates['CHARACTER'][0], self.signs[sign])]
        character_coord = self.field[c_coord[0]][c_coord[1]]
        if character_coord == ELEMENTS['WALL']:
            print('Stop, there is a dead end!')
            return False
        elif character_coord == ELEMENTS['BOX']:
            b_coord = [a + b for a, b in zip(c_coord, self.signs[sign])]
            b_index = [index for index in range(len(self.coordinates['BOX'])) if self.coordinates['BOX'][index] == c_coord]
            box_coord = self.field[b_coord[0]][b_coord[1]]
            if box_coord in [ELEMENTS['WALL'], ELEMENTS['BOX']]:
                print('Stop, there is a dead end!')
                return False
            else:
                self.coordinates['BOX'][b_index[0]] = b_coord
            self.coordinates['CHARACTER'][0] = c_coord
            return True
        else:
            self.coordinates['CHARACTER'][0] = c_coord
            return True

    def redraw_field(self):
        self.field = array([['.']*len(self.field[0])]*len(self.field))
        self.redraw_el('WALL')
        self.redraw_el('PLACE')
        self.redraw_el('BOX')
        c_coord = self.coordinates['CHARACTER'][0]
        self.field[c_coord[0]][c_coord[1]] = ELEMENTS['CHARACTER']

    def redraw_el(self, el):
        for wall in self.coordinates[el]:
            self.field[wall[0]][wall[1]] = ELEMENTS[el]

    def show_field(self):
        for row in self.field:
            for el in row:
                print(el, end=' ')
            print('\n', end='')

    def check_end(self):
        check = 0
        for box in self.coordinates['BOX']:
            if True in [True if box == place else False for place in self.coordinates['PLACE']]:
                check += 1
        if check == len(self.coordinates['BOX']):
            print('You are win!')
            self.restart()
            return True

    def restart(self):
        self.coordinates, self.field = {'WALL': [], 'PLACE': [], 'BOX': [], 'CHARACTER': []}, []
                
if __name__ == '__main__':
    Sokoban()