def bfs(graph,start):
    queue = [start]
    visited = set()
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(f"Visit {vertex}")
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            print(f"Add '{vertex}' to visited set: {graph[vertex]}")
            print()
            
#simulate graph
graph = {
    "A": {"B","C"},
    "B": {"A","D","E"},
    "C": {"A","F"},
    "D": {"B"},
    "E": {"B","F"},
    "F": {"C","E"}
}
print ("BFS traversal starting from vertex 'A':")
bfs(graph,"A")