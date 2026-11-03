def sequential_search(items, target):
    comparisons = 0

    for i in range(len(items)):
        comparisons += 1

        if items[i] == target:
            return i, comparisons

    return -1, comparisons


tools = [
    "T-101",
    "T-125",
    "T-184",
    "T-210",
    "T-250"
]

targets = ["T-101", "T-184", "T-250", "T-999"]

for target in targets:
    position, comparisons = sequential_search(tools, target)

    if position != -1:
        print(target, "found at position", position + 1)
    else:
        print(target, "not found")

    print("Comparisons:", comparisons)
    print()
