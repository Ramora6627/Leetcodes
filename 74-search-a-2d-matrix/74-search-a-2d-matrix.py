class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])
        
        first, last = 0, rows-1
        
        while first<=last:
            target_row = (first+last)//2
            if target>matrix[target_row][-1]:
                first = target_row + 1
            elif target < matrix[target_row][0]:
                last = target_row -1
            else:
                break
        if not(first<=last):
            return False
        target_row = (first +last)//2
        l,r = 0, cols-1
        while l<=r:
            mid = (l+r)//2
            if target > matrix[target_row][mid]:
                l = mid +1
            elif target <matrix[target_row][mid]:
                r = mid -1
            else:
                return True
        return False