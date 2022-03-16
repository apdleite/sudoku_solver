def check_row(matrix, row, iteration):
    # print(matrix[row])
    # print(matrix[row].count(iteration))
    if matrix[row].count(iteration) <= 0:
        return True
    else:
        return False


def check_col(matrix, col, iteration):
    col_list = []
    for m in matrix:
        col_list.append(m[col])

    if col_list.count(iteration) <= 0:
        return True
    else:
        return False


def zero_check(matrix):
    n_zeros = 0
    for i in matrix:
        n_zeros = n_zeros + i.count(0)
    if n_zeros == 0:
        return False
    else:
        return True


def solve_square(matrix, count=0):
    # todo - start by square with higher elements filled
    # ROWS       COLS
    square_def = [
        [[0, 1, 2], [0, 1, 2]],
        [[0, 1, 2], [3, 4, 5]],
        [[0, 1, 2], [6, 7, 8]],
        [[3, 4, 5], [0, 1, 2]],
        [[3, 4, 5], [3, 4, 5]],
        [[3, 4, 5], [6, 7, 8]],
        [[6, 7, 8], [0, 1, 2]],
        [[6, 7, 8], [3, 4, 5]],
        [[6, 7, 8], [6, 7, 8]]
    ]
    count += 1
    if zero_check(matrix):
        for square_pos in square_def:
            square_list = []
            filled_list = []
            empty_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            position = 0
            position_list = []
            search_rows = square_pos[0]
            search_cols = square_pos[1]
            for r in search_rows:
                for c in search_cols:
                    square_list.append(matrix[r][c])
                    if matrix[r][c] != 0:
                        filled_list.append(matrix[r][c])

            for i in range(len(filled_list)):
                empty_list.remove(filled_list[i])

            for r in search_rows:
                for c in search_cols:
                    if matrix[r][c] == 0:
                        # print("Checking position " + str(str(r) + "," + str(c)))
                        iteration_list = []
                        for i in empty_list:
                            if check_row(matrix, r, i):
                                # print(str(i) + " not found on row " + str(r))
                                if check_col(matrix, c, i):
                                    # print(str(i) + " not found on col" + str(c))
                                    iteration_list.append(i)
                                    # print(iteration_list)
                                # else:
                                    # print(str(i) + " FOUND on COL " + str(r))
                            # else:
                                # print(str(i) + " FOUND on ROW " + str(r))
                        position_list.append([[r, c], iteration_list])

            # check which element has only 1 distinct entry
            for i in empty_list:
                counter = 0
                for n in position_list:
                    counter += n[1].count(i)
                    if n[1].count(i) == 1:
                        position = n[0]
                if counter == 1:
                    # print("Place " + str(i) + " at pos " + str(position))
                    matrix[position[0]][position[1]] = i
                # else:
                # print("counter equals to " + str(counter))
        for item in matrix:
            print(item)
        solve_square(matrix, count)
    else:
        print("solved in " + str(count) + " recursive calls.")

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

if __name__ == '__main__':
    sudoku = solve_square(sudoku)
    for item in sudoku:
        print(item)
