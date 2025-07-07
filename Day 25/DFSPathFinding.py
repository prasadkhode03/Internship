def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            if node == goal:
                return path

            for neighbor in reversed(graph.get(node, [])):  # reverse for consistent ordering
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

            visited.add(node)

    return None

print("DFS Path:", dfs(graph, 'A', 'F'))
