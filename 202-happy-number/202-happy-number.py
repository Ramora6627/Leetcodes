class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}
        total = 0
        while total != 1:
            string = str(n)
            # print(string)
            for num in string:
                
                x = int(num)
                # print (int(num))
                squared = x**2
                # print(squared)
                total += squared
                # print("*",total)
            # print(total)
            if total == 1:
                return True
            elif total in visited:
                break
            else:
                visited[total] = 1 + visited.get(total,0)
                # print(visited)
                n = total
                total = 0
                
                
        return False
    
