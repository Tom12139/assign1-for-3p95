import random

def random_test_case_generator(max_length=100, max_value=1000): # generate a random test case
    length = random.randint(0, max_length) # generate a random length
    return [random.randint(0, max_value) for _ in range(length)] # generate a random array

def quick_sort(arr): # quick sort algorithm
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

for i in range(10):  # run with 10 different test cases
    test_case = random_test_case_generator() # generate a random test case
    print(f"Test case {i+1}:")
    print(f"Input array: {test_case}") # print the input array
    sorted_array = quick_sort(test_case.copy()) # sort the array
    print(f"Output array: {sorted_array}")
    print(f"Test passed: {sorted_array == sorted(test_case)}\n") # check if the array is sorted correctly
