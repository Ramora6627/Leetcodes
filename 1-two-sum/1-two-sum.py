class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         res = []
#         for num in nums:
#             residual = target - num
#             if residual in res and num != residual:
#                 return ([nums.index(residual), nums.index(num)])
#             elif residual in res and num == residual:
#                 a = nums.index(residual)
#                 b = nums[a+1:]
#                 print (a)
#                 return [a,b.index(num)+len(nums[:a+1])]

#             res.append(num)
            
            
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i