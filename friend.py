n, k = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cost = 0

while right < n:
    if nums[left] + nums[right] < k:
        cur = nums[left] + nums[right]
        cost += (k - cur)
        nums[right] += k - cur
    left += 1
    right += 1

print(cost)
print(*nums)
