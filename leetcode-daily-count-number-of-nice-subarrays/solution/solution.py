from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, prefix_sum, curr_sum = 0, {0: 1}, 0
        for num in nums:
            curr_sum += num % 2
            count += prefix_sum.get(curr_sum - k, 0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return count