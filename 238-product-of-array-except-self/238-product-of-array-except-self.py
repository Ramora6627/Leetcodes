class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hashtable = {}
        answer = []
        for num in nums:
            hashtable[num] = 1 + hashtable.get(num, 0)
        # print(hashtable)           
        for num in nums:
            p = 1
            hashtable[num] -= 1
            for key,val in hashtable.items():
                if val != 0:
                    p = p*(key**val); 
                    # print(p)
            answer.append(p)
            hashtable[num]+= 1
        return answer
            
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j != i:
#                     p = p*nums[j]
#             answer.append(p)
#             p = 1
#         return answer
                