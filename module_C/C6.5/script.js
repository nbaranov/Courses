btnNode = document.querySelector('.btn')

btnNode.addEventListener('click', () => {
    const width = window.screen.width
    const height = window.screen.height
    window.alert(`Размеры вашего экрана:\nШирина - ${width}\nВысота - ${height}`)

})