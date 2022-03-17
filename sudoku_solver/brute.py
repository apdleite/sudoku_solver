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
    # d=[i for i in received_list if i!=0]
    # return len(set(d))==len(d)
    d=received_list.copy()
    occur = []
    while (d.count(0)):
        d.remove(0)

    for i in d:
        if i < 10:
            occur.append(d.count(i))
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
    #list comprehension
    # return [[r,c] for r in range(9) for c in range(9) if matrix[r][c] == 0]
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
    while index<len(zero_list):
        row_index = zero_list[index][0]
        col_index = zero_list[index][1]

        matrix[row_index][col_index]+=1

        for item in matrix:
            print(item)
        print()
        if matrix[row_index][col_index] >= 10:
            matrix[row_index][col_index] = 0
            # oops, jump back
            return False
        else:
            if check_rows(matrix) and check_cols(matrix) and check_squares(matrix):
                # value is good, jump to next empty position
                if solve_sudoku(matrix, index+1):
                    return True
    return True



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
sudoku2= [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
zero_list = []


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    build_zero_list(sudoku)
    solve_sudoku(sudoku)
