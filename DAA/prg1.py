import numpy as np
import matplotlib.pyplot as plt
import time

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Generate a k-nearly sorted array
def generate_k_nearly_sorted_array(n, k):
    arr = np.arange(n)
    for i in range(k):
        # Swap random elements within the first k elements
        idx1, idx2 = np.random.randint(0, n), np.random.randint(0, n)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

# Complexity analysis
sizes = [100, 200, 300, 400, 500]
insertion_times = []
bubble_times = []

for size in sizes:
    arr = generate_k_nearly_sorted_array(size, 10)  # k = 10
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_times.append(time.time() - start_time)

    arr = generate_k_nearly_sorted_array(size, 10)
    start_time = time.time()
    bubble_sort(arr.copy())
    bubble_times.append(time.time() - start_time)

# Plotting the results
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, bubble_times, label='Bubble Sort', marker='x')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Time Complexity Analysis')
plt.legend()
plt.grid()
plt.show()