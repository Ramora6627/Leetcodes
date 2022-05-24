class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        x = []
        i = 1
        while i <= k:
            if i in arr:
                k+=1
                i+=1
            else:
                x.append(i)
                i+=1
        return max(x)