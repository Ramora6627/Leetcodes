class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1] 

        
#         i = 0
#         while numbers[i] <= target: 
            
#             res = target-numbers[i]
#             # print(res)
#             if res >= numbers[i]:
#                 if res in numbers[i+1:]:
#                     return (i+1, (numbers[i+1:].index(res))+i+2)
#                     break
            
#             i += 1
                
                