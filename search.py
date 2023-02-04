import time
a = time.time()
def search(matrix, target, row, col, visited):
    #print(f"searching {row} {col} and value there is {matrix[row][col]}")
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or visited[row][col]:
        return False
    if matrix[row][col] == target:
        return True
    #print(f"searching {row} {col} and value there is {matrix[row][col]}")
    visited[row][col] = True
    found = search(matrix, target, row + 1, col, visited) or \
            search(matrix, target, row - 1, col, visited) or \
            search(matrix, target, row, col + 1, visited) or \
            search(matrix, target, row, col - 1, visited)
    visited[row][col] = False
    return found

def search_matrix(matrix, target):
    if not matrix:
        return False
    visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if search(matrix, target, i, j, visited):
                return True
    return False
'''
    This script uses the search function to traverse the matrix in a depth-first manner and
    checks if the target value is found. The visited array is used to keep track of which 
    cells have already been visited to avoid repeating the same cell multiple times.
    The search_matrix function initializes the visited array and starts the search at each 
    cell in the matrix.
'''
# Test cases
matrix = [    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 20],
    [18, 21, 23, 26, 0]
]

print(search_matrix(matrix, 5)) # True
print(search_matrix(matrix, 20)) # False
print(search_matrix(matrix, 0)) # False
'''
This code creates a test matrix and tests the search_matrix function with 
three different targets, 5, 20, and 0, and prints the results of each search. 
The expected output of this code is True False False.
'''

print(time.time() - a)