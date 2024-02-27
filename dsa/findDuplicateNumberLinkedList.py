def findDuplicate(nums):
    print(nums)

    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break


    print("check")

    




print(findDuplicate([1,3,4,2,2]))