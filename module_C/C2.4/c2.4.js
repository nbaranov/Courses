function isPrime(value) {
    if (value > 1000) {
        console.log('Данные не верны')
        return undefined
    }

    if (value > 1) {
        let dividers = []
        for (let i = 3; i < value; i++) {
            if (value % i == 0) {
                dividers.push(i)
            }
        }
        if (dividers.length > 0) {
            console.log(`число ${value} -- составное делится на: ${dividers.join(', ')}`)
            return false
        }
    }
    console.log(`Число ${value} -- простое`)
    return true
}

const TEST_ARRAY = [0, 1, 2, 5, 7, 13, 15, 20, 25, 36, 111, 113, 150, 222, 525, 1000, 1100, 1500]

TEST_ARRAY.forEach(element => {
    isPrime(element)
});