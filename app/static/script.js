const drag = document.querySelector('.drag')
const input = document.querySelector('input[type="file"]')
const form = document.querySelector('form')

const modalClose = document.querySelector('.modal > .close')
const modalWrapper = document.querySelector('.modal-wrapper')
const modalImg = document.querySelector('.modal > img')
const animalText = document.querySelector('.animal-text')

modalClose.addEventListener('click', () => {
    modalWrapper.classList.remove('active')
})

const onDrop = async (e) => {
    if (!input.files.length) {
        console.log('setting file..')
        console.log(e.dataTransfer)
        input.files = e.dataTransfer.files
    }
    
    const res = await fetch('/submit', {method: 'post', body: new FormData(form)})
    const object = await res.json()
    const result = object.result
    
    const fr = new FileReader()
    fr.addEventListener('load', () => {
        modalImg.setAttribute('src', fr.result)
    }, {once: true})
    fr.readAsDataURL(input.files[0])
    animalText.textContent = result === "cat" ? "It's a cat!" : result === "dog" ? "It's a dog!" : "Can't identify"
    modalWrapper.classList.add('active')
    drag.classList.remove('dragover')
    form.reset()
}
drag.ondrop = (e) => {
    e.preventDefault()
    onDrop(e)
}
input.addEventListener('change', onDrop)



drag.addEventListener('dragover', (e) => {
    e.preventDefault() 
    drag.classList.add('dragover')
})
drag.addEventListener('dragleave', (e) => {
    e.preventDefault()
    drag.classList.remove('dragover')
})

// drag.addEventListener('dragstart', (e) => {
//     e.preventDefault()  
// })


drag.addEventListener('click', e => {
    input.click()
})