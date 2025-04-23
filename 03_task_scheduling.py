# 3. Task Scheduling Problem (Optimization)
# A software engineer has multiple tasks to complete. Each task has:
# • a deadline (day by which it must be finished),
# • an amount of time it takes to complete (in days).
# Write a Python function to:
# • Determine the maximum number of tasks the engineer can complete without missing
# deadlines.
# Input Example:
# tasks = [
# {'name': 'Task 1', 'deadline': 4, 'duration': 2},
# {'name': 'Task 2', 'deadline': 3, 'duration': 1},
# {'name': 'Task 3', 'deadline': 2, 'duration': 1},
# {'name': 'Task 4', 'deadline': 1, 'duration': 2},
# ]

#----------solution--------->
import heapq

def max_tasks(tasks):

    tasks.sort(key=lambda x: x['deadline'])
    
    max_heap = []  # We'll store negative durations to simulate a max-heap
    time_used = 0

    for task in tasks:
        duration = task['duration']
        deadline = task['deadline']
        
        if time_used + duration <= deadline:
            heapq.heappush(max_heap, -duration)
            time_used += duration
        elif max_heap and -max_heap[0] > duration:
            time_used += duration + heapq.heappop(max_heap)
            heapq.heappush(max_heap, -duration)
            time_used -= -max_heap[0]

    return len(max_heap)

# 🔧 Example
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

print("Maximum tasks that can be completed:", max_tasks(tasks))
