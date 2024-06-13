// Here is the factorial challenge in javascript

function factorial(number) {
    // 0! or 1! will always be 1
    if (number === 0 || number === 1) {
        return 1;
    }
    // set factorial variable as my accumulator
    let factorial = number
    while (number >= 2) {
        factorial *= (number - 1)
        number--
    }

    return factorial
}

module.exports = { factorial }