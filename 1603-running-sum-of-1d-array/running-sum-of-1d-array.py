class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nn=[]
        for i in range(len(nums)):
            s=0
            for j in range(i):
                s+=nums[j]
                
            nn.append(nums[i]+s)
        return nn

        