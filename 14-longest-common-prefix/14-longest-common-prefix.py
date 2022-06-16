class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 1 or not all((strs)):
            return res
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res