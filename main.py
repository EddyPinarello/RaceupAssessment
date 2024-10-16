from collections import deque

# Function to extract matrices from file
def extract_matrices_from_file(file_path):
    matrices = [] # List of all the matrices collected
    current_matrix = [] 

    with open(file_path, 'r') as file: # Open file
        for line in file:
            line = line.strip() # For every line remove white spaces
            
            if not line: # Case when we reached the bottom of one matrix
                if current_matrix:
                    matrices.append(current_matrix) # So we can append in the list of matrices
                    current_matrix = []  # Reset the current matrix
            else:
                current_matrix.append(list(line)) 
        
        if current_matrix: # At the end of for if still have a remaning matrix, append it
            matrices.append(current_matrix)

    return matrices 


# Hashmap with the directions allowed in the matrix  
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

# Find the start 'S' and the end 'E' in the maze
def find_start_and_end(matrix):
    start = end = None
    for r, row in enumerate(matrix):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
            elif char == 'E':
                end = (r, c)
    return start, end

# Check if the move is valid
def is_valid_move(matrix, r, c):
    rows, cols = len(matrix), len(matrix[0])
    return 0 <= r < rows and 0 <= c < cols and matrix[r][c] != '#'

# BFS to solve the maze
def solve_maze(matrix):
    start, end = find_start_and_end(matrix)

    if not start or not end:
        return "Invalid maze: Start or End point missing."

    queue = deque([(start, [])])
    matrix[start[0]][start[1]] = '#'  # Mark start as visited

    while queue:
        (current_r, current_c), path = queue.popleft()
        
        # If we reach the exit, return the path
        if (current_r, current_c) == end:
            return path
        
        # Explore all possible directions
        for direction, (dr, dc) in DIRECTIONS.items():
            new_r, new_c = current_r + dr, current_c + dc
            
            if is_valid_move(matrix, new_r, new_c):
                matrix[new_r][new_c] = '#'  # Mark new position as visited
                queue.append(((new_r, new_c), path + [direction]))
    
    return "No solution exists."


# Run the code and store the solutions in a list of lists
file_path = 'inputs.txt'  
matrices = extract_matrices_from_file(file_path)
solutions = []

# Solve each matrix and store the direction in solution
for matrix in matrices:
    solution = solve_maze(matrix)
    solutions.append(solution)

# Print all solutions
for i, solution in enumerate(solutions):
    print(f"Solution for maze {i + 1}: {solution}")