#Challenge:

#

class Solution:
    def twoSum(self, nums, target):
        '''
        If the sum of the value of 2 indices, in a list, equal the target, return the         two indices in a list
        1. Iterate over the list
        2. Need 2 loops i & j--0(n^2)--Will need to optimize later
        3. i is the current variable. j will iterate over the list.  If the target - j
        equals i, return [i, j]

        '''
        #Want to return a list
        #Research list comprehension for list methods
        #Instead of iterating. Would it be possible to use recursion?



        #Brute force
        # for i in range(0, len(nums)-1):
        #     for j in range(1, len(nums)-1):
        #         if (nums[i] == target - nums[j]):
        #             return [i, j]
