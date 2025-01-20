from collections import deque

class RequestQueue:
    def __init__(self):
        self.queue = deque()
        
    def add_request(self,request):
        self.queue.append(request)
        print(f"Add request {request}")
    
    def process_request(self):
        if self.queue:
            request = self.queue.popleft()
            print(f"Process request {request}")
            return request
        else:
            print("Queue is empty")
    def display_queue(self):
        print("Queue: ",list(self.queue))
        
if __name__ == "__main__":
    request_queue = RequestQueue()
    request_queue.add_request("Request 1")
    request_queue.add_request("Request 2")
    request_queue.add_request("Request 3")
    request_queue.display_queue()
    
    request_queue.process_request() 
    request_queue.display_queue()
    
    request_queue.process_request() 
    request_queue.display_queue()
    
    request_queue.process_request() 
    request_queue.display_queue()