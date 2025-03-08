import math

class E476:
    def findComplement(self, num: int) -> int:
        number_bits = 0
        number = num
        while number > 0:
            number_bits += 1
            number = number >> 1
        return (1 << number_bits) - 1 - num

print(int(math.log2(5)) + 1)
a = E476()
print(a.findComplement(5))
print(a.findComplement(1))