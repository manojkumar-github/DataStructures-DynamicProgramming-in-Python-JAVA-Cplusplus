class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def is_one_letter_word(word):
            n_diff = 0
            for i in range(len(word)):
                if beginWord[i] != word[i]:
                    n_diff += 1
            if n_diff == 1:
                return True
            return False

        if beginWord == endWord:
            return 0

        for index, word in enumerate(wordList):
            if is_one_letter_word(word):
                if word != endWord:
                    return 1 + self.ladderLength(word, endWord,
                                                 wordList[index:])
                else:
                    return 1
        return 0

input = "hit"
wlist = ["hot","dot","dog","lot","log","cog"]

obj = Solution()

print(obj.ladderLength(input, "cog", wlist))