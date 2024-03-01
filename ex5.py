class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, element):
        if (self.rear + 1) % self.size == self.front:
            print("enqueue None")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        print(f"enqueue {element}")

    def dequeue(self):
        if self.front == -1:
            print("dequeue None")
            return None
        elif self.front == self.rear:
            element = self.queue[self.front]
            self.front = self.rear = -1
            print(f"dequeue {element}")
            return element
        else:
            element = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(f"dequeue {element}")
            return element

    def peek(self):
        if self.front == -1:
            print("peek None")
            return None
        else:
            print(f"peek {self.queue[self.front]}")
            return self.queue[self.front]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, element):
        new_node = Node(element)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def dequeue(self):
        if self.head is None:
            print("dequeue None")
            return None
        elif self.head.next == self.head:
            element = self.head.data
            self.head = None
            print(f"dequeue {element}")
            return element
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            element = self.head.data
            temp.next = self.head.next
            self.head = self.head.next
            print(f"dequeue {element}")
            return element

    def peek(self):
        if self.head is None:
            print("peek None")
            return None
        else:
            print(f"peek {self.head.data}")
            return self.head.data


operations = []

# Enqueue 20 elements
for i in range(1, 21):
    operations.append(("enqueue", i))

# Dequeue 20 elements
for i in range(20):
    operations.append(("dequeue", None))

# Peek 20 times
for i in range(20):
    operations.append(("peek", None))

# Test the CircularQueue implementation with the above operations
cq = CircularQueue(20)
for op, arg in operations:
    if op == "enqueue":
        cq.enqueue(arg)
    elif op == "dequeue":
        cq.dequeue()
    elif op == "peek":
        cq.peek()

#this code was generated using chatGPT but was modified to provide accurate results/output