def lengthOfLongestSubstring(s):
    print(s)
    l = 0
    r = 1

    prevElements = {}
    lengthMax= 0

    if len(s) == 1:
        return 1

    while r<len(s):
        print(l,r)
        prevElements[s[l]] = l

        if s[r] in prevElements:
            # duplicate found end the sub string  here:
            if r == prevElements[s[r]] + 1:
                l = r 
            else:
                l = prevElements[s[r]] + 1
                r = l + 1
            prevElements = {}

         

        prevElements[s[r]] = r

        r = r + 1
        if (r-l) > lengthMax:
            lengthMax = r-l


    return lengthMax



print(lengthOfLongestSubstring("abba"))

print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("dvdf"))