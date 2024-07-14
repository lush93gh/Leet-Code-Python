class M50:
    def myPow(self, x: float, n: int) -> float:
        result = 1.0
        mul, num = x, abs(n)
        while num > 0:                
            if num & 1:
                result *= mul
            mul *= mul
            num >>= 1
        return result if n >= 0 else 1 / result

    
a = M50()
print(a.myPow(x = 2.00000, n = 10))
print(a.myPow(x = 2.10000, n = 3))
print(a.myPow(x = 2.00000, n = -2))