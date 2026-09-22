class Solution(object):
    def pivotIndex(self, nums):
        total = 0
        total1 = 0
        sumall = []
        sumall1 = []

        for i in range(len(nums)):
            total+=nums[i]
            sumall.append(total)
            
        for j in range(len(nums)-1,-1,-1):
            total1+=nums[j]
            sumall1.append(total1)
        
        sumall1.reverse()

        for i in range(len(nums)):
            if sumall[i] == sumall1[i]:
                return i
            

        return -1