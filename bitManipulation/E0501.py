class E0501:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        upper = N >> (j + 1) << (j+ 1)
        lower = N & (pow(2, i) - 1)
        mShiftedBits = M << i
        return upper + lower + mShiftedBits