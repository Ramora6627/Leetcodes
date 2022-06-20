class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        reverse_list = []
        for char in s:
            if char.lower() in vowels:
                reverse_list.append(char)
        index = 0
        new = ""
        for char in s:
            if char.lower() in vowels:  
                new += reverse_list[::-1][index]
                index += 1
            else:
                new += char
        
        
        return new
            