function useRequest(url, callback) {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);

    xhr.onload = function() {
        if (xhr.status != 200) {
            console.log('Код ошибки: ', xhr.status);
        } else {
            const result = JSON.parse(xhr.response);
            if (callback) {
                callback(result);
            }
        }
    };

    xhr.onerror = function() {
        console.log('Ошибка! Код ошибки: ', xhr.status);
    };

    xhr.send();
};

function displayResult(apiData) {
    let cards = '';

    apiData.forEach(item => {
        const cardBlock = `
        <div class="card">
          <img
            src="${item.download_url}"
            class="card-image"
          />
          <p>${item.author}</p>
        </div>
      `;
        cards = cards + cardBlock;
    });

    resultNode.innerHTML = cards;
}


// Ищем ноду для вставки результата запроса
const resultNode = document.querySelector('.images');
// Ищем кнопку, по нажатии на которую будет запрос
const btnNode = document.querySelector('button');


// Вешаем обработчик на кнопку для запроса
btnNode.addEventListener('click', () => {
    let count = Number(document.querySelector('input').value)
    if ((count >= 1) & (count <= 10) & (count != NaN)) {
        let url = `https://picsum.photos/v2/list/?limit=` + count
        useRequest(url, displayResult);
    } else {
        resultNode.innerHTML = '<p>Число вне диапазона от 1 до 10</p>'
    }
})