/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const ans = {}
    for(let e of this){
        const key = fn((e))
        ans[key] ||=[]
        ans[key].push(e)
    }
    return ans
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */