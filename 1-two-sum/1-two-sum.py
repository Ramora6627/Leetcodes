class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = list(set(nums))
        output = []

        hashtable = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in hashtable:
                output.append(hashtable[res])
                output.append(nums[i:].index(nums[i])+i)
            else:
                hashtable[nums[i]] = i
        
        
        return output
        
        
        
                
        