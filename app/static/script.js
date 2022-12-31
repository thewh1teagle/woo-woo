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
    e.preventDefault()
    if (!input.files.length) {
        input.files = e.dataTransfer.files
    }
    const file = input.files[0]
    const res = await fetch('/submit', {method: 'post', body: new FormData(form)})
    const object = await res.json()
    const result = object.result
    
    const fr = new FileReader()
    fr.addEventListener('load', () => {
        console.log('setting src...')
        modalImg.setAttribute('src', fr.result)
        console.log(fr.result)

    }, {once: true})
    fr.onload = () => {
        
    }
    fr.readAsDataURL(file)
    animalText.textContent = result === "cat" ? "It's a cat!" : result === "dog" ? "It's a dog!" : "Can't identify"
    modalWrapper.classList.add('active')
    drag.classList.remove('dragover')
    form.reset()
}
drag.addEventListener('drop', onDrop)
input.addEventListener('change', onDrop)

drag.addEventListener('dragover', (e) => {
    e.preventDefault() 
    drag.classList.add('dragover')
})

drag.addEventListener('dragstart', (e) => {
    e.preventDefault()  
})
drag.addEventListener('dragleave', (e) => {
    drag.classList.remove('dragover')
})

drag.addEventListener('click', e => {
    input.click()
})