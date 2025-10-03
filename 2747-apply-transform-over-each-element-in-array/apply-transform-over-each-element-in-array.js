/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let len=arr.length;
    let jas=[];
    for(let i=0;i<len;i++){
        jas[i]=((fn(arr[i],i)))
        }
    return jas;    
    
};