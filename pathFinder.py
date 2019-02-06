maze = """\
#################
#       ###    ##
# #### #### ## ##
# ####      ## ##
# ############ ##
# *  ## #       #
####      #### ##
#################
"""

def init_grid(e): #sets the maze as the matrix
    global grid
    grid = [] #makes the grid into a list
    maze_list = [] #auxiliary list
    for i in e: #the index in the maze
        if i in ['#', ' ', '*', '.']: #if the character of the indexed item matches one in the list
            maze_list.extend(i) #added to the list as individual items
        else:
            grid.append(maze_list) #add the list as a whole element
            maze_list = []
 
def path_finder (y, x):
    if grid[y][x] == '*': #checks if target is reached
        print_grid()
        input('\nPress any key for another solution')
        return True
    if grid[y][x] != ' ': #boundary check, already occupied block
        return False
    grid[y][x] = '.' #marking traversed territory
    path_finder(y-1,x) #checks every direction for possible route
    path_finder(y,x-1)
    path_finder(y+1,x)
    path_finder(y,x+1) 
    grid[y][x] = ' ' #unmark traversed territory that is not a solution
    return False

def solve(y,x): #checks if there is a possible solution
    if(path_finder(y,x) == False):
        print('Sorry! No solution(s) found\n')

def print_grid(): #function to display the maze in the shell
    print('\nHere is the maze \n')
    for row in grid:
        for col in row:
            if col in ['#', ' ', '*', '.']:
                print(col, end='')
        print()

init_grid(maze) #sets the maze to the grid on initialising the program
