#week 2.3
"""
Sample Input:
5
3 34 4 12 5
9

Sample Output:
True
"""

def subset_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0 or target < 0:
        return False
    return (subset_sum(arr, n - 1, target) or
            subset_sum(arr, n - 1, target - arr[n - 1]))

def solve():
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())
        print(subset_sum(arr, n, target))
    except EOFError:
        pass

if __name__ == "__main__":
    solve()

#week 2.4
"""
Sample Input:
AGGTAB
GXTXAYB

Sample Output:
4
"""

def solve():
    try:
        s1 = input().strip()
        s2 = input().strip()

        n = len(s1)
        m = len(s2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        print(dp[n][m])

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
