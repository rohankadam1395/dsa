def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # print(nums)
    # numSet = set()
    # consecutiveNums = set()
    # # print(consecutiveNums)
    # for num in range(len(nums)):
    #     # print(nums[num])
    #     if nums[num]+1 in numSet:
    #         consecutiveNums.add(nums[num])
    #         consecutiveNums.add(nums[num]+1)
    #     if nums[num]-1 in numSet:
    #         consecutiveNums.add(nums[num])
    #         consecutiveNums.add(nums[num]-1)
    #     # print("consecutiveNums",consecutiveNums)
    #     numSet.add(nums[num])
    # return len(consecutiveNums)

    numSet = set(nums)
    max = 0
    for num in range(len(nums)):
        count =1 
        startNum = nums[num]
        while startNum-1 in numSet:
            count = count + 1
            startNum = startNum -1
            numSet.discard(startNum)

        startNum = nums[num]
        while startNum + 1 in numSet:
            count = count + 1
            startNum = startNum + 1
            numSet.discard(startNum)
        numSet.discard(nums[num])
        if count > max:
            max =count

    return max


        






        
print(longestConsecutive([101,0,2,7,3,100,5,8,4,6,0,1,0]))