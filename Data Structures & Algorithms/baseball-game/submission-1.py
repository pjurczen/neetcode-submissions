import re

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: list[int] = []
        sum: int = 0
        idx: int = 0
        for op in operations:
            if re.match(r"^-?\d+$", op):
                num = int(op)
                record.append(num)
                sum += num
                idx += 1
            elif op == "+":
                num = record[idx - 1] + record[idx - 2]
                record.append(num)
                sum += num
                idx += 1
            elif op == "D":
                num = record[-1] * 2
                record.append(num)
                sum += num
                idx += 1
            elif op == "C":
                num = record.pop()
                sum -= num
                idx -= 1
            else:
                raise Exception("Programming error")
        return sum
