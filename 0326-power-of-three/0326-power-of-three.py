class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n < 1:
            return False
        
        elif n == 1:
            return True
        
        else:
            return self.isPowerOfThree(n / 3)
        
#         if n == 1:
#             return True
        
#         elif n % 3 != 0 or n == 0:
#             return False
        
#         else:
#             return self.isPowerOfThree(n // 3)