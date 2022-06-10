class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num//2
        if num == 1:
            return True
        while low<= high:
            mid = (low+high)//2
            # mid = mid-1
            # print(mid)
            # print(lst[mid]**2)
            if ( mid**2 == num):
                return True
            elif (mid**2 < num):
                low = mid + 1
                # print(mid,low,high)
            elif (mid**2 > num):
                # print(mid)
                high = mid - 1 
                # print(mid,low,high)
        
        return False