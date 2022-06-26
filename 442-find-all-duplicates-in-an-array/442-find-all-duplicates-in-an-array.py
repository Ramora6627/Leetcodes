class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        hashtable = {}
        for num in nums:
            hashtable[num] = 1 + hashtable.get(num,0)
            
        return [key for key,value in hashtable.items() if value>1]
        