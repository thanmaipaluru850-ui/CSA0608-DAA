Task 3: 0/1 Knapsack using Dynamic Programming
def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weight <= w:
                dp[i][w] = max(dp[i][w],
                               value + dp[i - 1][w - weight])

    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, weight, value = items[i - 1]
            selected.append(name)
            w -= weight
    selected.reverse()
    return dp[n][capacity], selected, dp

if __name__ == "__main__":
    items = [("P", 2, 12), ("Q", 3, 20), ("R", 4, 25), ("S", 5, 30)]
    best, chosen, table = knapsack(items, 7)
    print("Maximum value:", best)
    print("Selected items:", chosen)
    print("Final DP row:", table[-1])
