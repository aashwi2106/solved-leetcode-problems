class Solution(object):
    def twoSum(self, nums, target):
        list1 = list(nums)
        i=0
        for i in range(len(list1)):
            for j in range(i+1,len(nums)):
                if list1[i] + nums[j] == target:
                    return [i,j]
                    break