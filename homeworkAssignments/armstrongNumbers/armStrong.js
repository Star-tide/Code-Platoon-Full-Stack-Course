const armstrong = (num) => {
    let total = 0
    let str = num.toString()
    if (str.length < 2) {
        return `${num} is an armstrong number`
    }

    for (let number in str) {
        total += str[number] ** str.length
    }
    if (total === num) {
        return `${num} is an armstrong number`
    } else { return `${num} is not an armstrong number`}
}

console.log(armstrong(371))