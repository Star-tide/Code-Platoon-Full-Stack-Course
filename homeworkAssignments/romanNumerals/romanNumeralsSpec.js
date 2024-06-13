function toRomanLazy(num) {
    let output = '';
    romanNumeralToArabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1 
    };
    for (const [roman, arabic] of Object.entries(romanNumeralToArabic)) {
        let repeat = Math.floor(num / arabic)
        num -= repeat * arabic
        if (repeat != 0) {
                output += roman.repeat(repeat)
        }
    }
        return output
}
console.log(toRomanLazy(2622))