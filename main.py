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
    key = input("Move: ")
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


#--------------------------------------------------------------------------------------------
#just console

# set_value_0(matrix_2048)
# add_tile(matrix_2048)
# print_matrix(matrix_2048)
#
#
# running = True
# while running:
#     action(matrix_2048)
#     if check_if_over(matrix_2048) is True:
#         running = False
#         score_2048 = calculate_score(matrix_2048)
#         print(f"GAME OVER! SCORE: {score_2048}.")


#--------------------------------------------------------------------------------------------
#graphic interface
import pygame

pygame.init() # loading pygame (also for FONTS to be loaded until the game starts)

#hardcoded variables
WIDTH, HEIGHT = 800,800
FONT = pygame.font.SysFont("arial", 80)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048 - Cristea Andrei")


BACKGROUND_COLOR = (187, 173, 160)

TILE_COLORS = {  # dictionary for the colors of the tiles
    0: (250, 247, 205),
    2: (247, 236, 74),
    4: (227, 195, 54),
    8: (227, 166, 54),
    16: (227, 143, 54),
    32: (219, 87, 31),
    64: (219, 59, 31),
    128: (232, 5, 5),
    256: (92, 92, 237),
    512: (55, 114, 222),
    1024: (16, 160, 204),
    2048: (200, 3, 255)
}
TEXT_COLOR = (10, 23, 7)

CELL_SIZE = WIDTH // 4
MARGIN = 5 #space between tiles


def draw_board(matrix):
    screen.fill(BACKGROUND_COLOR)
    for r in range(4):
        for c in range(4):
            value = matrix[r][c]
            rect = pygame.Rect(c * CELL_SIZE + MARGIN, r* CELL_SIZE + MARGIN, CELL_SIZE - 2*MARGIN, CELL_SIZE - 2*MARGIN)
            color = TILE_COLORS.get(value, ()) #default value if the color isn't found in the dict
            pygame.draw.rect(screen, color,rect) # draw a tile on the screen with the color from the tile color dictionary and the dimensions from rect
            if value != 0:  # printing the text on the non-zero tiles
                text_surface = FONT.render(str(value), True, TEXT_COLOR)
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)

    pygame.display.update()

def game_over_screen(score):
    screen.fill(BACKGROUND_COLOR)
    game_over_text = FONT.render("GAME OVER!", True, TEXT_COLOR)
    score_text = FONT.render(f"SCORE: {score}", True, TILE_COLORS[64])
    game_over_rect = game_over_text.get_rect(center = (WIDTH //2, HEIGHT // 3))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # configuring the play again button
    button_color = (0, 255, 0)  # Green
    button_width = WIDTH // 2
    button_height = 100
    button_rect = pygame.Rect((WIDTH - button_width) // 2, (HEIGHT // 1.5) - (button_height // 2), button_width,
                              button_height)
    button_text = FONT.render("Play Again", True, TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text,score_rect)
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.update()

    #pygame.time.delay(3000) # show the game over screen for 3 seconds
    running_game_over_screen = True
    while running_game_over_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running_game_over_screen = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    startgame()  #call function start game
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                startgame()


def startgame():
    matrix_2048 = []

    set_value_0(matrix_2048)
    add_tile(matrix_2048)

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)  # I am hardcoding the FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT :  # cross button
                running = False

            # now I basically rewrite the action function but for the pygame interface
            elif event.type == pygame.KEYDOWN:
                copy_matrix = [row[:] for row in matrix_2048]
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up(matrix_2048)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left(matrix_2048)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down(matrix_2048)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right(matrix_2048)
                elif event.key == pygame.K_ESCAPE:
                    running = False


                if matrix_2048 != copy_matrix:
                    add_tile(matrix_2048)

        draw_board(matrix_2048)

        if check_if_over(matrix_2048) is True:
            running = False
            score_2048 = calculate_score(matrix_2048)
            game_over_screen(score_2048)

#-----------------------------------------------------------
startgame()



pygame.quit() #only if the user is not exiting normally
