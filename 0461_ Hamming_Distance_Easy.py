"""
# 题目 #
https://leetcode.com/problems/hamming-distance/

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.


# 思路 #

两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符个数。换而言之就是将一个字符串替换为另一个字符串所需要的字符个数。

例如：二进制数 001与100之间的汉明距离是2。

本题中需要将x，y变化成二进制字符串后再进行比较。

而 ^ 运算符则表示两个数字的二进制形式对应位置的字符相同则为0，不同则为1。
bin()函数的作用就是将整数转换为二进制数，

"""


# 代码：

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")



