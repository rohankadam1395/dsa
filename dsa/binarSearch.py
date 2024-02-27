
def search(nums,target):
    # print(nums,target)
    
    l = 0
    h = len(nums) - 1

    while l <= h :
        print(l,h)
        mid = l + (h-l)//2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid + 1 
        else:
            h = mid - 1
    return -1







# print(search([-1,0,3,5,9,12],9))


print(search([-1,0,3,5,9,12],2))
print(search([5],5))


# 0,5
# 2
# 0,2
# 1,2
# 1
# 1,2
# 1,2


# 0 0

