
'''

[1,2,3,6,8]
[1,3,6,12,20]

'''
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    lsum , rsum = nums[0]+nums[1], nums[-1]
    left, right = 1, len(nums)-1

    while left < right:
        if lsum < rsum:
            print("YES")
            break
        left += 1
        right -= 1
        lsum += nums[left]
        rsum += nums[right]
    # print(left, right)
    if left >= right:
        print("NO")

