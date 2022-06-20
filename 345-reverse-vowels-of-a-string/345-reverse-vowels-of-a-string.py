class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        reverse_list = []
        for char in s:
            if char.lower() in vowels:
                reverse_list.append(char)
        print(reverse_list)
        index = 0
        reverse_list[::] = reverse_list[::-1]
        print(reverse_list)
        new = ""
        for char in s:
            if char.lower() in vowels:  
                # print(index)
                new += reverse_list[index]
                index += 1
            else:
                new += char
        
        
        return new
            