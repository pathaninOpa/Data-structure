def counting_sort(arr):
    max_value = max(arr)
    count = [0] * (max_value + 1)

    # Count occurrences of each element
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

A = [1, 4, 1, 2, 7, 5, 2]
result_counting_sort = counting_sort(A)
print(result_counting_sort)


            
