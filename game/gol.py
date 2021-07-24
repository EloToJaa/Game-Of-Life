from utils import *
import numpy as np


class GameOfLife:

    def __init__(self):
        self.current_generation = self.generate_grid()
        #self.current_generation = self.load_template('glider_gun')
        self.connections = self.connecting()

    def generate_grid(self):
        random_vals = np.random.randint(
            0, CHANCES + 1, (ROWS + 2, COLS + 2))
        grid = np.zeros((ROWS + 2, COLS + 2), dtype=bool)
        for i in range(ROWS + 2):
            for j in range(COLS + 2):
                if (not (i == 0 or j == 0 or i == COLS + 1 or j == ROWS + 1)) and random_vals[i, j] == 0:
                    grid[i, j] = True
        return grid

    def load_template(self, temp_name):
        offsets = {
            'glider_gun': 1,
            "infinite_growth_1": 120,
            "infinite_growth_2": 100,
            "infinite_growth_3": 70
        }
        grid = np.zeros((ROWS + 2, COLS + 2), dtype=bool)
        with open(f'./game/templates/{temp_name}.txt') as f:
            lines = [line.split() for line in f.readlines()]

        offset = offsets[temp_name]

        additional_lines = [
            ['0' for _ in range(len(lines[0]) + offset)] for _ in range(offset)]

        additional_zeros = ['0' for _ in range(offset)]

        for i in range(len(lines)):
            lines[i] = additional_zeros + lines[i]

        lines = additional_lines + lines

        for i, line in enumerate(lines):
            for j, val in enumerate(line):
                if val == '1':
                    grid[i + 1, j + 1] = True

        return grid

    def change_template(self, button_text):
        temp_name = button_text.lower().replace(' ', '_')
        if temp_name == 'random':
            self.current_generation = self.generate_grid()
        else:
            self.current_generation = self.load_template(temp_name)

    def connecting(self):
        set_list = [[[] for j in range(COLS + 2)] for i in range(ROWS + 2)]
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                set_list[i][j].append((i, j))
        set_list[1][1].append((ROWS + 1, COLS + 1))
        set_list[ROWS][COLS].append((0, 0))
        set_list[1][COLS].append((ROWS + 1, 0))
        set_list[ROWS][1].append((0, COLS + 1))
        for i in range(1, COLS + 1):
            set_list[1][i].append((ROWS + 1, i))
            set_list[ROWS][i].append((0, i))
        for i in range(1, ROWS + 1):
            set_list[i][1].append((i, COLS + 1))
            set_list[i][COLS].append((i, 0))
        return set_list

    def set_val(self, y, x, val):
        positions = self.connections[y][x]
        for pos in positions:
            self.current_generation[pos] = val

    def alive_count(self, y, x):
        counter = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if self.previous_generation[i, j]:
                    counter += 1
        if self.previous_generation[y, x]:
            counter -= 1
        return counter

    def next_generation(self):
        self.previous_generation = np.copy(self.current_generation)
        self.current_generation = np.zeros((ROWS + 2, COLS + 2), dtype=bool)
        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                counter = self.alive_count(i, j)
                alive = self.previous_generation[i, j]
                if (alive and (counter == 2 or counter == 3)) or ((not alive) and counter == 3):
                    self.set_val(i, j, True)
                else:
                    self.set_val(i, j, False)
        return self.current_generation
