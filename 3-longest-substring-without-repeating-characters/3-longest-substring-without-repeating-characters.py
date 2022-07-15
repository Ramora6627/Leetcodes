class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        curr = 0
        for i in range(len(s)):
            j = i
            while j<len(s) and s[j] not in res:
                res.add(s[j]) 
                j += 1
            # print(i,j,res,curr)
            if len(res)>curr:
                curr = len(res)
            res.clear()
        return curr