function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
    if(!l1 && !l2) {
        return l1;
    }
    let l3 = new ListNode();
    let ifFirst = true;
    while (l1 !== null || l2 !== null) {
        let tempL = new ListNode();
        if (l1 && l2 === null) {
            tempL.val = l1.val;
            l1 = l1.next
        } else if (l1 === null && l2) {
            tempL.val = l2.val;
            l2 = l2.next
        } else if (l1.val >= l2.val) {
            tempL.val = l2.val
            l2 = l2.next
        } else {
            tempL.val = l1.val;
            l1 = l1.next;
        }
        if (ifFirst) {
            l3 = tempL;
            ifFirst = false;
            // temps.push(tempL);
        } else {
            let nextList = findTail(l3);
            nextList.next = tempL;
        }
    }
    return l3;
};

var findTail = function (l1) {
    if (l1.next) {
        return findTail(l1.next)
    }
    return l1
}

const s1 = new ListNode(4);
const s2 = new ListNode(2, s1);
const s3 = new ListNode(1, s2);
const c1 = new ListNode(4);
const c2 = new ListNode(3, c1);
const c3 = new ListNode(1, c2);
console.log(mergeTwoLists(c3, s3));





