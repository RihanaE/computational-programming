class DataStream:

    def __init__(self, value: int, k: int):
        self.count=0
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count +=1
            
        else:
            self.count = 0
            
        if self.count >= self.k:
            return True
        
        else:
            return False
        
#         self.datastream.append(num)
        
#         if len(self.datastream) < self.k:
#             return False
        
#         elif set(self.datastream[-(self.k):]) == set([self.value]):
#             return True
        
#         else:
#             return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)