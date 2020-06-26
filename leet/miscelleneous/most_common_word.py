import string
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        tokens = paragraph.split()
        final_tokens = list()
        for tok in tokens:
            if tok.strip(string.punctuation) not in banned:
                final_tokens.append(tok.strip(string.punctuation).lower())
        return max(final_tokens, key=final_tokens.count).lower()

    def mostCommonWord_1(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))
        translated_text_tokens = paragraph.translate(translator).split()
        new_list = []
        for tok in translated_text_tokens:
            if tok.lower() not in banned:
                new_list.append(tok.lower())
        return max(new_list, key = new_list.count).lower()

if __name__ == '__main__':
    ip = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    obj = Solution()
    print(obj.mostCommonWord_1(ip, banned))