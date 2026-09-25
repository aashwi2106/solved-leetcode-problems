class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        streak = 0
        max_streak = 0
        for i in nums:
            if i == 1:
                streak += 1
                max_streak = max(max_streak,streak)
            else:
                streak = 0
        return max_streak