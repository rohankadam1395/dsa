def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hash_s = {}
    hash_t = {}
    if len(s) != len(t):
        return False
    else:
        for i in range(len(s)):
            if hash_s.get(s[i]) is None:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] = hash_s[s[i]] + 1
            if hash_t.get(t[i]) is None:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] = hash_t[t[i]] + 1
        for key in hash_t:
            if hash_t.get(key) != hash_s.get(key):
                return False
        return True

    print(hash_s)
    print(hash_t)




print(isAnagram("anagram","nagaram"))