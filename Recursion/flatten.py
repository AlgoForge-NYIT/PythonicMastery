def flatten(arr):
    result = []
    for element in arr:
        if not isinstance(element, list):
            result.append(element)
        else:
            result.extend(flatten(element))
    return result


input_list = [1, [2], [3, [[4]]]]
expected_result = [1, 2, 3, 4]
actual_result = flatten(input_list)

test_result = "Passed" if expected_result == actual_result else "Failed"
print(f"Test Case {test_result}: Expected {expected_result}, got {actual_result}")
