def two_sum(nums, target):
    for i in nums:
        if target - i in nums:
            return print(nums.index(i), nums.index(target - i))


two_sum([2, 5, 3, 7, 3, 8], 10)
