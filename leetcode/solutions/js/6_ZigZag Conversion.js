/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = function (s, numRows) {
    if (numRows < 2) {
        return s;
    }
    let convertedArray = [];
    let initSize = Math.round((s.length / numRows + 1) * 2);
    for (let i = 0; i < numRows; i++) {
        convertedArray.push([]);
        for (let j = 0; j < initSize; j++) {
            convertedArray[i].push(null);
        }
    }
    let rowIndex = 0;
    let columnIndex = 0;
    for (let i = 0; i < s.length;) {
        for (let j = rowIndex; j < numRows && i < s.length; j++) {
            convertedArray[j][columnIndex] = s[i];
            i++
            rowIndex++
        }
        if (numRows > 2) {
            rowIndex--;
            for (let k = 0; k < numRows - 1 && i < s.length; k++) {
                --rowIndex
                ++columnIndex
                convertedArray[rowIndex][columnIndex] = s[i++];
            }
            rowIndex++;
        }
        if(numRows===2) {
            rowIndex--;
            rowIndex--;
            ++columnIndex
        }
    }
    let string = '';
    for (let i = 0; i < convertedArray.length; i++) {
        for (let j = 0; j < convertedArray[i].length; j++) {
            if (convertedArray[i][j]) {
                string = `${string}${convertedArray[i][j]}`
            }
        }
    }

    return string;
};


console.log(convert(s = "ABC", numRows = 2));
