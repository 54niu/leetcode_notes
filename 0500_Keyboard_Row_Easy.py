"""
# 题目 #
https://leetcode.com/problems/keyboard-row/
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of
American keyboard like the image below.

给定一组单词，返回可以用美式键盘中的某一行字母键入的所有单词。

注意：

键盘中的字符可以使用多次

可以假设输入只包含小写或者大写字母

# 思路 #

用正则表达式解决问题

"""
# 代码:
import re


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return list(filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words))


res = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
print(res)
