class TimeMap:

    def __init__(self):
        self.state = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        values: list[tuple[int, str]] = self.state[key]
        values.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values: list[tuple[int, str]] = self.state[key]
        result = ""
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                result = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return result

# [(10, one), (20, two), (30, three)]
# target = 25
# m = 1
        
# (10, value1)

# [(1, happy), (3, sad)]
#  0,           1
#  target = 3
        
# [(1, happy)]
# [(1, happy), (3, sad), (4, neutral), (7, angry)]
# [0,           1,        2,            3        ]
# timestamp = 2
# 3 + 0 // 2 = 1
# l = 0, r = 1
# m = 0

# [(10, value1)]
