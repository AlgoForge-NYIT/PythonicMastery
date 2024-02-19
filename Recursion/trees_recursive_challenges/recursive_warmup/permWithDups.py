
### Input string with duplicates ###
def string_permute_no_dups(s, current_permutation='', remaining_chars=None):
    if remaining_chars is None:
        remaining_chars = s
    
    all_permutations = []

    if not remaining_chars:
        all_permutations.append(current_permutation)
    else:
        local_used_chars = set()

        for i in range(len(remaining_chars)):

            curr_char = remaining_chars[i]
            # Make a copy of remaining_chars for recursive call
            if curr_char not in local_used_chars:
                local_used_chars.add(curr_char)

                new_remaining_chars = remaining_chars[:i] + remaining_chars[i+1:]
                # set s to new remaining chars to update set based on new string instead of original
                all_permutations += string_permute_no_dups(new_remaining_chars, current_permutation + curr_char)
    return all_permutations



input_str2 = "aabb"
expected_output2 = ["aabb", "abab", "abba", "baab", "baba", "bbaa"]
actual_output2 = string_permute_no_dups(input_str2)
assert sorted(actual_output2) == sorted(expected_output2), f"Test Case 2 Failed: Expected {expected_output2}, got {actual_output2}"
print(f"Test Case 2 Passed: {actual_output2}")
