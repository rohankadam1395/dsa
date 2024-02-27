
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    prefixProducts = [1 for i in range(len(nums))]
    suffixProducts = [1 for i in range(len(nums))]
    answer = [0 for i in range(len(nums))]

    prefixProducts[0] = nums[0]
    suffixProducts[len(nums)-1] = nums[len(nums)-1]

# in the belwo two for loops nums[i] is once forwards and backwards
# lets combine it into one loops
    for i in range(1,len(nums)):
        print(i, "pre")
        prefixProducts[i] = prefixProducts[i-1] * nums[i]

    for i in range(len(nums)-2,-1,-1):
        print(i,"suff",suffixProducts)
        suffixProducts[i] = suffixProducts[i+1] * nums[i]
        print("test",suffixProducts)


    newAnswer =[]
    for i in range(1,len(nums)-1):
        j =len(nums)-1-i
        print(i,j)










    # print(prefixProducts)
    # print(suffixProducts)

    answer[0] = suffixProducts[1]
    answer[len(nums)-1] = prefixProducts[len(nums)-2]

    for i in range(1,len(nums)-1):
        answer[i] = suffixProducts[i+1] * prefixProducts[i-1]
    # print(answer)
    return answer





# print(productExceptSelf([1,2,3,4]))

def productExceptSelf2(nums):
    result = [1] * len(nums)

    prefix = 1
    suffix = 1

    for i in range(len(nums)):
        print(i)

        result[i] = result[i] * prefix
        prefix = prefix * nums[i]

    for i in range(len(nums)-1,-1,-1):
        result[i]= result[i] * suffix
        suffix = suffix * nums[i]


    return result



print(productExceptSelf2([1,2,3,4]))

# 1 2 3 4

# for 1st item get the 2nd from suffix
# for last item get the 2nd last from prefix

# for any other element have to multiply index-1 form suffix to index+1 in prefix


# prefix
# 1 2 6 24

# suffix
# 24 24 12 4


# 24 12 8 6


