class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: list[int] = []
        sum: int = 0
        for op in operations:
            if op == "+":
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
                num = int(op)
                record.append(num)
                sum += num
        return sum
