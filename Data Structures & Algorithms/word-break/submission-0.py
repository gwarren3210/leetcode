class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)+1, -1, -1):
            for word in wordDict:
                #print('_'*4)
                #print(i, len(word)+i, len(s))
                #print(word, s[i:i+len(word)])
                if len(word)+i > len(s) or \
                    not dp[i+len(word)] or \
                    s[i:i+len(word)] != word:
                    continue
                dp[i] = True
            #print(dp)
        #print(dp)
        return dp[0]