class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        res = [0]*len(temp)
        stack =  [] #(temp, index)
        for i in range(len(res)):
            while stack and stack[-1][0] < temp[i]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp[i], i))
        return res