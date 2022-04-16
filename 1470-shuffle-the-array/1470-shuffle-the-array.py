class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]: 
        # return [el for zipped in zip(nums[:n], nums[n:]) for el in zipped] 
        new_list = []
        for i in range(0,len(nums)//2):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list
        
        
