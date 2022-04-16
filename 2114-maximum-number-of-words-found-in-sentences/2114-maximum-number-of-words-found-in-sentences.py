class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([sentence.count(" ") for sentence in sentences]) + 1
        # for sentence in sentences: for letter in range(len(sentence)): print(count)
        # # result = list(map(lambda letter: count +=1 for letter in sentences , sentences))
        # print (count)
        # list(map(lambda animal: str.upper(animal), animals))
#     lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>
        # print ([count += 1 for letter in sentence for sentence in sentences if letter == " "])
    
    
         # for i in range(3): for j in range(3): print((i,j))

         # [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]