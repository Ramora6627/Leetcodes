class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         if t == "" and s == "":
#             return True
#         if t == "":
#             return False
#         lst = list(t)
#         output = []
#         for i in range(len(s)):
#             if i == 0:
#                 if s[i] in lst:
#                     output.append(lst.index(s[i]))
#                     lst[lst.index(s[i])] ="-"
#             elif s[i] in lst[output[-1]:]:
#                 # print(output[-1:])
#                 output.append(lst[output[-1]:].index(s[i])+output[-1])
#                 lst[lst.index(s[i])] ="-"

#         if len(output) == len(s):
#             return True
#         return False
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
