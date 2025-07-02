'''🔹 Task 7: Maze Solver with BFS and DFS
Design a 2D grid maze (start to goal). Use:
•	0 for free cell, 1 for wall
•	Start = (0,0), Goal = (n-1,n-1)
Implement:
•	BFS to find shortest path
•	DFS to find any path
Add visualization:
•	Print grid with path traced'''
from collections import deque
import copy

# Maze grid: 0 = free, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

n = len(maze)
start = (0, 0)
goal = (n-1, n-1)

# Possible moves: down, up, right, left
moves = [(1,0), (-1,0), (0,1), (0,-1)]

def print_maze(maze, path):
    # Mark path in maze copy
    maze_copy = copy.deepcopy(maze)
    for x, y in path:
        maze_copy[x][y] = '*'
    maze_copy[start[0]][start[1]] = 'S'
    maze_copy[goal[0]][goal[1]] = 'G'
    for row in maze_copy:
        print(' '.join(str(cell) for cell in row))
    print()

# BFS for shortest path
def bfs(maze, start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == goal:
            return path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# DFS for any path
def dfs(maze, start, goal):
    stack = []
    stack.append((start, [start]))
    visited = set()
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == goal:
            return path

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))
    return None

# Run both solvers and visualize
print("Maze:")
print_maze(maze, [])

print("BFS Shortest Path:")
bfs_path = bfs(maze, start, goal)
if bfs_path:
    print_maze(maze, bfs_path)
else:
    print("No path found.")

print("DFS Any Path:")
dfs_path = dfs(maze, start, goal)
if dfs_path:
    print_maze(maze, dfs_path)
else:
    print("No path found.")


