class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        curr = ""
        for i in range(len(s)):
            j = i
            while j<len(s) and s[j] not in res:
                res += s[j]
                j += 1
            # print(i,j,res,curr)
            if len(res)>len(curr):
                curr = res
            res=""
        return len(curr)