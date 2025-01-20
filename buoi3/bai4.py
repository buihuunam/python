def decimal_to_binary(n):
    stack = []
    print(f"convert {n} to binary")
    
    if n == 0:
        stack.append(0)
        print(f"pushed 0 to stack")
    else:
        while n > 0:
            remainder = n % 2
            stack.append(remainder)
            print(f"pushed {remainder} to stack")
            n = n // 2
            print(f"n = {n}")

    binary = ""
    print("pop all elements from stack")
    while stack:
        binary += str(stack.pop())
        print(f"popped {binary[-1]} from stack")
    return binary

# simulate
number = 10
binary = decimal_to_binary(number)
print(f"Binary representation of {number} is: {binary}")