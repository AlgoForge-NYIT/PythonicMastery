def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers

    mid = len(numbers) // 2
    left_slice = numbers[:mid]
    right_slice = numbers[mid:]

    sorted_left = merge_sort(left_slice)
    sorted_right = merge_sort(right_slice)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    idx_left, idx_right = 0, 0
    result = []
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] < right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1

    result.extend(left[idx_left:])
    result.extend(right[idx_right:])

    return result


# Test 1: Testing with a list of unsorted integers
numbers1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_numbers1 = merge_sort(numbers1)
print(f"Test 1 - Expected: [1, 1, 2, 3, 4, 5, 5, 6, 9], Actual: {sorted_numbers1}, Result: {'Passed' if sorted_numbers1 == [1, 1, 2, 3, 4, 5, 5, 6, 9] else 'Failed'}")

# Test 2: Testing with an empty list
numbers2 = []
sorted_numbers2 = merge_sort(numbers2)
print(f"Test 2 - Expected: [], Actual: {sorted_numbers2}, Result: {'Passed' if sorted_numbers2 == [] else 'Failed'}")

# Test 3: Testing with a list of sorted integers
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_numbers3 = merge_sort(numbers3)
print(f"Test 3 - Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9], Actual: {sorted_numbers3}, Result: {'Passed' if sorted_numbers3 == [1, 2, 3, 4, 5, 6, 7, 8, 9] else 'Failed'}")
