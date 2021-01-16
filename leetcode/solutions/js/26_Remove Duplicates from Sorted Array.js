/**
 * @param {number[]} nums
 * @return {number}
 */
let removeDuplicates = function (nums) {
    let arrayLength = nums.length;
    let arrayStart = 0;
    for (let i = arrayStart; i < arrayLength;) {
        if (nums[i] === nums[i + 1]) {
            nums.splice(i, 1)
            arrayLength--;
        }else {
            i++
        }

    }
    // console.log(nums);
    return nums.length;
};
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
