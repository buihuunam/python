#robot
class Robot:
    def __init__(self):
        self.position = [0, 0]#[x, y]
        self.direction = 'N' # N, E, S, W
        self.history = []   #stack to store the history of commands
    
    def move_forward(self):
        if self.direction == 'N':
            self.position[1] += 1
            
        elif self.direction == 'E':
            self.position[0] += 1
            
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'W':
            self.position[0] -= 1
        self.history.append('forward')
        print(f"Moved forward to {self.position}, facing {self.direction}")
        
    def move_backward(self):
        if self.direction == 'N':
            self.position[1] -= 1
            
        elif self.direction == 'E':
            self.position[0] -= 1
            
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'W':
            self.position[0] += 1
        self.history.append('backward')
        print(f"Moved backward to {self.position}, facing {self.direction}")
        
    def turn_left(self):
        dirs = ['N', 'E', 'S', 'W']
        idx = dirs.index(self.direction)
        self.direction = dirs[(idx + 1) % 4]
        self.history.append('left')
        print(f"Turned left to face {self.direction}, at {self.position}")
        
    def turn_right(self):
        dirs = ['N', 'E', 'S', 'W']
        idx = dirs.index(self.direction)
        self.direction = dirs[(idx + 1) % 4]
        self.history.append('right')
        print(f"Turned right to face {self.direction}, at {self.position}")
        
    def undo(self):
        if not self.history:
            print("No command to undo")
            return
        last_command = self.history.pop()
        print(f"Undoing {last_command}")
        if last_command == 'forward':
            self.move_backward()
        elif last_command == 'backward':
            self.move_forward()
        elif last_command == 'left':
            self.turn_right()
        elif last_command == 'right':
            self.turn_left()
            
    def display_status(self):
        print(f"Robot is at {self.position}, facing {self.direction}")
        
if __name__ == "__main__":
    robot = Robot()
    robot.move_forward()
    robot.turn_right()
    robot.move_forward()
    robot.turn_left()
    robot.move_backward()
    robot.display_status()
    
    print("\nUndoing last command")
    robot.undo()
    robot.undo()
    robot.display_status()