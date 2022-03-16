import sys
import threading

def check_rows(matrix):
    valid_rows = True
    for row in matrix:
        if check_repeats(row) == False:
            valid_rows = False
    #print("rows " + str(valid_rows))
    return valid_rows


def check_cols(matrix):
    rebuilt_matrix = []
    col_list = []
    for col in range(len(matrix)):
        col_list = []
        for row in matrix:
            col_list.append(row[col])
        rebuilt_matrix.append(col_list)

    valid_cols = True
    for col in rebuilt_matrix:
        if check_repeats(col) == False:
            valid_cols = False
    #print("cols " + str(valid_cols))
    return valid_cols


def check_squares(matrix):
    rebuilt_matrix = []
    # get size of matrix
    row_size = len(matrix)
    col_size = len(matrix[0])

    square1_list = []
    square2_list = []
    square3_list = []

    if row_size == 9 and col_size == 9:
        count = 0
        for row in matrix:
            for col in range(3):
                square1_list.append(row[col])
                square2_list.append(row[col+3])
                square3_list.append(row[col+6])
                if count == 2 and col == 2:
                    rebuilt_matrix.append(square1_list)
                    rebuilt_matrix.append(square2_list)
                    rebuilt_matrix.append(square3_list)
                    square1_list = []
                    square2_list = []
                    square3_list = []
                    count = -1
            count += 1

    valid_squares = True
    for squares in rebuilt_matrix:
        if check_repeats(squares) == False:
            valid_squares = False
    #print("squares " + str(valid_squares))

    return valid_squares


def check_repeats(received_list):
    list = received_list.copy()
    occur = []
    while (list.count(0)):
        list.remove(0)

    for i in list:
        if i < 10:
            occur.append(list.count(i))
        else:
            return False

    if len(occur) == sum(occur):
        return True
    else:
        return False


def validate_sudoku(matrix):
    # Validate all squares rows and columns
    return check_rows(matrix) and check_cols(matrix) and check_squares(matrix)


def build_zero_list(matrix):
    row_index = 0
    for row in matrix:
        column_index = 0
        for item in row:
            if item == 0:
                zero_list.append([row_index, column_index])
            column_index = column_index + 1
        row_index = row_index + 1

    return zero_list


def solve_sudoku(matrix, index=0):
    row_index = zero_list[index][0]
    col_index = zero_list[index][1]

    current_val = matrix[zero_list[index][0]][zero_list[index][1]]
    current_val += 1
    matrix[zero_list[index][0]][zero_list[index][1]] = current_val

    for item in matrix:
        print(item)

    if current_val >= 10:
        matrix[zero_list[index][0]][zero_list[index][1]] = 0
        # oops, jump back
        solve_sudoku(matrix, index-1)
    else:
        if check_rows(matrix):
            if check_cols(matrix):
                if check_squares(matrix):
                    # value is good, jump to next empty position
                    solve_sudoku(matrix, index+1)
                else:
                    solve_sudoku(matrix, index)
            else:
                solve_sudoku(matrix, index)
        else:
            solve_sudoku(matrix, index)

    return matrix

sudoku = [
        [2, 5, 0, 0, 3, 0, 9, 0, 1],
        [6, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 3, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]
    ]

zero_list = []


if __name__ == '__main__':
    build_zero_list(sudoku)
    #solve_sudoku(sudoku)

    sys.setrecursionlimit(10000)
    threading.stack_size(20000000)
    thread = threading.Thread(target=solve_sudoku(sudoku))
    thread.start()
