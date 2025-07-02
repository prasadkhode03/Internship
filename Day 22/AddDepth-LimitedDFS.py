'''Task 5: Add Depth-Limited DFS (DLS)
Modify your DFS code to support depth-limiting.
•	Try depth = 2, 3
•	Observe how it avoids infinite loops'''
def dls(graph, start, goal, limit):
    stack = [(start, 0)]  # stack stores (node, depth)
    visited = []

    while stack:
        print(f"Current stack: {stack}")  # Show stack at each step

        node, depth = stack.pop()

        if node not in visited:
            visited.append(node)
            print(f"Visited: {visited}")

            if node == goal:
                print(f"\nGoal node '{goal}' found at depth {depth}!")
                break

            if depth < limit:
                neighbors = graph[node]
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1))

    print(f"\nFinal visited order (depth limit {limit}): {visited}")

# Example graph (adjacency list)
graph = {
    'H': ['I', 'J'],
    'I': ['K', 'L'],
    'J': ['M'],
    'K': [],
    'L': ['N'],
    'M': [],
    'N': []
}

# Test DLS with different depth limits
print("\n--- DLS with depth = 2 ---")
dls(graph, 'H', 'M', limit=2)

print("\n\n--- DLS with depth = 3 ---")
dls(graph, 'H', 'M', limit=3)

