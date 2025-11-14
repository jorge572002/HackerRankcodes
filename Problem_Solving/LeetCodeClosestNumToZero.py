class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        #temmp variable to compare
        temp = nums[0]
        #iterate through array
        for i in nums:
            if abs(temp) > abs(i):
                temp = i
            elif abs(temp) == abs(i):
                if i > temp:
                    temp = i
            
        return temp