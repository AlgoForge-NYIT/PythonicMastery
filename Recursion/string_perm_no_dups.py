
### input string unique ###
def string_permute(s, current_permutation='', remaining_chars=None):
    if remaining_chars is None:
        remaining_chars = s
    
    all_permutations = []

    if not remaining_chars:
        all_permutations.append(current_permutation)
    else:
        for i in range(len(remaining_chars)):
            curr_char = remaining_chars[i]
            # Make a copy of remaining_chars for recursive call # new var name
            new_remaining_chars = remaining_chars[:i] + remaining_chars[i+1:]
            all_permutations += string_permute(s, current_permutation + curr_char, new_remaining_chars)
    return all_permutations


input_str1 = "abc"
expected_output1 = sorted(["abc", "acb", "bac", "bca", "cab", "cba"])
actual_output1 = sorted(string_permute(input_str1))
print(f"Test Case 1 {'Passed' if actual_output1 == expected_output1 else 'Failed'}: Expected {expected_output1}, got {actual_output1}")