from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1
    

        if 1 in count:
            ans = count[1] if count[1] % 2 else count[1] - 1

        for x in count:
            if x == 1:
                continue

            cur = x
            length = 0

            while count.get(cur, 0) >= 2:
                length += 2
                cur = cur * cur

            if count.get(cur, 0):
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans