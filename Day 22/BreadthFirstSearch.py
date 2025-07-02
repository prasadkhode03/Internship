'''🔁 Level 2 – Code Implementation
🔹 Task 4: Write BFS and DFS in Python
Use an adjacency list representation.
•	Find a goal node in a graph
•	Trace visited nodes
Add:
•	Print statement to show queue/stack
•	Print visited nodes in order'''
#Code for BFS
'''        A
         /   \
        B     C
       / \   / \
      D   E F   G'''

from collections import deque

graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F", "G"],
    "D" : [],
    "E" : [],
    "F" : [],
    "G" : []
}

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current == goal:
            print(f"\nFound the {goal} node.\nCongrats, you reached the goal.")
            print("\nVisited Nodes Order : ", visited)
            return True
        if current not in visited:
            print(f"\nVisiting the node : {current}")
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        print("Queue Stack : ", queue)
    print("Goal not found.")
    return False

start = "A"
goal = "G"
bfs(graph, start, goal)