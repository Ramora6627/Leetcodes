class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        output = 0
        for i in range(len(s)):
            while j<len(s) and s[j] not in s[i:j]:
                j += 1
            if len(s[i:j])> output:
                output = len(s[i:j])
             
            i += 1
            j = i +1
        return output