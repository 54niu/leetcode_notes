"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers,
every element appears twice except for one. Find that single one.

Input: [2,2,1]
Output: 1

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""
from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber2(self, nums):
        return 2*sum(set(nums)) - sum(nums)

    def singleNumber3(self, nums):
        return reduce(operator.xor, nums)


nums = [4, 4, 5, 6, 6]
print(Solution().singleNumber(nums))
print(Solution().singleNumber2(nums))
print(Solution().singleNumber3(nums))

"""
任意一个数字异或自己都是0，0与任何数字进行异或都是任何数，所以将数组里的所有数进行异或两两相同的数都会抵消成0只剩下那个落单的数
"""