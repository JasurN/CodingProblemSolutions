let isValid = function (s) {
    let parenthesesStack = [];

    if (s.length < 2) {
        return false;
    }
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === ']' && (parenthesesStack.length < 1 || parenthesesStack[parenthesesStack.length - 1] !== '[')) {
            return false;
        } else if (s.charAt(i) === '}' && (parenthesesStack.length < 1 || parenthesesStack[parenthesesStack.length - 1] !== '{')) {
            return false;
        } else if (s.charAt(i) === ')' && (parenthesesStack.length < 1 || parenthesesStack[parenthesesStack.length - 1] !== '(')) {
            return false;
        } else if (s.charAt(i) === '(' || s.charAt(i) === '[' || s.charAt(i) === '{') {
            parenthesesStack.push(s.charAt(i))
        } else {
            parenthesesStack.pop();
        }
        if (i > s.length - 2 && parenthesesStack.length > 0) {
            return false;
        }
    }
    return true;
};
