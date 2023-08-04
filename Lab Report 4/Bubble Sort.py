def bubble_sort(arr):
    n = len(arr)
    total_loops = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            total_loops += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, total_loops


input_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array, loops = bubble_sort(input_array)
print("Sorted Array:", sorted_array)
print("Total Loops:", loops)
