class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        s = sentence.split(" ")
        for i in range(len(s)):
            if s[i][0]== "$":
                
                if s[i][1:].isnumeric():
                    price = int(s[i][1:])
                # price = int(price)
                    print(price)

                    updated_price = ((100-discount)*int(price))/100
                    print(updated_price)

                # print(updated_price)
                    u = str(updated_price)
                    s[i] = "$"+ '%.2f'%updated_price
                # print(s[i],s)
        return " ".join(s)