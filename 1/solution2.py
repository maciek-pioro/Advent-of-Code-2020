f = open('input.txt', 'r')

nums = [int(l) for l in f]
n = len(nums)
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(nums[i] * nums[j] * nums[k])