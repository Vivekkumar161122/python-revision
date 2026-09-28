#bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap

numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print(numbers) # Output: [11, 12, 22, 11, 90]

=======================================================================================

# Sort Character Alphabetically
def bubble_sort_chars(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

    chars = ["d", "a", "e", "b", "c"]
    print(buble_sort_chars(chars))
# Output: ['a', 'b', 'c', 'd',]

========================================================================================

# Sort in Descending Order
def bubble_sort_decending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Change comparison operator to '<'
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

nums = [5, 1, 4, 2, 8]
print(bubble_sort_descending(nums))
# Output: [8, 5, 4, 2, 1]

