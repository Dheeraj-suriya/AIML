# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            # Print each visited node
            print("Visited:", current)

            if current == goal:
                break

            # Push neighbors in reverse alphabetical order
            for neighbor in sorted(graph[current], reverse=True):
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = current
                    stack.append(neighbor)

    # Find path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("\nDFS Traversal Path:")
    print(" -> ".join(path))

# Main
dfs(graph, "Alice", "Bob")