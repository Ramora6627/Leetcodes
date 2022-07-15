class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        curr = 0
        l = 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l]) 
                l += 1
            res.add(s[r])
            # print(i,j,res,curr)
            curr = max(curr,r-l+1)
            
        return curr