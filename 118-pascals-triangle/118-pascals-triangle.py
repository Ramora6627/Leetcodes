class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # only up to n = 5: return [list(str(11**(i-1))) for i in range (1, numRows+1)]
        res = [[1]]
        
        for i in range (numRows-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range (len(res[-1]) + 1):
                row.append(temp[j]+ temp[j+1])
            res.append(row)    
        return res