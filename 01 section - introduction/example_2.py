# The Fibonacci Number Algorithm - recursion

print(0)
print(1)
# module level
count = 2

def fibonacci(prev1, prev2):
    global count # global count tells Python that the function should use and update the module-level count instead.
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1, 0)