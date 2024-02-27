def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash = {}
    for i in range(len(nums)):
        print(i)
        temp = target - nums[i]
        if nums[i] in hash:
            return [i,hash[nums[i]]]
        hash[temp] = i






print(twoSum([-1,-2,-3,-4,-5], -8))

