def searchMatrix(matrix, target):
    print(matrix,target)
    l = 0
    h = len(matrix) - 1

    while l<=h:
        mid = l + (h-l)//2
        # print("mid",mid)
        lastElementOfMidMatrix = len(matrix[mid]) - 1
        if target < matrix[mid][0]:
            # go to the left side matrixes
            h = mid -1
        elif target > matrix[mid][lastElementOfMidMatrix]:
            # go to the right side matrixes
            l = mid + 1
        else:
            # either target lies in mid matrix or is not present at all
            return searchArray(matrix[mid],target)
    return False

def searchArray(nums, target):

    l=0
    h=len(nums) - 1

    while l<=h:
        mid = l + (h-l)//2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid +1
        else:
            h = mid -1
    return False




print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],12))