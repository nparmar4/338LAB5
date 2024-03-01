# Code help from ChatGPT 

import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# QUESTION 1
class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

#QUESTION 2
class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is not None:
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            return None

    def is_empty(self):
        return self.head is None

#QUESTION 3
def random_list(length):
    tasks = []
    for _ in range(length):
        task = random.choices(["push", "pop"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

#QUESTION 4
def measure_array_stack(tasks):
    stack = ArrayStack()
    for task in tasks:
        if task == "push":
            stack.push(1)
        elif task == "pop":
            stack.pop()

def measure_linked_list_stack(tasks):
    stack = LinkedListStack()
    for task in tasks:
        if task == "push":
            stack.push(1)
        elif task == "pop":
            stack.pop()

array_times = []
linked_list_times = []


for _ in range(100):
    tasks = random_list(10000)
    array_time = timeit.timeit(lambda: measure_array_stack(tasks), number=1)
    linked_list_time = timeit.timeit(lambda: measure_linked_list_stack(tasks), number=1)
    array_times.append(array_time)
    linked_list_times.append(linked_list_time)

print("Array Times: ", array_times, "\n")
print("Linked List Times: ", linked_list_times)

#QUESTION 5
plt.hist(array_times, bins=20, alpha=0.5, label='Array Stack')
plt.hist(linked_list_times, bins=20, alpha=0.5, label='Linked List Stack')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Times for Array Stack vs Linked List Stack')
plt.legend()
plt.show()

# Both implementations generally have the same execution times. Accessing elements at the tail of an array 
# and accessing elements at the head of a linked list have the same time constant time complexity of O(1).
# They vary slightly, but they have the same general trend.