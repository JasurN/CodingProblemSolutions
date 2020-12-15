/**
 * @param {string[]} strs
 * @return {string}
 */
let longestCommonPrefix = function (strs) {
    let prefix = "";
    let prefixSize = 1;
    if (strs.length > 0) {
        let initialPrefix = strs[0].charAt(0);
        for (let i = 0; i < strs[0].length; i++) {
            for (let j = 1; j < strs.length; j++) {
                if (initialPrefix !== strs[j].substr(0, prefixSize) || strs[j].length < prefixSize) {
                    // console.log(prefix);
                    return prefix;
                }
            }
            prefix = initialPrefix;
            if (strs[0].charAt(i + 1)) {
                initialPrefix = `${initialPrefix}${strs[0].charAt(i + 1)}`
                prefixSize++;
            }
        }
    }
    // console.log(prefix)
    return prefix;
};
longestCommonPrefix(strs = ["flower", "flow", "flight"]);

