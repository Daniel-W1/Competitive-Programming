t = int(input())
 
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
 
    dp = [0]*n
    for idx in range(n):
        num = nums[idx]
        dp[idx] += num
        if idx + num < n:
            dp[idx+num] = max(dp[idx+num], dp[idx])
 
    print(max(dp))
