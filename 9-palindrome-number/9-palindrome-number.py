class Solution:
    def isPalindrome(self, x: int) -> bool:
        m = str(x)
        if len(m) == 1:
            return True
        for i in range((len(m)//2)):
            if m[i] != m[-i-1]:
                # print (m[i],m[-i-1])
                return False
        #         print(list(x[-i-1]))
        #             # return True
        return True    
        