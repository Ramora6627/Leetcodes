class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = ""
        if not needle:
            return 0
        if needle in haystack:
            for j in range(len(haystack)):
                if haystack[j] == needle[0]:
                    i = 1
                    index = j
                    res += needle[0]
                    while i < len(needle) and haystack[j+i]==needle[i]:
                        
                        res += haystack[j+i]
                        # print(i)
                        i += 1
                    # print(res)
                    if res != needle:
                        res = ""
                    else:
                        return index

                    

        return -1
                
        