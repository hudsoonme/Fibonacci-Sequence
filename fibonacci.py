def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

# Example usage:
fib_nums = fibonacci(10)
print(fib_nums)