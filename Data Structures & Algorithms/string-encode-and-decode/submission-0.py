class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str_lens, res = [], []
        for string in strs:
            str_lens.append(len(string))
        for sz in str_lens:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        str_lens, res, i = [], [], 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            str_lens.append(int(s[i:j]))
            i = j + 1
        i += 1

        for sz in str_lens:
            res.append(s[i:i + sz])
            i += sz
        return res

