const sumPair = (numArr, requestedNum) => {
    let pairs = new Set([])
    for (let index in numArr) {
        for (let sum in numArr) {
            if (numArr[index] + numArr[sum] === requestedNum) {
                pairs.add([numArr[index], numArr[sum]])
            }
        }
    }
    return pairs
}

console.log(sumPair([1,2,3,4,5], 9))