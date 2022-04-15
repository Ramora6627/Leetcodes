class Solution:
    def romanToInt(self, s: str) -> int:
#         roman_dict = {"I":1, "V":5, "X": 10, "L":50, "C": 100, "D":500, "M": 1000 }
#         exceptions = {"IV" : 4, "IX" : 9, "XL": 40, "XC": 90, "CD":400 , "CM":900}
#         total = 0
#         i = 0
#         while i < len(s) : 
#             if i != s[-1]:
#                 combined = s[i:i+2:1]
#                 if combined in exceptions.keys():
#                     total += exceptions[combined]
#                     i += 2
#                 else:
#                     total += roman_dict[s[i]]
#                     i += 1
#             else:
#                 total += roman_dict[s[i]]
#         return total
    
#         Solution 2:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        nums = list(map(lambda x:d[x],s))

        ans, carry = 0, 0

        for num in nums:
            if num <= carry:
                ans += carry
                carry = num
            else:
                ans -= carry
                carry = num
        
        return ans+carry