class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #copy from bbs
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


def main():
    s=Solution()
    nums = [3,2,4]
    target = 6
    result = s.twoSum(nums, target)
    print(result)

if __name__ == '__main__':
    main()