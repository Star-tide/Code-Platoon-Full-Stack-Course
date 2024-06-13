function angram(checkAnagram, checkList) {
    let grams = []
    let sorted = checkAnagram.split('').sort().join('')

    for (let word in checkList) {
        if(checkList[word].split('').sort().join('').toLowerCase() === sorted.toLowerCase()) {
            grams.push(checkList[word])
       }
    }
    return grams
}

console.log(angram("saltier", ["cognac", "saltier", "realist", "retails"]))