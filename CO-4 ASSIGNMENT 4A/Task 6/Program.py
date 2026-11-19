Task 6: Energy-Aware Weighted Interval Scheduling
def energy_schedule(jobs):
    # Each job: (ID, start, finish, energy_saving)
    jobs = sorted(jobs, key=lambda job: job[2])
    n = len(jobs)
    p = [0] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if jobs[j][2] <= jobs[i][1]:
                p[i] = j + 1  # number of compatible jobs before i
                break

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        value = jobs[i - 1][3]
        include = value + dp[p[i - 1]]
        exclude = dp[i - 1]
        dp[i] = max(include, exclude)

    selected = []
    i = n
    while i > 0:
        value = jobs[i - 1][3]
        if value + dp[p[i - 1]] > dp[i - 1]:
            selected.append(jobs[i - 1][0])
            i = p[i - 1]
        else:
            i -= 1
    selected.reverse()
    return selected, dp[n], dp

if __name__ == "__main__":
    jobs = [
        ("J1", 1, 3, 20), ("J2", 2, 5, 50),
        ("J3", 4, 6, 30), ("J4", 6, 8, 40),
        ("J5", 5, 9, 60), ("J6", 8, 10, 30),
        ("J7", 9, 11, 50), ("J8", 11, 13, 40)
    ]
    chosen, total, dp = energy_schedule(jobs)
    print("Selected jobs:", chosen)
    print("Maximum energy saving:", total)
    print("DP values:", dp)

    challenge = [
        ("A", 1, 10, 100), ("B", 1, 3, 40),
        ("C", 3, 5, 40), ("D", 5, 7, 40), ("E", 7, 10, 40)
    ]
    chosen2, total2, _ = energy_schedule(challenge)
    print("Challenge selected jobs:", chosen2)
    print("Challenge maximum value:", total2)
