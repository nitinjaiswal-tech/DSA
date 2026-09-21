class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0

        for i in range(32):
            count = 0

            for num in nums:
                if num & (1 << i):
                    count += 1

            if count % 3 != 0:
                answer |= (1 << i)

        if answer >= (1 << 31):
            answer -= (1 << 32)

        return answer