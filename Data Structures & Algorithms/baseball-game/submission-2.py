import re

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: list[int] = []
        sum: int = 0
        for op in operations:
            if re.match(r"^-?\d+$", op):
                num = int(op)
                record.append(num)
                sum += num
            elif op == "+":
                num = record[-1] + record[-2]
                record.append(num)
                sum += num
            elif op == "D":
                num = record[-1] * 2
                record.append(num)
                sum += num
            elif op == "C":
                num = record.pop()
                sum -= num
            else:
                raise Exception("Programming error")
        return sum
