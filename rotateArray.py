#Scarlett Chen
#2015.3.3
#Rotate Array
#rotate the first n-k numbers, then rotate the last k numbers, then rotate all numbers in the array
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k=k%len(nums)

        nums[0:-k]=reversed(nums[0:-k])
        nums[-k:]=reversed(nums[-k:])
        nums.reverse()