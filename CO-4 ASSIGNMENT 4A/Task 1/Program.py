# Task 1: Fractional Knapsack
def fractional_knapsack(capacity, packages):
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")
    for name, weight, value in packages:
        if weight <= 0 or value < 0:
            raise ValueError("Weight must be positive and value non-negative")

    ordered = sorted(packages, key=lambda p: p[2] / p[1], reverse=True)
    remaining = capacity
    total_value = 0.0
    selected = []

    for name, weight, value in ordered:
        if remaining == 0:
            break
        fraction = min(1.0, remaining / weight)
        selected.append((name, fraction))
        total_value += fraction * value
        remaining -= fraction * weight

    return selected, total_value

if __name__ == "__main__":
    packages = [("A", 10, 60), ("B", 20, 100), ("C", 30, 120)]
    chosen, maximum = fractional_knapsack(50, packages)
    print("Selected fractions:", chosen)
    print("Maximum value:", round(maximum, 2))
