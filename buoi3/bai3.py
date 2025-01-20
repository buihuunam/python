def dfs(graph,start):
    stack = [start]
    visited = set()
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex,end=' ')
            visited.add(vertex)
            
            #add all neighbors of vertex to stack
            neighbors = reversed(graph[vertex])
            stack.extend(neighbors)
            print(f"đã đẩy các nút kề '{vertex}' vào stack: {list(neighbors)}")
            print()
            
#try
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS traversal starting from vertex 'A':")
dfs(graph,'A')
            