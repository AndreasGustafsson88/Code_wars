def queue_time(customers, n):
    tills = [[0] for _ in range(n)]
    for time in customers:
        min(tills)[0] += time

    return max(tills)[0]



print(queue_time([5], 1))
