def isPalindrome(s):
    # print(s)

    l = 0
    r = len(s) -1
    while l<r:
        # print(s[l],s[r])
        while l < len(s) and not s[l].isalnum():
            l=l+1
        while r >0 and not s[r].isalnum():
            r=r-1


        if l<len(s) and r>0 and s[l].lower() != s[r].lower():
            # print("issue")
            return False
        


        l=l+1
        r=r-1
    return True

print(isPalindrome(".,"))
