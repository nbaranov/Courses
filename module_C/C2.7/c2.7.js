function printSomeValues(begin, end) {
    let current = begin;

    let timer = setInterval(function() {
        console.log(current);
        if (current == end) {
            clearInterval(timer)
        }
        current++;
    }, 1000);
}

a = parseInt(prompt('Input start value'))
b = parseInt(prompt('Input finish value'))

printSomeValues(a, b)