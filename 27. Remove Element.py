class Solution:
    def removeElement(self, nums, val) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums.pop(i)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        print(f"nums = {nums}")
        total = len(nums)
        return total
    
test = Solution()
nums = [3,2,2,3]
val = 2
test.removeElement(nums,val)