def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacciDP(n):
    memo = {0: 0, 1: 1}
    
    def recurse(m):
        if m not in memo:
            memo[m] = recurse(m-1) + recurse(m-2)
        return memo[m]
    
    return recurse(n)


n = 10
expected_result = 55
actual_result = fibonacciDP(n)

test_result = "Passed" if expected_result == actual_result else "Failed"
print(f"Test Case {test_result}: Expected {expected_result}, got {actual_result}")
