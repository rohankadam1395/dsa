def findMin(nums):
    # print(nums)
    print("--------------")
    l = 0
    h = len(nums) - 1

    while l<=h:
        print(l,h)
        mid = l + (h-l)//2
        print(nums[l],nums[mid],nums[h])
        if nums[mid] < nums[h]:
            h=mid
        elif nums[mid] > nums[h]:
            l = mid + 1
        else:
            return nums[l]

            
           


        
    return nums[l]


# print(findMin([3,4,5,1,2]))
# print(findMin([4,5,6,7,0,1,2]))
# print(findMin([2,1]))
# print(findMin([3,1,2]))
# print(findMin([3,2,1]))
# print(findMin([1,2,3,4,5]))

# print(findMin([4,5,1,2,3]))
# print(findMin([4,5,1,2,3]))
# print(findMin([2,3,4,5,1]))

# 1,2,3

# 3,2,1










