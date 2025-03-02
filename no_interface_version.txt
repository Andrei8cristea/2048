#Cristea Andrei - 2048 game project

# have an all 0 set matrix
# add on an empty position the value 2, 4 or 8 with the odds of picking each
# being (60%, 30%, 10%)

# the moves: wasd
# have to put every non-zero tile on the furthest position
# have to make the sum of two equal adjacent tiles

#move_left:
# I am setting a list of all non_zero elements
# and merge them two by two

#move_down
#matrix -> transpose -> move_right -> transpose back

#move_up
#matrix -> transpose -> move_left -> transpose back

#########################################################################################################################
import random


matrix_2048 = []
score_2048 = int(0)

def set_value_0(matrix):
    for i in range(4):
        matrix.append([0 for _ in range(4)])

def print_matrix(matrix):
    for row in matrix:
        print(*row)
    print()

def add_tile(matrix):
    empty_cells = []
    for row in range(4):
        for col in range(4):
            if matrix[row][col] == 0:
                empty_cells.append((row, col))
    if empty_cells:
        random_value = random.randint(0, 9)
        if random_value == 9:
            value = 8
        elif random_value >= 6:
            value = 4
        else:
            value = 2
        random_row, random_col = random.choice(empty_cells)
        matrix[random_row][random_col] = value


def sum_matrix(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total


def move_left(matrix):
    for row in matrix:
        new_row = [x for x in row if x != 0]
        new_row.extend([0] * (4 - len(new_row)))
        i = 0
        while i < 3:
            if new_row[i] == new_row[i+1]:
                new_row[i] *= 2
                new_row[i+1] = 0
                i += 1
            i += 1

        new_row = [x for x in new_row if x != 0]
        new_row.extend([0] * (4 - len(new_row)))
        for j in range(4):
            row[j] = new_row[j]


def move_right(matrix):
    for row in matrix:
        new_row = [x for x in row if x != 0]
        new_row =([0] * (4 - len(new_row))) + new_row
        i = 3
        while i > 0:
            if new_row[i] == new_row[i-1]:
                new_row[i] *= 2
                new_row[i-1] = 0
                i -= 1
            i -= 1

        new_row = [x for x in new_row if x != 0]
        new_row =([0] * (4 - len(new_row))) + new_row
        for j in range(4):
            row[j] = new_row[j]


def move_down(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]
    move_right(matrix)
    matrix[:] = [list(row) for row in zip(*matrix)]


def move_up(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]
    move_left(matrix)
    matrix[:] = [list(row) for row in zip(*matrix)]



def action(matrix):
    key = input("Muta: ")
    original_matrix = [row[:] for row in matrix]  #save a copy of the matrix for checking if the move was valid

    if key == 'w':
        move_up(matrix)
    elif key == 'a':
        move_left(matrix)
    elif key == 's':
        move_down(matrix)
    elif key == 'd':
        move_right(matrix)
    else:
        pass  #if the key is invalid it won t make any move

    # if the move was valid it adds a new tile and outputs the new matrix.
    if matrix != original_matrix:
        add_tile(matrix)
        print_matrix(matrix)

def check_if_over(matrix):
    #first I check if I have any zeros in the matrix
    #if yes ret false else check if any two adjacent
    #items are equal. If yes ret false else true
    if any(0 in sublist for sublist in matrix):
        return False
    else:
        for i in range(4):
            for j in range(4):
                if j<3 and matrix[i][j] == matrix[i][j+1]:
                    return False
                if i<3 and matrix[i][j] == matrix[i+1][j]:
                    return False
        return True

def calculate_score(matrix):
    score = 0
    for i in range(4):
        for j in range(4):
            score += matrix[i][j]
    return score


# !!!  beginning of program


# matrix_test1 = [[1, 2, 3, 4],
#                [5, 6, 7, 8],
#                [9,10,11,12],
#                [13,14,15,16]]
#
# matrix_test2 = [[2, 2, 3, 4],
#                [5, 6, 7, 8],
#                [9,10,11,12],
#                [13,14,15,16]]
#
# print(matrix_test1 == matrix_test2)

#
set_value_0(matrix_2048)
add_tile(matrix_2048)
print_matrix(matrix_2048)


running = True
while running:
    action(matrix_2048)
    if check_if_over(matrix_2048) is True:
        running = False
        score_2048 = calculate_score(matrix_2048)
        print(f"GAME OVER! SCORE: {score_2048}.")
