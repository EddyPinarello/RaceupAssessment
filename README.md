# Maze Solver (BFS)

This project shows how to solve a maze using the Breadth-First Search (BFS) algorithm. The maze is a matrix, and the goal is to find a path from the start to the end point, avoiding obstacles.

## Approach

### Why BFS?

BFS is an ideal algorithm for solving maze problems, especially when looking for the shortest path. Here's why:

- **Shortest path guarantee**: BFS explores all possible paths from the start, one step at a time, ensuring that the first time we reach the end, we've found the shortest path.
- **Systematic exploration**: It checks all neighboring cells before moving further into the maze, making it thorough and reliable.
- **Termination**: BFS will either find the shortest path or confirm that no solution exists.

### How BFS Works

BFS uses a **queue** to manage the points to explore next. The process follows these steps:

1. **Start from the initial point**: Mark the start cell as visited.
2. **Explore neighbors**: Check neighboring cells (up, down, left, right), adding valid ones to the queue.
3. **Track the path**: Keep track of the direction taken to reach each new cell.
4. **Continue until solved**: Repeat until the end point is reached, or the queue is empty (no path exists).
<img src="https://github.com/user-attachments/assets/069e5ff7-50b3-49ec-9ed1-6669ed3adf44" alt="image description" width="300"/>


### Why Use a Queue?

A **queue** is essential for BFS because it follows the **First In, First Out (FIFO)** principle. This ensures that the algorithm explores the maze evenly, processing the earliest discovered positions first and finding the shortest path.

Each time we explore a cell, we add its neighbors to the back of the queue. This guarantees that we expand outward from the start point, layer by layer.

## Optimization

Initially, to track visited cells, I used a separate set: `visited = set()`. This set stored the coordinates of every visited cell. While this method worked, it introduced memory overhead because I needed to store each visited cell separately.

#### Improved Approach

To optimize memory usage, I modified the algorithm to mark visited cells **directly in the maze matrix** by replacing their values with `'#'` (representing an obstacle). This eliminated the need for the separate `visited` set.
Instead of storing visited cells in a separate set (O(N) space complexity, where N is the number of cells), I reuse the maze itself to track visited cells, reducing memory usage to **O(1)**.

This optimization significantly improves performance, especially for larger mazes, while maintaining the correctness and efficiency of the BFS algorithm.

With this optimized BFS approach, the maze-solving algorithm is both memory-efficient and simple, ensuring the shortest path is found effectively.

## Time and Memory Complexity 
The BFS algorithm looks for a path from "S" (start) to "E" (end) in the maze.

- **Time Complexity:** O(n * m)  
  The algorithm checks each cell in the maze once, where `n` is the number of rows and `m` is the number of columns.

- **Space Complexity:** O(n * m)  
  The queue used in BFS can hold up to `n * m` cells in the worst case.
## Core Code Steps

### 1. Parsing Example Matrices from `.txt`

The following function reads a file and extracts matrices that represent the maze. Each matrix is separated by an empty line in the `.txt` file.

```python
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

```

### 2. HashMap with Directions Allowed in the Matrix

This dictionary defines the possible directions (up, down, left, right) and the corresponding changes in row and column indices.

```python
# Hashmap with the directions allowed in the matrix
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}
```

### 3. Functions to Find Start and End Points and Validate Moves

These functions help find the start (S) and end (E) coordinates in the matrix, and check whether a move to a new position is valid (i.e., not out of bounds or into an obstacle).

```python
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

```

### 4. BFS Algorithm to Solve the Maze

The BFS algorithm searches for the path from the start to the end point, using a queue to explore the maze level by level. It returns the sequence of directions to follow or a message if no solution exists.

```python
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

```
