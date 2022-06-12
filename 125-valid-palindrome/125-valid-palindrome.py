class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l =''.join( c for c in s if  c not in '?:!/;' )
        s = s.lower()
        for char in s:
            if not char.isalnum(): 
                s = s.replace(char,'') 
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
        
        