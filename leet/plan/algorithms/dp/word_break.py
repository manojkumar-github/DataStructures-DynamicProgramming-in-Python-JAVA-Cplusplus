#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

memo = {}

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s in memo:
            return memo[s]
        if len(s) == 0:
            return False
        if len(s) == 1:
            return (s in wordDict)
        if s in wordDict:
            return True

        for word in wordDict:
            len_word = len(word)
            if len_word > len(s):
                continue
            left = s[:len_word + 1]
            right = s[len_word + 1:]

            if left in wordDict:
                if right in wordDict:
                    memo[s] = True
                    return True
                else:
                    right_verdict = self.wordBreak(right, wordDict)
                    memo[s] = right_verdict
                    if right_verdict:
                        return True
        memo[s] = False
        return False


obj = Solution()

#print(obj.wordBreak("leetcode", ["leet", "code"]))
print(obj.wordBreak("applepenapple", ["apple", "pen"]))
#print(obj.wordBreak("a", ["apple", "pen", "a"]))
#print(obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
# print(obj.wordBreak(
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa",
# "aaaaaaaaa","aaaaaaaaaa"]))

print(memo)


