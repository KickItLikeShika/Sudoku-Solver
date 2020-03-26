grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def display_gird(gird):
    for i in range(len(gird)):
        if i % 3 == 0 and i != 0:
            print("-------------------------------")
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == len(grid[0]) - 1:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end=" ")

def find_empty_field(grid):
    """Finding the empty field."""
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) # The position of the element

    return None

def check_validation(grid, num, pos):
    """Check if the number we will insert is valid"""
    # Checking the row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking the column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking 3*3 grid
    """This is method is to find check each 3*3 grid, 
    it divides the row and col by three and gets the int number,
    so the numbers of the sub-grids bercome like that(first sub-gird
    is(0, 0), the second is (0, 1), the third is (0, 2), the fourth is
    (1, 0), etc....). Then the range of the numbers will be [0,2],
    and when you muliply the number by 3 you then get the position of
    each element."""
    grid_x = pos[1] // 3
    grid_y = pos[0] // 3

    for i in range(grid_y*3, grid_y*3 + 3):
        for j in range(grid_x*3, grid_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(grid):
    """Backtracking algorithm."""
    emtpy = find_empty_field(grid)
    if not emtpy:
        return True
    else:
        row, col = emtpy
    
    for i in range(1, 10):
        if check_validation(grid, i, (row, col)):
            grid[row][col] = i

            if solve(grid):
                return True
                
            grid[row][col] = 0

    return False


display_gird(grid)
solve(grid)
print("----------------------------")
print("----------SOLVED!-----------")
display_gird(grid)