class Solution:
    def sortSentence(self, s: str) -> str:
        
        """
        split by space and turn it to a list
        substract one from num[-1] == index
        rearrange the word list
        join
        """
        
        word_list = s.split()
        new_arrange = [""]*len(word_list)
        for word in word_list:
            # print (word, word[-1])
            
            new_arrange[int(word[-1])-1] = word[:-1]
            # print(new_arrange)
        # print(new_arrange)
        # ('').join(new_arrange)
        
        return (' ').join(new_arrange)
            
        