class MinHeap:
def __init__(self):
self.heap = []
def push(self, value):
self.heap.append(value)
self._heapify_up()
def pop(self):
if len(self.heap) == 0:
return None
if len(self.heap) == 1:
return self.heap.pop()
root = self.heap[0]
self.heap[0] = self.heap.pop()
self._heapify_down()
return root
def _heapify_up(self):
index = len(self.heap) - 1
while index > 0:
parent_index = (index - 1) // 2
if self.heap[index] < self.heap[parent_index]:
self.heap[index], self.heap[parent_index] = (
self.heap[parent_index],
self.heap[index],
)
index = parent_index
else:
break
def _heapify_down(self):
index = 0
while True:
left_child_index = 2 * index + 1
right_child_index = 2 * index + 2
min_index = index
if (
left_child_index < len(self.heap)
and self.heap[left_child_index] < self.heap[min_index]
):
min_index = left_child_index
if (
right_child_index < len(self.heap)
and self.heap[right_child_index] < self.heap[min_index]
):
min_index = right_child_index
if min_index != index:
self.heap[index], self.heap[min_index] = (
self.heap[min_index],
self.heap[index],
)
index = min_index
else:
break
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)
print("Min-Heap:")
while len(heap.heap) > 0:
print(heap.pop())
