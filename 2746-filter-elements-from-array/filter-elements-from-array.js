/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let len=arr.length;
    let new_arr=[]
    for (let i=0; i<len;i++){
        if (fn(arr[i],i)){
            new_arr.push(arr[i])
        }
       

    }
    return new_arr
};