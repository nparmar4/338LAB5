#Q1:
import sys


def mergeSort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    arr1 = arr[low:mid+1]
    arr2 = arr[mid+1:high+1]

    i = 0
    j = 0
    k = low

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            j += 1
            k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1

class PriorityQueueMerge:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        merge_sort(self.queue, 0, len(self.queue)-1)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0


#Q2:
class PriorityQueueSorting:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        if len(self.queue) == 0:
            self.queue.append(item)
        else:
            inserted = False
            for i in range(len(self.queue)):
                if item <= self.queue[i]:
                    self.queue.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

#Q3:
import random


def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7:  
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

#Q4:
import timeit


def measure_performance(priority_queue_class):
    total_time = 0
    for _ in range(100):
        tasks = generate_random_tasks()
        pq = priority_queue_class()
        start_time = timeit.default_timer()
        for task in tasks:
            if task[0] == "enqueue":
                pq.enqueue(task[1], random.randint(1, 1000))  
            else:
                pq.dequeue()
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / 100

sorted_pq_time = measure_performance(PriorityQueueSorting)
merge_sort_pq_time = measure_performance(PriorityQueueMerge)

print("Sorted Priority Queue Average Time:", sorted_pq_time)
print("Merge Sort Priority Queue Average Time:", merge_sort_pq_time)



#Q5:
'''The Merge Sort Priority Queue implementation is slightly faster on average compared to the 
Sorted Priority Queue implementation. This is because the Sorted Priority Queue implementation 
incurs overhead from shifting elements when inserting new elements into the sorted array, 
while the Merge Sort Priority Queue implementation postpones sorting it until it is necessary and 
efficiently sorts the array using merge sort when needed. Therefore, for larger arrays, 
the Merge Sort Priority Queue performs better due to the efficiency of merge sort.
'''
