class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                return [hashtable[nums[i]],i]
            hashtable[target-nums[i]] = i
            # print(hashtable)
        # return output
        
        
        
                
        