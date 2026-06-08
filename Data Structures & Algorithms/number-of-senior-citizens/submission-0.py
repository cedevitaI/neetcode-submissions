class Solution:
    def countSeniors(self, details: List[str]) -> int:
        output = []
        for detail in details:
            if int(detail[11:13]) > 60:
                output.append(str(detail[:10]))
        return len(output)