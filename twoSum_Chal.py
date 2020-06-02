#Challenge:

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def twoSum(self, nums, target):
        pass
        # If the sum of the value of 2 indices, in a list, equal the target, return the  two indices in a list
        # 1. Iterate over the list
        # 2. Need 2 loops i & j--0(n^2)--Will need to optimize later
        # 3. i is the current variable. j will iterate over the list.  If the target - j
        # equals i, return [i, j]

        #Want to return a list
        #Research list comprehension for list methods
        #Instead of iterating. Would it be possible to use recursion?
        #Dictionary? 

        # The base case is we don't want a conditon where 
        # 
        # if the current value of the index equals the target minus the next value in the array
        # return the current value and the next value. 
        #  If not try again with the next value

        #So given an array:
        # [1,2,3,4] target = 7
        # What we need to do is start with value[0] which is the current value,
        # Then check and see if current value[0] = currentValue[0 + 1] - target
        #The question is how to keep track of the iterations (meaning the index and the value) without using a nested loop

        #Question:  How we push items into a dictionary?
        

        #This is what I am looking for:
        #Given the array from above, su



        #Brute force
        # for i in range(0, len(nums)-1):
        #     for j in range(1, len(nums)-1):
        #         if (nums[i] == target - nums[j]):
        #             return [i, j]
