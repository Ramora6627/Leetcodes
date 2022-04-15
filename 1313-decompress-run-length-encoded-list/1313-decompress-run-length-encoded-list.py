import itertools   

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # lst = []
        # for i in range(0, len(nums) - 1, 2): lst.extend([nums[i+1]]*nums[i])
        # return lst

        lst = []
        for i in range(0, len(nums) - 1, 2):
            lst.extend(list(itertools.repeat(nums[i+1],nums[i])))
        return lst
       
            
        