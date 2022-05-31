class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        for num in  arr:
            if not num in target:
                return False
                break
            elif arr.count(num) > target.count(num):
                return False
        return True