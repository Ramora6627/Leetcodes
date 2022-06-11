class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
#         if len(s) != len(t):
#             return False
#         hashtable = {}
        
#         for letter in set(s):
#             hashtable[letter] = s.count(letter)
#         new = ""
#         for st in t:
#             if st not in hashtable:
#                 return False
#             elif st in hashtable and hashtable[st] != 0:
#                 new += st
#                 hashtable[st] -= 1
#         return len(new) == len(s)


#         if len(s) != len(t):
#             return False
        
#         countS, countT = {}, {}
        
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         for c in countS:
#             if countS[c] != countT.get(c, 0):
#                 return False
#         return True

