def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]
    
    left, right = [], []
    
    for i in range(len(numbers)-1):
        if numbers[i] < pivot:
            left.append(numbers[i])
        else:
            right.append(numbers[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)



# Test cases
test_case_1 = [3, 1, 4, 1, 5, 9, 2, 6]
expected_1 = [1, 1, 2, 3, 4, 5, 6, 9]
actual_1 = quick_sort(test_case_1)
print(f"Test 1 - Expected: {expected_1}, Actual: {actual_1}")

test_case_2 = [10, 7, 8, 9, 1, 5]
expected_2 = [1, 5, 7, 8, 9, 10]
actual_2 = quick_sort(test_case_2)
print(f"Test 2 - Expected: {expected_2}, Actual: {actual_2}")

test_case_3 = [99]
expected_3 = [99]
actual_3 = quick_sort(test_case_3)
print(f"Test 3 - Expected: {expected_3}, Actual: {actual_3}")

