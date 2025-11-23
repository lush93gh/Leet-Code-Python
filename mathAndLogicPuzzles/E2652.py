class E2652:
    def sumOfMultiples(self, n: int) -> int:
        mul_three = [i  for i in range(3, n + 1) if i %3 == 0]
        mul_five = [i  for i in range(5, n + 1) if i %5 == 0]
        mul_seven = [i  for i in range(7, n + 1) if i % 7 == 0]
        mul_fifteen = [i  for i in range(15, n + 1) if i % 15 == 0]
        mul_thirty_five = [i  for i in range(35, n + 1) if i % 35 == 0]
        mul_twenty_one = [i  for i in range(21, n + 1) if i % 21 == 0]
        mul_one_o_five = [i  for i in range(105, n + 1) if i % 105 == 0]

        return sum(mul_three) + sum(mul_five) + sum(mul_seven) - sum(mul_fifteen) - sum(mul_thirty_five) - sum(mul_twenty_one) + sum(mul_one_o_five)