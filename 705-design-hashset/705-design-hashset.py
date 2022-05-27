class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size
        
    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] != None:
            while key in self.table[hv]: 
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hv = self.calculate_hash_value(key)
        
        if self.table[hv] != None:
            return key in self.table[hv]
        return False
                

#         self.size = 1000000
#         self.hashset = [None]*self.size
        
#     def find_index(self,key):
#         return key%self.size
        

#     def add(self, key: int) -> None:
#         index = self.find_index(key)
#         print(index)
#         if self.hashset[index] == None:
#             self.hashset[index] = key
#         else:
#             self.hashset[index].append(key)
#         return self.hashset

#     def remove(self, key: int) -> None:
#         index = self.find_index(key)
#         if key in self.hashset[index]:
#             self.hashset[index].remove(key)
#         return self.hashset

#     def contains(self, key: int) -> bool:
#         index = self.find_index(key)
#         if self.hashset[index] != None:
#             print(self.hashset[index])
#                 # return True
#         else:
#             return False
        # return self.hashset


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)