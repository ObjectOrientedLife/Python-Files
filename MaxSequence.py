def maximumSequence(sequence):
    maxSum = max(sequence)
    for i in range(0, len(sequence)):
        sum = 0
        for j in range(i, len(sequence)):
            sum += sequence[j]
            if sum > maxSum:
                maxSum = sum
    return maxSum
