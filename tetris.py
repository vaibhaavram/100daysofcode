from copy import copy, deepcopy

R = int(input())
C = int(input())


def create_border():

    for row in range(R):
        for col in range(C):
            if(row == 0 or row == R-1 or col == 0 or col == C-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()


def tetris_ground():
    matrix = [[0 for col in range(C)] for row in range(R)]

    for row in range(R):
        for col in range(C):
            if(row == 0 or row == R-1 or col == 0 or col == C-1):
                matrix[row][col] = -1
            else:
                matrix[row][col] = 0

    return matrix


def print_matrix(matrix):
    for row in range(R):
        for col in range(C):
            if(matrix[row][col] == -1 or matrix[row][col] == 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def spawn_shapes(shape, matrix, old_matrix, pos=[1, C//2-1]):
    matrix = deepcopy(old_matrix)

    # print(shape)
    height = len(shape)
    width = len(shape[0])
    for row in range(pos[0], pos[0]+height):
        for col in range(pos[1], (pos[1])+width):
            matrix[row][col] = shape[row-pos[0]][col-(pos[1])]

    # print(height, width)
    print_matrix(matrix)
    return matrix, pos


def rotate(shape, direction):
    height = len(shape)
    width = len(shape[0])

    new_shape = [[0 for i in range(height)] for j in range(width)]

    # for row in range(height):
    #     for col in range(width):
    #         new_shape[col][row] = shape[row][col]

    if(direction == "Q"):
        new_row = 0
        for col in range(width-1, -1, -1):
            new_col = 0
            for row in range(height):
                new_shape[new_row][new_col] = shape[row][col]
                new_col += 1
            new_row += 1
    elif(direction == "E"):
        new_row = 0
        for col in range(width):
            new_col = 0
            for row in range(height-1, -1, -1):
                new_shape[new_row][new_col] = shape[row][col]
                new_col += 1
            new_row += 1

    # print(len(new_shape))
    # print(new_shape)
    i = 0
    while(i < len(new_shape)):
        if(new_shape[i] == [0, 0, 0]):
            new_shape.remove([0, 0, 0])
        i += 1
    # print(new_shape)

    return new_shape


def move(matrix, direction, pos):
    # print(matrix)
    # print("Rows "+str(len(matrix))+" Cols "+str(len(matrix[0])))

    if(direction == "A"):
        for row in range(1, R-1):
            for col in range(1, C-1):
                if(matrix[row][col] == 1):

                    matrix[row][col-1] = 1
                    matrix[row][col] = 0
                # if(matrix[row][col-1] == -1):
                #     print_matrix(matrix)
                #     return(matrix)
        pos[1] -= 1

    elif(direction == "D"):
        for row in range(1, R-1):
            for col in range(C-2, 1, -1):
                if(matrix[row][col] == 1):
                    matrix[row][col+1] = 1
                    matrix[row][col] = 0

        pos[1] += 1

    elif(direction == "S"):
        for col in range(1, C-1):
            for row in range(pos[0]+3, 0, -1):
                if(matrix[row][col] == 1):
                    matrix[row][col] = 0
                    matrix[row+1][col] = 1
        pos[0] += 1

    # print(pos)
    print_matrix(matrix)
    return matrix, pos


def user_input():
    Z = [[1, 1, 0],
         [0, 1, 1]]
    S = [[0, 1, 1],
         [1, 1, 0]]
    ML = [[0, 1, 0],
          [0, 1, 0],
          [1, 1, 0]]
    L = [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 1]]
    T = [[1, 1, 1],
         [0, 1, 0],
         [0, 1, 0]]
    I = [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
    SQ = [[1, 1, 0],
          [1, 1, 0]]

    old_matrix = tetris_ground()
    matrix = tetris_ground()
    # print_matrix(matrix)
    shapes = [S, T, Z, I]
    pos = [1, C//2-1]
    for shape in shapes:
        matrix, pos = spawn_shapes(shape, matrix, old_matrix, pos)
        while(pos[0] < R-3):
            print("Enter Operation: ")
            op = input()
            if(op == "A" or op == "D" or op == "S"):
                matrix, pos = move(matrix, op, pos)
            elif(op == "Q" or op == "E"):
                shape = rotate(shape, op)
                matrix, pos = spawn_shapes(shape, matrix, old_matrix, pos)
            else:
                continue
        pos = [1, C//2-1]
        old_matrix = matrix


user_input()
