class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        p = []
        for d in range(1,n+1):
            for x in range(1,d):
                if gcd(x,d) == 1:
                    p.append(f"{x}/{d}")
        return p

