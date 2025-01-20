from collections import deque
import threading
import time

class CommandQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def enqueue(self, command):
        with self.lock:
            self.queue.append(command)
            print(f"Enqueued {command}")
    
    def dequeue(self):
        with self.lock:
            if self.queue:
                command = self.queue.popleft()
                print(f"Dequeued {command}")
                return command
            else:
                print("Queue is empty")
                return None
    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0
        
class RobotController:
    def __init__(self, command_queue):
        self.command_queue = command_queue
        self.thread = threading.Thread(target=self.process_commands,daemon=True)
        self.thread.start()
        
    def process_commands(self):
        while True:
            if not self.command_queue.is_empty():
                command = self.command_queue.dequeue()
                self.execute_command(command)
            else:
                time.sleep(1)
                
    def execute_command(self, command):
        if command == 'forward':
            print("Moving forward")
        elif command == 'backward':
            print("Moving backward")
        elif command == 'left':
            print("Turning left")
        elif command == 'right':
            print("Turning right")
        elif command == 'stop':
            print("Stopping")
        else:
            print(f"Unknown command {command}")
            time.sleep(2)
            
#simulate the robot controller
def main():
    command_queue = CommandQueue()
    controller = RobotController(command_queue)
    
    #add some commands to the queue
    commands = ['forward', 'backward', 'left', 'right', 'stop']
    for command in commands:
        command_queue.enqueue(command)
        time.sleep(0.5)#wait for half a second
    
    #keep the main thread alive    
    time.sleep(15)
        
if __name__ == '__main__':
    main()