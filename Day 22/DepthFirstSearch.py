#DFS Code
'''

        H
      /   \
     I     J
    / \     \
   K   L     M
        \
         N
         
'''
graph = {
    "H" : ["I", "J"],
    "I" : ["K", "L"],
    "J" : ["M"],
    "K" : [],
    "L" : ["N"],
    "M" : [],
    "N" : []
}

def dfs(graph, start, goal):
    stack = [start]
    visited = []

    while stack:
        print(f"Current stack: {stack}") 

        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(f"Visited: {visited}")  

            if node == goal:
                print(f"\nGoal node '{goal}' found!")
                break
            neighbors = graph[node]
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

    print(f"\nFinal visited order: {visited}")

start = "H"
goal = "M"
dfs(graph, start, goal)
 