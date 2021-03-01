// Задание 1
// Строка для парсинга

const xmlString = `
<list>
<student>
  <name lang="en">
    <first>Ivan</first>
    <second>Ivanov</second>
  </name>
  <age>35</age>
  <prof>teacher</prof>
</student>
<student>
  <name lang="ru">
    <first>Петр</first>
    <second>Петров</second>
  </name>
  <age>58</age>
  <prof>driver</prof>
</student>
</list>
`;

const xmlParser = new DOMParser();
const xmlDOM = xmlParser.parseFromString(xmlString, 'text/xml')

let list = xmlDOM.querySelector('list')
const students = list.querySelectorAll('student')
list_ = []

for (let i = 0; i < students.length; i++) {
    let name_ = students[i].querySelector('name') 
    let lang_ = name_.getAttribute('lang')
    name_ = `${name_.querySelector('first').textContent} ${name_.querySelector('second').textContent}`
    let age_ = parseInt(students[i].querySelector('age').textContent)
    let prof_ = students[i].querySelector('prof').textContent
    list_.push({name: name_, age: age_, prof: prof_, lang: lang_})
}

const obj = {list: list_}
console.log(obj)


// Задание 2
// Строка для парсинга
const jsonString = `
{"list": [
    {
    "name": "Petr",
    "age": "20",
    "prof": "mechanic"
    },
    {
    "name": "Vova",
    "age": "60",
    "prof": "pilot"
    }
]}`;

const data = JSON.parse(jsonString)

data['list'].forEach(element => {
    element.age = parseInt(element['age'])
});

console.log(data)
