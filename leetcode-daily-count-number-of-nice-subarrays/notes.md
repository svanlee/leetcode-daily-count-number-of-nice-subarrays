# Notes

Add your notes and explanations here.

Solved on LeetCode: NumberOfSubarraysWithKOddNumbers

Hey fellow coders!

I just solved the "NumberOfSubarraysWithKOddNumbers" problem on LeetCode and I'm excited to share my solution with you!

Problem Statement: Given an array of integers nums and an integer k, return the number of subarrays that have exactly k odd numbers.

My Solution: I used a prefix sum approach to solve this problem. The idea is to count the number of odd elements in each prefix of the array and store it in a dictionary. Then, for each prefix, I check if there is a previous prefix that has k fewer odd elements. If so, I add the count of such previous prefixes to the answer.

Here's the code: (Python3)

class Solution:
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
count, prefix_sum, curr_sum = 0, {0: 1}, 0
for num in nums:
curr_sum += num % 2
count += prefix_sum.get(curr_sum - k, 0)
prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
return count

Takeaways:
Prefix sum is a powerful technique for solving array problems.
Using a dictionary to store the count of prefixes with a certain number of odd elements can reduce the time complexity to O(n).

Don't be afraid to refactor your code to make it more concise and efficient!

Want to try it yourself? Head over to LeetCode and give it a shot! [link to the problem]

Let's connect! If you're interested in coding challenges or want to discuss this problem further, let's connect on LinkedIn!

hashtag#LeetCode hashtag#CodingChallenge hashtag#PrefixSum hashtag#ArrayProblems hashtag#CodingCommunity
