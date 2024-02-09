def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        curr_num = numbers[i]
        j = i - 1
        while j >= 0 and curr_num < numbers[j]:
            numbers[j + 1] = numbers[j] # overwrites numbers[i] in shifting process
            j -= 1
        numbers[j + 1] = curr_num

 

 # Test 1: Normal list
test_list_1 = [4, 2, 6, 5, 1, 3]
expected_result_1 = [1, 2, 3, 4, 5, 6]
insertion_sort(test_list_1)
print("Test 1 passed:", test_list_1 == expected_result_1)

# Test 2: List already sorted
test_list_2 = [1, 2, 3, 4, 5]
expected_result_2 = [1, 2, 3, 4, 5]
insertion_sort(test_list_2)
print("Test 2 passed:", test_list_2 == expected_result_2)

# Test 3: List with negative numbers and zeros
test_list_3 = [-3, -1, -2, 0, 2, 1, 0]
expected_result_3 = [-3, -2, -1, 0, 0, 1, 2]
insertion_sort(test_list_3)
print("Test 3 passed:", test_list_3 == expected_result_3)
