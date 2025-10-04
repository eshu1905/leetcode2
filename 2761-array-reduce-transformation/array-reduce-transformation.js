/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let value=init;
    let len=nums.length;
    for (let i=0; i<len;i++){
        value=fn(value,nums[i])

    }
    return value

    
};