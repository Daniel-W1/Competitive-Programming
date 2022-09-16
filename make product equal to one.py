n = int(input())
nums = list(map(int, input().split()))

cost, total, zero = 0, 1, 0

for num in nums:
    if num != 0:
        total *= 1 if num > 0 else -1
        cost += (-1 - num) if num < 0 else num-1
    else:
        zero += 1

if total == 1 or zero:
    print(zero + cost)
else:
    print(cost + 2)
