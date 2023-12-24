class Queue:
def __init__(self):
self.items = []
def is_empty(self):
return len(self.items) == 0
def enqueue(self, item):
self.items.append(item)
def dequeue(self):
if not self.is_empty():
return self.items.pop(0)
else:
print("Queue is empty.")
def size(self):
return len(self.items)
if __name__ == "__main__":
my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print("Queue size:", my_queue.size())
print("Dequeue:", my_queue.dequeue())
print("Queue size after dequeue:", my_queue.size())
