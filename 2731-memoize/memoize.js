/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
  const cache = new Map();

  return function(...args) {
    // Create a unique key for the arguments
    const key = args.join(',');

    // If the result is already cached, return it
    if (cache.has(key)) {
      return cache.get(key);
    }

    // Otherwise, compute and cache the result
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */