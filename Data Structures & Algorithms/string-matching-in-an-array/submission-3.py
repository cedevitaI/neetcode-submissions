class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for word1 in words:
            for word2 in words:
                if (word1 != word2) and (word1 in word2):
                    substrings.append(word1)
                    break
        return substrings