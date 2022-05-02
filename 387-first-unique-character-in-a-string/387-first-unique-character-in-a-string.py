class Solution:
    def firstUniqChar(self, s: str) -> int:
#         for char in s:
#             if s.count(char) == 1:
                
#                 return s.index(char)
#                 break
          
#         return -1
        count = collections.Counter(s)
        
        print(count)
        
        for index, char in enumerate(count):
            if(count[char] == 1):
                return s.find(char)
        return -1