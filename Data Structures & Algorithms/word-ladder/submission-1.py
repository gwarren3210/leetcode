from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def isOneOff(w1, w2):
            oneOff = False
            for i in range(len(beginWord)):
                if w1[i] == w2[i]: continue
                if oneOff: return False
                oneOff = True
            return oneOff
        m = { w: [] for w in wordList }
        m[beginWord] = []
        for i in range(len(wordList)):
            if isOneOff(wordList[i], beginWord):
                m[beginWord].append(wordList[i])
            for j in range(i, len(wordList)):
                if isOneOff(wordList[i], wordList[j]):
                    m[wordList[i]].append(wordList[j])
                    m[wordList[j]].append(wordList[i])
        
        s = set([beginWord])
        q = deque([beginWord])
        out = 0
        while q:
            out += 1
            print(q)
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    print(word)
                    return out
                #print(m)
                for nei in m[word]:
                    if nei in s: continue
                    if nei == endWord: 
                        print(word)
                    s.add(nei)
                    q.append(nei)
        return 0            