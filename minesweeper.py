import random
class MineSweeper:

    def __init__(self):
        self.matrix_size = 9
        self.create_boards()
        self.moves = 0

    def create_boards(self):
        self.mine_matrix = [[0] * self.matrix_size for _ in range(self.matrix_size)]
        self.input_matrix = [[' '] * self.matrix_size for _ in range(self.matrix_size)]

        for i in range(self.matrix_size):
            self.mine_matrix[i][random.randrange(0,self.matrix_size)] = '*'

        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.mine_matrix[i][j] == '*':
                    if i > 0:
                        if self.mine_matrix[i-1][j] != '*':
                            self.mine_matrix[i-1][j] += 1
                        if j < self.matrix_size - 1 and self.mine_matrix[i - 1][j + 1] != '*':
                            self.mine_matrix[i - 1][j + 1] += 1
                        if j > 0 and self.mine_matrix[i - 1][j - 1] != '*':
                            self.mine_matrix[i - 1][j - 1] += 1

                    if i < self.matrix_size - 1:
                        if self.mine_matrix[i+1][j] != '*':
                            self.mine_matrix[i+1][j] += 1
                        if j < self.matrix_size - 1 and self.mine_matrix[i + 1][j + 1] != '*':
                            self.mine_matrix[i + 1][j + 1] += 1
                        if j > 0 and self.mine_matrix[i + 1][j - 1] != '*':
                            self.mine_matrix[i + 1][j - 1] += 1
                        
                    if j > 0 and self.mine_matrix[i][j - 1] != '*':
                        self.mine_matrix[i][j - 1] += 1
                    if j < self.matrix_size - 1 and self.mine_matrix[i][j + 1] != '*':
                        self.mine_matrix[i][j + 1] += 1


        self.x_axis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.y_axis = [1,2,3,4,5,6,7,8,9]

    def play(self):
        incorrect_choice = False
        while True:
            ret = self.get_input(incorrect_choice)
            incorrect_choice = False
            if ret == -1:
                break
            elif ret == 1:
                continue
            elif ret == 2:
                incorrect_choice = True

    def reset_game(self):
        self.create_boards()
        self.moves = 0
        self.play()
        

    def display_board(self,found_mine=False):
        print(' ', *self.x_axis)
        for i in range(self.matrix_size):
            if not found_mine: print(self.y_axis[i], *self.input_matrix[i])
            else: print(self.y_axis[i], *self.mine_matrix[i])

    def get_input(self, incorrect_choice = False):
        if incorrect_choice:
            location = input("Incorrect input. Enter again (eg. A5): ")
        else:
            self.display_board()
            location = input("Enter location choice eg. E3: ")
        if len(location) != 2:
            return 2
        if not (97 <= ord(location[0].lower()) <= 97 + self.matrix_size - 1):
            return 2
        if not (49 <= ord(location[1]) <= 57):
            return 2

        self.moves += 1
        x_loc = ord(location[0].lower()) - 97
        y_loc = int(location[1]) - 1

        mine_value = self.mine_matrix[y_loc][x_loc]
        if mine_value == '*':
            self.display_board(found_mine=True)
            print('# of moves: %s' % self.moves)
            play_again = input("Play again? y/n: ")
            if play_again.lower() == 'y':
                self.reset_game()
            else:
                return -1
        elif mine_value == 0:
            self.unhide_all_0s_connected_to(y_loc, x_loc)
        else:
            self.input_matrix[y_loc][x_loc] = self.mine_matrix[y_loc][x_loc]
        return 1

    def unhide_all_0s_connected_to(self,row: int, col: int):
        if row >= self.matrix_size or col >= self.matrix_size: return
        if row < 0 or col < 0: return
        if self.mine_matrix[row][col] == '*': return

        if self.mine_matrix[row][col] == 0:
            if self.input_matrix[row][col] == 0: return
            self.input_matrix[row][col] = self.mine_matrix[row][col]
            self.unhide_all_0s_connected_to(row, col + 1)
            self.unhide_all_0s_connected_to(row, col - 1)
            self.unhide_all_0s_connected_to(row + 1, col)
            self.unhide_all_0s_connected_to(row - 1, col)
        self.input_matrix[row][col] = self.mine_matrix[row][col]

game = MineSweeper()
game.play()

