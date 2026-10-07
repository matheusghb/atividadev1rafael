function header () {
    const header = document.createElement('header')
    const btnline = document.createElement('div')
    const logo = document.createElement('a')

    btnline.className = 'btnline'
    logo.className = 'logo'
    
    const img = document.createElement('img')
    img.src = "static/imagens/lanches.png"
    const nome = document.createElement('h1')
    nome.innerHTML = 'Lá Ele LANCHES'
    
    logo.href = '/'

    if (pagina == "Pedido") { // não faço idéia de como acessar o comando static pelo javascript
        logo.append(nome)
    } else {
        logo.append(img, nome)
    }
    

    const lista = ['Salgados','Sanduiches','Bebidas']

    if (pagina != '') {
        lista.push('')
    }

    for (let i of lista) {

        const sitebtn = document.createElement('a')
        sitebtn.href = '/'+i
        if (i != '') {
            sitebtn.innerHTML = i
        } else {
            sitebtn.innerHTML = "Voltar"
            sitebtn.id = 'voltar'
        }
        btnline.append(sitebtn)

    }

    header.append(logo,btnline)

    return header
}
function footer () {

    const footer = document.createElement("footer")
    const line = document.createElement("hr")
    const copyright = document.createElement('p')
    const sobrenos = document.createElement('a')
    const textodiv = document.createElement('div')

    copyright.innerHTML = '©2026 La ele. Todos os direitos reservados.'
    sobrenos.innerHTML = 'Sobre nós'
    sobrenos.href = '/sobrenos'

    textodiv.append(copyright,sobrenos)
    footer.append(line,textodiv)

    return footer

}

function render(str) {

    const body = document.getElementsByTagName("body")[0]
    body.children[0].before(header())
    body.children[(body.children.length)-1].after(footer())

}

render(pagina)