'''
Subsequence Bitwise Goodnes
A network analysis tool is evaluating the performance of various servers by analyzing specific metrics represented as an array of integers. The performance goodness of a sequence is defined as the bitwise-OR of its elements. Given an array arr of length n, your task is to determine all possible distinct values of performance goodness that can be obtained by selecting any strictly increasing subsequence from the array. The result should be sorted in non-decreasing order.

Note: A subsequence is derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

Example
Consider n = 4, arr = [4, 2, 4, 1].

The strictly increasing subsequences that can be chosen to have distinct performance goodness values are:

Empty subsequence; performance goodness = 0
[1]; performance goodness = 1
[2]; performance goodness = 2
[4]; performance goodness = 4
[2, 4]; performance goodness = 6 (since 2 OR 4 = 6)
There are no other strictly increasing subsequences that yield a different performance goodness value. Therefore, the answer is [0, 1, 2, 4, 6], sorted in non-decreasing order.

Function Description
Complete the function getDistinctGoodnessValues in the editor below.

getDistinctGoodnessValues has the following parameter:

int arr[n]: an array of integers
Returns:

int[]: all possible distinct values of performance goodness
Constraints
1<= n <=10^4
1<= arr[i] <1024
'''
class SubsequenceBitwiseGoodnes:
    def getDistinctGoodnessValues(self, arr: list[int]) -> list[int]:
        table = {}
        ans = set()
        table[0] = 0
        ans.add(0)

        for n in arr:
            new_table = {}
            for idx, or_val in table.items():
                if or_val < n:
                    new_idx = idx | n
                    new_table[new_idx] = min(table.get(new_idx, float('inf')), n)
                    ans.add(new_idx)
            for idx, or_val in new_table.items():
                table[idx] = new_table[idx]
        
        return sorted(ans)
    

a = SubsequenceBitwiseGoodnes()
print(a.getDistinctGoodnessValues([4, 2, 4, 1]))
print(a.getDistinctGoodnessValues([2, 4, 6, 5]))
