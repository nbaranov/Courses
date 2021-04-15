//100-300 слишком маленькие картинки поставил диапазон 200-500

// Ищем ноду для вставки результата запроса
const resultNode = document.querySelector('.image');
// Ищем кнопку, по нажатии на которую будет запрос
const btnNode = document.querySelector('.btn');

// Вешаем обработчик на кнопку для запроса
btnNode.addEventListener('click', () => {
    const height = document.querySelector('.height').value;
    const width = document.querySelector('.width').value
    console.log(height, width)
    if ((height >= 200 & width >= 200) & (height <= 500 & width <= 500) & (height != NaN & width != NaN)) {
        getImageURL(width, height, addTag);
    } else {
        resultNode.innerHTML = '<p>Число вне диапазона 100 - 300</p>'
    }
})

// Получаем url картинки и вызываем функуцию вставки картинки на страницу
function getImageURL(width, height, callback) {
    let url = `https://picsum.photos/${width}/${height}`
    return fetch(url)
        .then((response) => { return response.url; })
        //.then((url) => { console.log(url) })
        .catch(() => {
            console.log('error get url')
            callback(`<p>Не удалось загрузить картинку</p>`)
        })
        .then((url) => { callback(`<img src="${url}">`) })
        .catch(() => { callback(`<p>Не удалось загрузить картинку</p>`) })
}



function addTag(tag) {
    resultNode.innerHTML = tag
};