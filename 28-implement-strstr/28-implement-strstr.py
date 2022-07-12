class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
        
        if needle in haystack:
            
            for i in range(len(haystack)):
                res = ""
                if haystack[i] == needle[0]:
                    ind = i
                    # print(ind)
                    j = 0
                    k = i 
                    while j<len(needle) and haystack[k] == needle[j]:
                        res += haystack[k]
                        k += 1
                        j += 1
                    # print(res)
                    if len(res) == len(needle):
                        return ind
        return -1
                    
        