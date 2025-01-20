import random
import time
import threading
from collections import deque

class Sensor:
    def __init__(self, id, print_queue):
        self.id = id
        self.print_queue = print_queue
        
    def send_data(self):
        while True:
            data = f"Data from sensor {self.id}: {random.randint(1, 100)}"
            self.print_queue.append(data)
            time.sleep(random.uniform(0.5, 2))  # send a random data every 0.5 to 2 seconds

class PrintQueue:
    def __init__(self):
        self.queue = deque()
        
    def print_data(self):
        while True:
            if self.queue:
                data = self.queue.popleft()
                print(data)
            time.sleep(0.1)  # check the queue every 0.1 seconds

if __name__ == "__main__":
    print_queue = PrintQueue()
    
    sensors = [Sensor(i, print_queue.queue) for i in range(5)]
    
    sensor_threads = [threading.Thread(target=sensor.send_data) for sensor in sensors]
    print_thread = threading.Thread(target=print_queue.print_data)
    
    for thread in sensor_threads:
        thread.start()
    
    print_thread.start()
    
    for thread in sensor_threads:
        thread.join()
    