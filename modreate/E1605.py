class E1605:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        num = n
        while num >=5:
            num = num // 5
            sum += num
        return sum

a = E1605()

print(a.trailingZeroes(0))
print(a.trailingZeroes(3))
print(a.trailingZeroes(7))
print(a.trailingZeroes(50))
print(a.trailingZeroes(125))
print(a.trailingZeroes(200))