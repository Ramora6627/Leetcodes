class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        w = sum(mat, [])
        if len(w)%(r*c) != 0 or r*c==1:
            return mat
        return [w[(i-1)*c:i*c] for i in range(1,r+1)]