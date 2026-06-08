class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        possible_prefixes = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                possible_prefixes.append(chars[0])
            else: break
        return "".join(possible_prefixes)

        