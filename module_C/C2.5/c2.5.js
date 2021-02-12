function getSum(a) {
    return function(b) {
        return a + b
    }
};

const funcWithFirsValues = getSum(5);
console.log(funcWithFirsValues);

const sum = funcWithFirsValues(10);
console.log(sum);