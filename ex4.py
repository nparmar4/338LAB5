import random
import timeit
import matplotlib.pyplot as plt

# QUESTION 1
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        
#QUESTION 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if self.head:
            current = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current

#QUESTION 3
def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        if random.random() < 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

#QUESTION 4
def measure_performance(queue_type):
    total_times = []
    for _ in range(100):
        tasks = generate_random_tasks()
        queue = queue_type()

        start_time = timeit.default_timer()
        for task in tasks:
            if task == 'enqueue':
                queue.enqueue(1)
            else:
                queue.dequeue()
        end_time = timeit.default_timer()

        total_times.append(end_time - start_time)

    return total_times

if __name__ == "__main__":
    array_times = measure_performance(ArrayQueue)
    linked_list_times = measure_performance(LinkedListQueue)

    print("ArrayQueue times:", array_times)
    print("LinkedListQueue times:", linked_list_times)

#QUESTION 5

plt.hist(array_times, bins=20, alpha=0.5, label='ArrayQueue')
plt.hist(linked_list_times, bins=20, alpha=0.5, label='LinkedListQueue')
plt.legend(loc='upper right')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Queue Implementation Performance')
plt.show()
