class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # for num in  arr:
#             if not num in target or arr.count(num) > target.count(num):
#                 return False
#                 break
                
#         return True

        target.sort()
        arr.sort()
        return target == arr 