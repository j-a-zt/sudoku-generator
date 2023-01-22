import random
import itertools

class Sudoku():
    def __init__(self):
        self.count = 0
        self.solution_found = []

    def check_valid(self,num, x, y, board):
        ## To check if number exist in the row
        if num in board[y]:
            return False

        ## To check if number exist in the column
        for check in board:
            if num == check[x]:
                return False

        ## To check if number exist in the box
        x = x // 3
        y = y // 3
        for y1 in range(y * 3, y + 3):
            for x1 in range(x * 3, x * 3 + 3):
                if num == board[y1][x1]:
                    return False
        return True

    def single_solve(self,puzzle):
        solution = None
        for count_y in range(9):
            for count_x in range(9):
                if puzzle[count_y][count_x] == 0:
                    for num in range(1, 10):
                        if self.check_valid(num, count_x, count_y, puzzle):
                            puzzle[count_y][count_x] = num
                            solution = self.single_solve(puzzle)
                            if solution is not None:
                                return solution
                            puzzle[count_y][count_x] = 0
                    return None
        return puzzle

    def create_solved_sudoku(self):
        print('Running create_solved_sudoku')
        ## Initialise Sudoku array
        new_board = [[0] * 9 for i in range(9)]

        ## Storing in 1st box
        gen = list(range(1, 10))
        random.shuffle(gen)
        for y in range(3):
            for x in range(3):
                num = random.choice(gen)
                new_board[y][x] = num
                gen.remove(num)

        ## Storing in 2nd box
        gen = list(range(1, 10))
        random.shuffle(gen)
        for y in range(3, 6):
            for x in range(3, 6):
                num = random.choice(gen)
                new_board[y][x] = num
                gen.remove(num)

        ## Storing in 3rd box
        gen = list(range(1, 10))
        random.shuffle(gen)
        for y in range(6, 9):
            for x in range(6, 9):
                num = random.choice(gen)
                new_board[y][x] = num
                gen.remove(num)
        solved_board = self.single_solve(new_board)
        return solved_board

    def create_sudoku_puzzle(self,scale=0.3):
        solved_sudoku = self.create_solved_sudoku()
        x = [i for i in range(9)]
        y = [i for i in range(9)]
        a = list(itertools.product(x, y))
        random_list = random.sample(range(1, 81), int(scale * 81))
        for item in random_list:
            solved_sudoku[a[item][1]][a[item][0]] = 0
        return solved_sudoku

    def generate_puzzle(self,scale=0.3):
        puzzle = self.create_sudoku_puzzle(scale=scale)
        while self.check_duplicate(puzzle):
            puzzle = self.create_sudoku_puzzle(scale=scale)
            print('Checking duplicates..')
            self.solution_found = []
            scale = scale - 0.01
        return puzzle

    def check_duplicate(self,puzzle):
        test_ting = puzzle.copy()
        for count_y in range(9):
            for count_x in range(9):
                if test_ting[count_y][count_x] == 0:
                    for num in range(1, 10):
                        if self.check_valid(num, count_x, count_y, test_ting):
                            test_ting[count_y][count_x] = num
                            if self.check_duplicate(test_ting):
                                return True
                            test_ting[count_y][count_x] = 0
                    return False
        self.solution_found.append(puzzle)
        return len(self.solution_found) > 1