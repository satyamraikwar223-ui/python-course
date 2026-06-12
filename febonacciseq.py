def febonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = [0, 1]
    for i in range(2, n):
        next_value = seq[i - 1] + seq[i - 2]
        seq.append(next_value)

    return seq
n = 100
print(f"Fibonacci sequence up to {n} terms: {febonacci(n)}")
