// fibonacci(n) = first + second

function fibonacci(nth) {
    if (nth == 2 || nth == 3) {
        return 1
    } else if (nth == 1) {
        return 0
    }

    let first = 1
    let second = 1
    let count = 3
    let fib = first + second

    while (count != nth) {
        count++
        first = second
        second = fib
        fib = first + second
    }

    return fib
}

console.log(fibonacci(11))