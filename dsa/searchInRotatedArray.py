def search(nums, target):
    print(nums,target)

    l=0
    h= len(nums) - 1

    while l<=h:
        mid = l + (h-l)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[h]:
            if target > nums[h]:
                h=mid
            elif target < nums[mid]:
                h = mid
            else:
                l = mid+1
        elif nums[mid] > nums[h]:
                if target > nums[mid]:
                    l = mid +1 
                elif target <= nums[h]:
                    l = mid +1
                else:
                    h=mid
        else:
            return -1


print(search([1],0))
print(search([5,1,3],5))
print(search([4,5,6,7,0,1,2],0))
print(search([4,5,6,7,8,1,2,3],6))
print(search([1,3],3))






