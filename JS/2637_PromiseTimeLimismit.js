/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
	return async function(...args) {
        const originalFnPromise = fn(...args);

        const timeoutPromise = new Promise((_, reject) => {
            setTimeout(() => {
                reject('Time Limit Exceeded')
            }, t);
        })

        return Promise.race([originalFnPromise, timeoutPromise]);
        /* Promise.race() メソッドを使用して、2つの Promise オブジェクトの競争を行っています。originalFnPromise は元の関数 fn の実行結果を返す Promise です。timeoutPromise は指定された時間制限が経過した場合にタイムアウトエラーを発生させる Promise です。 */
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */