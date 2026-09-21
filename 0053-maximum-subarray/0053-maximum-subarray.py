class Solution(object):
    def maxSubArray(self, nums):
        max1 = nums[0]
        sum = 0
        for i in nums:
            sum+=i
            max1 = max(max1,sum)
            if sum<0:
                sum=0
        return max1