from typing import List

MOD = 10**9+7

class M2320:
    def countHousePlacements(self, n: int) -> int:
        one = self.fibMatrix(n+ 2)
        return one * one % MOD
    
    def f(self, n: int) -> int:
        a = 1
        b = 1
        c = a + b
        if n == 1:
            return a
        elif n == 2:
                return b
        
        for i in range(3, n + 1):
            c = a % MOD + b % MOD 
            a = b
            b = c
        return c % MOD 
    
    def fibMatrix(self, n: int) -> int:
        vector = [0, 1]
        m = [0, 1, 1, 1]
        num = n
        while num > 0:
            if num % 2 == 1:
                vector = self.vectorMatrixMul(vector=vector, matrix=m)
            m = self.matrixMul(m)
            num= num // 2

        return vector[0] % MOD
    
    def matrixMul(self, m: List[int]) -> List[int]:
        a, b, c, d = [x % MOD for x in m]
        return [a*a+b*c, a*b+b*d, c*a+d*c, c*b+d*d]
    
    def vectorMatrixMul(self, vector: List[int], matrix: List[int]) -> List[int]:
        a, b, c, d = [x % MOD for x in matrix]
        e, f = [x % MOD for x in vector]
        return [a*e+b*f, c*e+d*f]
         
        
a = M2320()
print(a.countHousePlacements(1))
print(a.countHousePlacements(2))
print(a.countHousePlacements(1000000))