import sys
input = sys.stdin.readline

def solve():
    n, W = map(int, input().split())
    dp = [0] * (W + 1)

    for _ in range(n):
        value, weight = map(int, input().split())
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    print(dp[W])

if __name__ == "__main__":
    solve()
