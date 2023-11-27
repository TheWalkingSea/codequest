import sys
from typing import List, Tuple

def getWalls(maze: List[List[str]], row: int, col: int) -> List[str]:
    """Gets all the walls from the cell, represented as a char

    Parameters:
    maze(List[List[str]]): The maze to retrieve the walls from
    row(int): The row of the cell
    col(int): The column of the cell

    Returns:
    (List[str]): A list of characters of the wall sorted by top, right, bottom, left

    """
    return [ maze[row-1][col], maze[row][col+2], maze[row+1][col], maze[row][col-1] ]
    

def isCritical(top: str, right: str, bottom: str, left: str) -> int:
    """Checks if the square is an entrance or an exit

    Parameters:
    top(str): One letter character that represents a wall of the cell
    right(str): One letter character that represents a wall of the cell
    bottom(str): One letter character that represents a wall of the cell
    left(str): One letter character that represents a wall of the cell

    Returns:
    (int): 0 if it is not critical, 1 if it's an entrance, 2 if it's an exit

    """
    # match top:
    #     case 'v':
    #         return 1 # Entrance
    #     case '^':
    #         return 2 # Exit
    # match bottom:
    #     case '^':
    #         return 2 # Entrance
    #     case 'v':
    #         return 1 # Exit
    # match right:
    #     case '<':
    #         return 1 # Entrance
    #     case '>':
    #         return 2 # Exit
    # match left:
    #     case '>':
    #         return 1 # Entrance
    #     case '<':
    #         return 2 # Exit
    if top == 'v' or bottom == '^':
        return 1
    if top == '^' or bottom == 'v':
        return 2
    if right == '<' or left == '>':
        return 1
    if right == '>' or left == '<':
        return 2
    return 0

def getNeighbors(maze: List[List[str]], visited: List[Tuple[int, int]], row: int, col: int) -> List[Tuple[int, int]]:
    """Retrieves the cells that can be accessed nearby

    Parameters:
    maze(List[List[str]]): The maze to retrieve the walls from
    visited(List[Tuple[int, int]]): List of visited squares to ignore
    row(int): The row of the cell
    col(int): The column of the cell

    Returns:
    (List[Tuple[int, int]]): A list of indexes (row, col) of nearby cells that are not 
                             blocked by a wall. Default to (-1, -1)

    """
    open = [(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
    top, right, bottom, left = getWalls(maze, row, col)
    if row >= 1 and top == " " and (row-2, col) not in visited: # Top
        open[0] = (row-2, col)
    if col <= len(maze[0])-3 and right == " " and (row, col+3) not in visited: # Right; Subtract 3 to get to the left side of the cell
        open[1] = (row, col+3)
    if row <= len(maze)-2 and bottom == " " and (row+2, col) not in visited: # Bottom
        open[2] = (row+2, col)
    if col >= 1 and left == " " and (row, col-3) not in visited: # Left
        open[3] = (row, col-3)
    return open

    

def main(stdin: List[List[str]]):
    visited = list()
    startPos = tuple()
    exitPos = tuple()
    for row in range(1, len(stdin), 2):
        for column in range(1, len(stdin[0]), 3):
            crit = isCritical(*getWalls(stdin, row, column))
            if (crit == 1):
                startPos = (row, column)
            elif (crit == 2):
                exitPos = (row, column)
    cnt = 1
    next = getNeighbors(stdin, visited, *startPos)
    flag = True
    while (flag):
        cnt += 1
        pendingCells = list() # New list of next
        for cell in next:
            if cell == (-1, -1):
                continue
            if cell == exitPos:
                flag = False
            visited.append(cell) # Append to visited
            for neighbor in getNeighbors(stdin, visited, *cell):
                pendingCells.append(neighbor)
        if pendingCells:
            next = pendingCells
        else:
            return -1

    return cnt


def getInput() -> str:
    """Returns the standard output

    Returns:
    (str): The std output

    """
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    cases = int(getInput())
    for caseNum in range(cases):
        height, width = tuple(map(int, getInput().split(" ")))
        mazeInput = [getInput() for _i in range(height)]
        print(main(mazeInput))
        
