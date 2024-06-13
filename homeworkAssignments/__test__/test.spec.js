const { factorial } = require("../factorialChallenge/factorial.js")

describe('factorial.js', () => {
    test("Testing for functionality of the factorial function", () => {
        expect(factorial(0)).toBe(1)
    })
    test("Testing for functionality of the factorial function", () => {
        expect(factorial(1)).toBe(1)
    })
    test("Testing for functionality of the factorial function", () => {
        expect(factorial(3)).toBe(6)
    })
    test("Testing for functionality of the factorial function", () => {
        expect(factorial(5)).toBe(120)
    })
})