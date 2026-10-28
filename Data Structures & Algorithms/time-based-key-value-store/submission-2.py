class TimeMap:

    def __init__(self):
        self.state = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        values: list[tuple[int, str]] = self.state[key]
        values.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values: list[tuple[int, str]] = self.state[key]
        if not values or timestamp < values[0][0]:
            return ""
        l, r = 0, len(values) - 1
        while l < r:
            m = (l + r) // 2
            if timestamp > values[m][0]:
                l = m + 1
            elif timestamp < values[m][0]:
                r = m - 1
            else:
                return values[m][1]
        return values[l - 1][1] if values[l][0] > timestamp else values[l][1]

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
