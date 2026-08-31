class Solution:
    def validPalindrome(self, s: str) -> bool:
        #rev = s[::-1]
        l,r = 0, len(s)-1

        while l < r:
#            print(l,r,s[l], s[r])
            if s[l] != s[r]:
#                print(s[l:r+1])
#                print(rev[l:r+1])
#                print(s[l+1:r+1], rev[l:r])
                skipL = s[l+1:r+1] == s[l+1:r+1][::-1] #rev[l:r]
#                print(s[l:r], rev[l+1:r+1])
                skipR = s[l:r] == s[l:r][::-1]
                #rev[l+1:r+1]
                return skipL or skipR
            l += 1
            r -= 1
        return True