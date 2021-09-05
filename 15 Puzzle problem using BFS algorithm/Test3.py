# opens the text file of nodes
txt_file = open("Test3.txt", "w+")

# Function to find empty tile location
def blank_tile_location(data):
    x = 0
    y = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] == 0:
                x = i
                y = j
    return x, y

# Defining function for move down action
def move_down(matrix, i, j):
    temp_arr = []
    for r in range(len(matrix)):
        t_a = []
        for t in matrix[r]:
            t_a.append(t)
        temp_arr.append(t_a)

    n = 0
    i_changed = i + 1
    # Checking the validity of points
    if i_changed >= 0 and i_changed < 4 and j >= 0 and j < 4:
        # Swapping the empty box to new location
        temp = temp_arr[i_changed][j]
        temp_arr[i_changed][j] = temp_arr[i][j]
        temp_arr[i][j] = temp
    else:
        n = n + 1
    return temp_arr, n

# Defining function for move up action
def move_up(matrix, i, j):
    temp_arr = []
    for r in range(len(matrix)):
        t_a = []
        for t in matrix[r]:
            t_a.append(t)
        temp_arr.append(t_a)

    n = 0
    i_changed = i - 1
    # Checking the validity of points
    if i_changed >= 0 and i_changed < 4 and j >= 0 and j < 4:
        # Swapping the empty box to new location
        temp = temp_arr[i_changed][j]
        temp_arr[i_changed][j] = temp_arr[i][j]
        temp_arr[i][j] = temp
    else:
        n = n + 1
    return temp_arr, n

# Defining function for move right action
def move_right(matrix, i, j):
    temp_arr = []
    for r in range(len(matrix)):
        t_a = []
        for t in matrix[r]:
            t_a.append(t)
        temp_arr.append(t_a)

    n = 0
    j_changed = j + 1
    # Checking the validity of points
    if i >= 0 and i < 4 and j_changed >= 0 and j_changed < 4:
        # Swapping the empty box to new location
        temp = temp_arr[i][j_changed]
        temp_arr[i][j_changed] = temp_arr[i][j]
        temp_arr[i][j] = temp
    else:
        n = n + 1
    return temp_arr, n

# Defining function for move right action
def move_left(matrix, i, j):
    temp_arr = []
    for r in range(len(matrix)):
        t_a = []
        for t in matrix[r]:
            t_a.append(t)
        temp_arr.append(t_a)

    n = 0
    j_changed = j - 1
    if i >= 0 and i < 4 and j_changed >= 0 and j_changed < 4:
        temp = temp_arr[i][j_changed]
        temp_arr[i][j_changed] = temp_arr[i][j]
        temp_arr[i][j] = temp

    else:
        n = n + 1

    return temp_arr, n

# Defining function for converting into characters for comparison
def conv(mat):
    # Converting values from 10-15 to A-F
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] < 10:
                mat[i][j] = mat[i][j]
            elif mat[i][j] == 10:
                mat[i][j] = 'A'
            elif mat[i][j] == 11:
                mat[i][j] = 'B'
            elif mat[i][j] == 12:
                mat[i][j] = 'C'
            elif mat[i][j] == 13:
                mat[i][j] = 'D'
            elif mat[i][j] == 14:
                mat[i][j] = 'E'
            elif mat[i][j] == 15:
                mat[i][j] = 'F'
    return mat

# Defining function to convert list to strings
def conv_string(temp_arr):
    e_s = ''
    list_temp = []
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr)):
            e_s = e_s + str(temp_arr[i][j])
    return e_s

# Defining function for converting characters to matrix
def char_to_mat(mat):
    for k in range(len(mat)):
        for i in range(len(mat[0])):
            for j in range(len(mat[0])):
                if mat[k][i][j] == 'A':
                    mat[k][i][j] = 10
                elif mat[k][i][j] == 'B':
                    mat[k][i][j] = 11
                elif mat[k][i][j] == 'C':
                    mat[k][i][j] = 12
                elif mat[k][i][j] == 'D':
                    mat[k][i][j] = 13
                elif mat[k][i][j] == 'E':
                    mat[k][i][j] = 14
                elif mat[k][i][j] == 'F':
                    mat[k][i][j] = 15
    return mat

# Function to solve the puzzle
def puzzle_solver(input_case):
    goal_mat = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]]

    append_mat = []
    # Converting goal state into characters
    goal_mat_t = conv(goal_mat)
    print(goal_mat_t)
    goal_mat_str = conv_string(goal_mat_t)
    # Converting the input into characters (A-F)
    input_case_t = conv(input_case)
    input_case_t_str = conv_string(input_case_t)
    # List to append all the possible matrices
    matrices = []
    matrices.append(input_case_t)
    print(matrices)
    stringss = []
    stringss.append(input_case_t_str)

    move_function = ["down", "up", "right", "left"]
    puzzle_solved = False
    find_mat_2 = []

    # creating a While loop until goal state is achieved
    while puzzle_solved == False:
        # print(matrices)
        find_mat = matrices.pop(0)
        i, j = blank_tile_location(find_mat)
        # Applying the move function
        for k in move_function:
            s = 0
            if k == "down":
                find_mat_2, s = move_down(find_mat, i, j)
                find_mat_2_str = conv_string(find_mat_2)
            elif k == "up":
                find_mat_2, s = move_up(find_mat, i, j)
                find_mat_2_str = conv_string(find_mat_2)
            elif k == "right":
                find_mat_2, s = move_right(find_mat, i, j)
                find_mat_2_str = conv_string(find_mat_2)
            elif k == "left":
                find_mat_2, s = move_left(find_mat, i, j)
                find_mat_2_str = conv_string(find_mat_2)
            # Copy flag to check the repeatability of nodes
            copy = False
            if s == 0:
                find_mat_2_str = conv_string(find_mat_2)
                for v in stringss:
                    if v == find_mat_2_str:
                        copy = True

                if copy == False:
                    matrices.append(find_mat_2)
                    stringss.append(find_mat_2_str)
                    append_mat.append(find_mat_2)
                    f = 0
                    if find_mat_2_str == goal_mat_str:
                        puzzle_solved = True
                        answr = find_mat_2
                        print("answer found:")
                        solved_ans = char_to_mat(append_mat)
                        f = f + 1
            if f > 0:
                break

    return solved_ans

# Input the test case
solved_puzzle = puzzle_solver([[0, 2, 3, 4],[ 1,5, 7, 8], [9, 6, 11, 12] , [13, 10, 14, 15]])

print(solved_puzzle)
# Saving the path in testX.txt file
txt_file.write("All the explored nodes from start to goal: \n\n")

for i in range(len(solved_puzzle)):
    txt_file.write("%s\n\n" %solved_puzzle[i])
