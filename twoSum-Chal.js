// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

//     Example:

// Given nums = [2, 7, 11, 15], target = 9,

//     Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

function twoSum(nums, target) {
    //Questions:  Is the array sorted? Will an unsorted array array work well with this algorithm? => Unsorted arrays will return undefined.  Need to create an isSorted function.

    //1. Loop through the nums array and if 2 values equal the target, return the indices of their values.
    //2. Make one variable,  starting at the left right at the first index(0)
    let left = 0;
    //3. make another variable starting at the right, which will be at the other end of the array.
    let right = nums.length - 1;
    //4. Now loop through the array.  While left is less than right, if the sum of the left and the right equals the target, then return the indices of their values.
    for (i = 0; i < nums.length; i++) {
        nums.sort();
    }
    while(left < right) {
        if (nums[left] + nums[right] === target) {
            return [left, right]
        }else if(nums[left] + nums[right] !== target) {
            right --
        }else {
            left ++
        }
    }
    //5. If not decrement the index of the value on the right
    //6. And increment the value of the index on the left.



    // for (let i=0; i < nums.length; i++) {
    //     for(let j=1; j < nums.length; j++){
    //         if (nums[i] + nums[j] === target) {
    //             return [i, j]
    //         }
    //     }
    // }

}

console.log(twoSum([3,2,4], 6))