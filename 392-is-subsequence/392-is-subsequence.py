class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for i in range(len(s)):
            # print(i)
            if s[i] in t[k:]:
                k = t[k:].index(s[i])+1+len(t[:k])
                # print(k)
            else:
                return False
        return True
        