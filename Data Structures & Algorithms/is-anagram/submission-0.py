class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for s_c in s:
            if s_c not in hashmap:
                hashmap[s_c] = 1
            else:
                hashmap[s_c] += 1
        
        for t_c in t:
            if t_c not in hashmap:
                hashmap[t_c] = 1
            else:
                new_count = hashmap[t_c] - 1
                if new_count == 0:
                    del hashmap[t_c]
                else:
                    hashmap[t_c] = new_count
        
        return True if not hashmap else False