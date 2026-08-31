from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        d = { c:[] for w in words for c in w }
        d2 = defaultdict(list)
        for i in range(1, len(words)):
            w1 = words[i-1]
            w2 = words[i]
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                    return ""
                if w1[j] != w2[j]:
                    d[w1[j]].append(w2[j])
                    d2[w2[j]].append(w1[j])
                    break
        out = ''
        q = []
        for k, v in d.items():
            if len(d[k]) == 0:
                q.append(k)
        print(q)
        while q:
            l = q.pop(0)
            out += l
            for char in d2[l]:
                d[char].remove(l)
                if len(d[char]) == 0:
                    q.append(char)
        if len(out) != len(d): return ""
        return out[::-1]