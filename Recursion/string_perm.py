


def permutations(s):
    results = set()  # Use a set to avoid duplicate entries

    def recurse(word, remainder):
        if len(remainder) == 0:
            results.add(word)
        for i in range(len(remainder)):
            recurse(word + remainder[i], remainder[:i] + remainder[i+1:])

    recurse('', s)
    return list(results)  # Convert the set to a list before returning



input_str = "abc"
expected_permutations = sorted(["abc", "acb", "bac", "bca", "cab", "cba"])
actual_permutations = sorted(permutations(input_str))

test_result = "Passed" if expected_permutations == actual_permutations else "Failed"
print(f"Test Case {'Passed' if expected_permutations == actual_permutations else 'Failed'}: Expected {expected_permutations}, got {actual_permutations}")
