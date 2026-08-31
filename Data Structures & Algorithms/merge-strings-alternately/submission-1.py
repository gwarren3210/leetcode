class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        i = 0
        while i < len(word1) and i<len(word2):
            out += word1[i] + word2[i]
            i += 1
            print(i, out)
        if len(word1) == len(word2):
            return out
        if len(word1) > len(word2):
            return out + word1[i:]
        return out + word2[i:]