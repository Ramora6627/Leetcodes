class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
# test 1
#         total = 1
#         for i in range(0,len(digits)): 
#             total += digits[i]*(10**(len(digits)-i-1))


        

#         return [str(num) for num in str(total)]
#  test 2       
      
        digits = [str(d) for d in digits]
        dig = int(''.join(digits)) + 1
        return [i for i in str(dig)]