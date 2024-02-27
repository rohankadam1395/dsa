
def contains_duplicate(nums):
     """
     :type nums: List[int]
     :rtype: bool
     """
     hash = {}
     print(hash)
     for num in nums:
          print(num)
          if hash.get(num) is not None:
               print("woah")
               if hash[num] == 1:
                    return True
          else:
               print("new")
               hash[num] = 1
     return False


contains_duplicate([1,2,3,4])
