from collections import deque

def dfs(grid, start, goal):
    stack = deque()
    stack.append(start)
    visited = set()
    parent = {}
    
    while stack:
        current = stack.pop()
        if current == goal:
            break
        if current in visited:
            continue
        visited.add(current)
        
        # get location of neighbors up, down, left, right
        neighbors = get_neighbors(grid, current)
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                parent[neighbor] = current
                
    # checking if a path is found or not
    if goal not in parent and start != goal:
        print("No path found")
        return None
        
    # build path from goal to start
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent.get(current, start)
    path.append(start)
    path.reverse()
    return path
    
def get_neighbors(grid, position):
    x, y = position
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if grid[new_x][new_y] == "O":
                neighbors.append((new_x, new_y))
    return neighbors

# simulate grid
if __name__ == "__main__":
    # 1: obstacle, O: destination
    grid = [
        ["O", "O", "O", "O", "O"],
        ["1", "1", "O", "1", "O"],
        ["O", "O", "O", "1", "O"],
        ["O", "1", "1", "1", "O"],
        ["O", "O", "O", "O", "O"]
    ]
    start = (0, 0)
    goal = (4, 4)
    path = dfs(grid, start, goal)
    if path:
        print("Path found: ")
        print(path)