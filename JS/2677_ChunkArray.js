/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    if (size <= 0) {
      return [];
    }
  
    let chunkedArr = [];
    for (let i = 0; i < arr.length; i += size) {
      let chunk = arr.slice(i, i + size);
      chunkedArr.push(chunk);
    }
  
    return chunkedArr;
  };
  