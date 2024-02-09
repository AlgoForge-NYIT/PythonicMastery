def bubble_sort(numbers):
    swapped = True
    while (swapped):
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True
    return numbers

# Test 1: Normal list
test_list_1 = [4, 2, 6, 5, 1, 3]
expected_result_1 = [1, 2, 3, 4, 5, 6]
print("Test 1 passed:", bubble_sort(test_list_1) == expected_result_1)

# Test 2: List already sorted
test_list_2 = [1, 2, 3, 4, 5]
expected_result_2 = [1, 2, 3, 4, 5]
print("Test 2 passed:", bubble_sort(test_list_2) == expected_result_2)

# Test 3: List with negative numbers
test_list_3 = [-3, -1, -2, 0, 2, 1]
expected_result_3 = [-3, -2, -1, 0, 1, 2]
print("Test 3 passed:", bubble_sort(test_list_3) == expected_result_3)
