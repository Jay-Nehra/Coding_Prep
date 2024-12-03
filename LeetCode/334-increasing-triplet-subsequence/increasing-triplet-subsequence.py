# """
#     Increasing triplet subsequence


#     nums: interger array,
#     if there are three consusecutive elements which are in the increasing order:
#         return true

# """


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #         # i = 0
        #         # while i < len(nums)-2:
        #         #     if nums[i+1]>nums[i] and nums[i+2]>nums[i+1]:
        #         #         return True
        #         #     i += 1
        #         # return False
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
