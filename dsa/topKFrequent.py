
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    frequency = {}
    def func(x):
        return x[1]

    for num in nums:
        frequency[num] = frequency.get(num,0)+1
    return [*dict(sorted(frequency.items(),key=func,reverse=True)[:k]).keys()]



print(topKFrequent([2,2,3,1,1,1,4,4,4,4,4],2))