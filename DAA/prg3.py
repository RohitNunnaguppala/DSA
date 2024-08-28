import heapq

def merge_sorted_lists(lists):
    # Step 1: Initialize a min-heap
    min_heap = []
    
    # Step 2: Insert the first element of each list into the heap
    for i in range(len(lists)):
        if lists[i]:  # Check if the list is not empty
            heapq.heappush(min_heap, (lists[i][0], i, 0))  # (value, list_index, element_index)

    # Step 3: Extract the minimum element and push the next element from the same list
    sorted_output = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)  # Get the smallest element
        sorted_output.append(value)  # Add it to the output
        
        # If there is a next element in the same list, push it to the heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return sorted_output

# Example usage
sorted_lists = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50],
    [16, 18, 22, 28]
]

result = merge_sorted_lists(sorted_lists)
print(result)  # Output: [10, 15, 16, 18, 20, 22, 25, 27, 28, 29, 30, 32, 33, 35, 37, 39, 40, 45, 48, 50]