const someObj = {
    property1 : 'abc',
    property2 : 123,
    property3 : true
}

//Задание 1
function printObjectProp (obj) {
    for (let property in obj) {
        if (obj.hasOwnProperty(property)) {
            console.log(property, obj[property]);
        }
    }
}

printObjectProp(someObj)


//Задание 2
str1 = 'property1'
str2 = 'qwerty'

function checkPropInObj (str, obj) {
    if (str in obj) {
        return true
    } else {return false}
}

console.log(checkPropInObj(str1, someObj))
console.log(checkPropInObj(str2, someObj))

//Задание 3
function createObjWithoutProto() {
    return Object.create(null);
}

emptyObj = createObjWithoutProto()

console.log(emptyObj)