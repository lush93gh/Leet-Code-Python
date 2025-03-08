class E1009:
    def bitwiseComplement(self, n: int) -> int:
        number_bits = 1 if n == 0 else 0
        number = n
        while number > 0:
            number_bits += 1
            number = number >> 1
        return (1 << number_bits) - 1 - n