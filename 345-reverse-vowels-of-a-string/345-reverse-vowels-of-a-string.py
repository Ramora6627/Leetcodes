class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','O','U','E','I']
#         reverse_list = []
#         for char in s:
#             if char.lower() in vowels:
#                 reverse_list.append(char)
#         index = 0
#         reverse_list[::] = reverse_list[::-1]
#         new = ""
#         for char in s:
#             if char.lower() in vowels:  
#                 new += reverse_list[index]
#                 index += 1
#             else:
#                 new += char
        
        
#         return new
        s = list(s)
        i = 0
        j = len(s) - 1
        while (i < j):
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue

            # swapping
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        s = "".join(s)
        return s
            