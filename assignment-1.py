import sys

def fractional_knapsack(items, capacity):
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for value, weight in items:
        if remaining_capacity == 0:
            break
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0

    return total_value


def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1

    results = []
    for _ in range(t):
        n = int(data[idx])
        w = int(data[idx + 1])
        idx += 2

        items = []
        for _ in range(n):
            v = int(data[idx])
            wt = int(data[idx + 1])
            idx += 2
            items.append((v, wt))

        max_value = fractional_knapsack(items, w)
        results.append(f"{max_value:.6f}")

    print("\n".join(results))


if __name__ == "__main__":
    main()
