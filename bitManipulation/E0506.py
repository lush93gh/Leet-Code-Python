class E0506:
    def convertInteger(self, A: int, B: int) -> int:
        normalizedA = A
        if A < 0:
            normalizedA = pow(2, 32) + A
        normalizedB = B
        if B < 0:
            normalizedB = pow(2, 32) + B
        num = normalizedA ^ normalizedB
        sum = 0
        while num> 0:
            sum += num % 2
            num //= 2
        return sum
    
a= E0506()
print(a.convertInteger(826966453, -729934991))