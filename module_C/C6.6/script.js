const wsUrl = "wss://echo.websocket.org/";
let coords = {} //Переменная для сохранения координатов

//Находим элементы интуп, книпки и поле для вывода сообщений.
const input = document.querySelector('.input-text');
const output = document.querySelector(".chat-window");
const btnSend = document.querySelector('.btn-send');
const btnGeo = document.querySelector('.btn-geo');

//Создаем вебсокет с обработчиком событий сообщений
let websocket = new WebSocket(wsUrl);
websocket.onmessage = function(evt) {
    if (!(evt.data.includes(`<a href="https://www.openstreetmap.org/#map=10/${coords.latitude}/${coords.longitude}" target="_blank">Я тут</a>`))) {
        writeToScreenRecieve(`${evt.data}`)
    }
};

// Отправка сообщений по нажатию Enter и кнопки Отправить
document.querySelector('.input-text').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        const message = readAndClearInput()
        sendMessage(message)
    }
});

btnSend.addEventListener('click', () => {
    const message = readAndClearInput()
    sendMessage(message)
});

// Функции отправки сообщений и добавления сообщений в окно чата. 
function readAndClearInput() {
    const message = input.value;
    input.value = ''
    return message
}


function sendMessage(message) {
    if (message !== '') {
        writeToScreenSend(message);
        websocket.send(message);
    }
}

function writeToScreenSend(message) {
    let pre = document.createElement("p");
    pre.className = "send message";
    pre.innerHTML = message;
    output.appendChild(pre);
    output.scrollTop = output.scrollHeight
}

function writeToScreenRecieve(message) {
    let pre = document.createElement("p");
    pre.className = "recieve message";
    pre.innerHTML = message;
    output.appendChild(pre);
    output.scrollTop = output.scrollHeight
}


//Получаем геопозицию и отправляем серверу в виде ссылки
btnGeo.addEventListener('click', () => {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition((position) => {
            coords = position;
            sendMessage(`<a href="https://www.openstreetmap.org/#map=10/${coords.latitude}/${coords.longitude}" target="_blank">Я тут</a>`)
        });
        output.scrollTop = output.scrollHeight
    }
})