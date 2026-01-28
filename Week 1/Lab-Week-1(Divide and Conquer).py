#tuesday
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i = j = 0
    merged = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def solve():
    T = int(input())
    res = []
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = merge_sort(arr)
        res.append(" ".join(map(str, sorted_arr)))
    print("\n".join(res))

if __name__ == "__main__":
    solve()


#wednesday
import sys
input = sys.stdin.readline

def max_crossing_sum(arr, l, m, r):
    left_sum = -10**18
    s = 0
    for i in range(m, l - 1, -1):
        s += arr[i]
        if s > left_sum:
            left_sum = s

    right_sum = -10**18
    s = 0
    for i in range(m + 1, r + 1):
        s += arr[i]
        if s > right_sum:
            right_sum = s

    return left_sum + right_sum

def max_subarray(arr, l, r):
    if l == r:
        return arr[l]

    m = (l + r) // 2
    return max(
        max_subarray(arr, l, m),
        max_subarray(arr, m + 1, r),
        max_crossing_sum(arr, l, m, r)
    )

def solve():
    T = int(input())
    out = []
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        out.append(str(max_subarray(arr, 0, N - 1)))
    print("\n".join(out))

if __name__ == "__main__":
    solve()
