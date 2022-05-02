class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # for count, ele in enumerate(nums,0):
        count = 0
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                count += nums[i+1:].count(nums[i])
        # print (count)
        return count
                
#         pairs = {}
#         for i in nums:
#             if i in pairs:
#                 pairs[i]+=1
#             else:
#                 pairs[i]=1
#         count=0
#         for i in pairs:
            
#             count+= (pairs[i]*(pairs[i]-1)//2)
#         return count