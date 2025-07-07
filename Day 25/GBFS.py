import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def greedy_bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    heap = [(manhattan(start, goal), [start])]

    while heap:
        _, path = heapq.heappop(heap)
        x, y = path[-1]

        if (x, y) == goal:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_path = path + [(nx, ny)]
                heapq.heappush(heap, (manhattan((nx, ny), goal), new_path))

    return None
