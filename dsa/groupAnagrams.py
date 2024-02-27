
def groupAnagrams(strs):
    """:type strs: List[str]
    :rtype: List[List[str]]
    """
    hashedAnagrams = {}
    for i in range(len(strs)):
        sortedStr = "".join(sorted(strs[i]))
        if hashedAnagrams.get(sortedStr):
            hashedAnagrams[sortedStr].append(strs[i])
        else:
            hashedAnagrams[sortedStr] = [strs[i]]
    return hashedAnagrams.values()

def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        return sorted(str1) == sorted(str2)



groupAnagrams(["eat","tea","tan","ate","nat","bat"])