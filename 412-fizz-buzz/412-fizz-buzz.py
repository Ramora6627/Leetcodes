class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = "Fizz"
        b = "Buzz"
        c = "FizzBuzz"
        output = []
        for i in range(1,n+1):
            if i%15 == 0:
                output.append(c)
            elif i%3 == 0:
                output.append(a)
            elif i%5 == 0:
                output.append(b)
            else:
                output.append(str(i))
        return output
                
            
            
        