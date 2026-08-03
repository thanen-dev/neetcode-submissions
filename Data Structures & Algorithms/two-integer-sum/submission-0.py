class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, number in enumerate(nums):
            missing_number = target - number
            if missing_number in dictionary:
                return [dictionary[missing_number], index]
            else:
                dictionary[number] = index