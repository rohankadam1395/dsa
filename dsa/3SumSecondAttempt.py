def threeSum(nums):
    # print(nums)
    hash_main = {}
    output =[]
    for index,num in enumerate(nums):
        # print(num)
        remainingItems = nums[:index] + nums[index+1:]
        print(remainingItems)
        result = twoSum(remainingItems,0-num,hash_main,num)
        if result is not None:
            print(num,result)
            output.append([num]+result)

    return output





        


def twoSum(nums,target,hash_main,fixedNum):
    l = 0
    r = len(nums) - 1

    keys = hash_main.keys()

    hash = {}

    while l<r:
        hash[nums[l]] = True
        hash[nums[r]] = True   
        if nums[l] in keys and nums[r] in keys and fixedNum in keys:
                return None 
        elif (target - nums[l]) in hash.keys():
            hash_main[fixedNum] = True
            hash_main[nums[l]] = True
            hash_main[target - nums[l]] = True
            return [nums[l],target - nums[l]]
    
        l=l+1
        r=r-1

# print(threeSum([3,0,-2,-1,1,2]))
# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([1,2,-2,-1]))




# print(twoSum([0,1,-1,4],5))


