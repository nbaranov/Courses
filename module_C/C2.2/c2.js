function countEvenOddZero(array) {
    let even = odd = zero = 0;
    for (let item of array) {
        if (typeof(item) == 'number' && !isNaN(item)) {
            if (item === 0) {
                zero += 1
            } else {
                if (item % 2 == 0) {
                    even += 1
                } else { odd += 1 }
            }
        }
    }
    console.log(` Even elements: ${even}\n Odd elements: ${odd}\n Zero elements: ${zero} `)
}

const TEST_ARRAY = [12, 13, 1, 2, 5, 7, NaN, null, 0, '', 0, 'word', true, false]

countEvenOddZero(TEST_ARRAY)