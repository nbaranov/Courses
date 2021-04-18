//Находим кнопку и добавляем действие по клику
const btnNode = document.querySelector('button')
    //Находим блок для вывода результата
const resultNode = document.querySelector('.result')
    //Загружаем карточки из прошлой сессии
loadLastCards()

btnNode.addEventListener('click', () => {
    // Получаем значени input'ов
    let page = Number(document.querySelector('#page').value)
    let limit = Number(document.querySelector('#limit').value)
    switch (true) {
        case (((!Number.isInteger(page)) || (page < 1) || (page > 10)) && ((!Number.isInteger(limit)) || (limit < 1) || (limit > 10))):
            console.log('Run case 3')
            tagInner('<p>Номер страницы и лимит вне диапазона от 1 до 10</p>');
            break;
        case ((!Number.isInteger(page)) || (page < 1) || (page > 10)):
            console.log('Run case 1')
            tagInner('<p>Номер страницы вне диапазона от 1 до 10</p>');
            break;
        case ((!Number.isInteger(limit)) || (limit < 1) || (limit > 10)):
            console.log('Run case 2')
            tagInner('<p>Лимит вне диапазона от 1 до 10</p>');
            break;
        case (((page >= 1) || (page <= 10)) && ((limit >= 1) || (limit <= 10))):
            getImages(page, limit, tagInner)
            break
    }
});

// Получаем url картинки и вызываем функуцию вставки картинки на страницу
async function getImages(page, limit) {
    let url = `https://picsum.photos/v2/list?page=${page}&limit=${limit}`
    return await fetch(url)
        .then((response) => { return response.json(); })
        .then((list) => {
            console.log(list)
            let cards = '';
            list.forEach((item) => {
                let card = `<div class="card">
                    <img
                      src="${item.download_url}"
                      class="card-image"
                    />
                    <p>Autor: ${item.author}</p>
                    <a href="${item.download_url}" target="_blank">Открыть оригинал</a>
                  </div>
                `;
                cards = cards + card;
            })
            return cards
        })
        .catch(() => {
            console.log('error get cards')
            tagInner(`<p>Не удалось получить данные</p>`)
        })
        .then((cards) => {
            tagInner(cards);
            localStorage.setItem('lastCards', cards)
        })
        .catch(() => { tagInner(`<p>Не удалось загрузить картинку</p>`) })
}

function tagInner(tags) {
    resultNode.innerHTML = tags
}

function loadLastCards() {
    const cards = localStorage.getItem('lastCards')
    tagInner(cards)
}