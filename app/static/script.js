const drag = document.querySelector('.drag')
const input = document.querySelector('input[type="file"]')
const form = document.querySelector('form')

const modal = document.querySelector('.modal')
const modalClose = document.querySelector('.modal > .close')
const modalWrapper = document.querySelector('.modal-wrapper')
const modalImg = document.querySelector('.modal > img')
const animalText = document.querySelector('.animal-text')

async function upload_image() {
    const res = await fetch('/submit', {method: 'post', body: new FormData(form)})
    const json = await res.json()
    const animal = json.animal
    return animal
}

function setModalImage() {
    const fr = new FileReader()
    fr.addEventListener('load', () => {
        modalImg.setAttribute('src', fr.result)
    }, {once: true})
    fr.readAsDataURL(input.files[0])
}

async function processImage() {
    setModalImage()
    const animal = await upload_image()
    animalText.textContent = 
        animal === "cat" ? "It's a cat!" : 
        animal === "dog" ? "It's a dog!" : 
        "Can't identify"
    modalWrapper.classList.add('active')
    drag.classList.remove('dragover')
    form.reset()
}

function onDrop(e) {
    e.preventDefault()
    if (!input.files.length) {
        input.files = e.dataTransfer.files
    }
    processImage()
}

function onDragOver(e) {
    e.preventDefault() 
    drag.classList.add('dragover')
}

function onDragLeave(e) {
    e.preventDefault()
    drag.classList.remove('dragover')
}

function onPaste(e) {
    if (!input.files.length) {
        input.files = e.clipboardData.files;
    }
    processImage()
} 

window.addEventListener('paste', onPaste);

modal.addEventListener('click', (e) => e.stopPropagation())
modalWrapper.addEventListener('click', () => modalWrapper.classList.remove('active'))
drag.addEventListener('drop', onDrop)
modalClose.addEventListener('click', () => modalWrapper.classList.remove('active'))
input.addEventListener('change', onDrop)
drag.addEventListener('dragover', onDragOver)
drag.addEventListener('dragleave', onDragLeave)
drag.addEventListener('click', (e) => input.click())