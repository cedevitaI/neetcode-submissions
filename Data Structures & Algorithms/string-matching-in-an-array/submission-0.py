class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for i in range(len(words)):
            curr_word = words[i]
            for j in range(len(words)):
                if i != j and curr_word in words[j]:
                    substrings.append(curr_word)
                    break
        return substrings