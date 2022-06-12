var form = document.querySelector('.formWithValidation')
var validateBtn = form.querySelector('.validateBtn')

var filenames = form.querySelector('.filenames')

//alert('aaaaaaaaaaaaaaaaaaaaaaa')


form.addEventListener('submit', function (event) {
    fileType = filenames.value.split(".")
    if (fileType[fileType.length-1] == "xls" ||fileType[fileType.length-1] == "xlsx") {
        console.log(form, validateBtn)
        event.requestSubmit(validateBtn);
        alert('aaaaaaaaaaaaaaaaaaaaaaa')

    } else {
        event.preventDefault()
        console.log(fileType[fileType.length-1])
        var error = document.createElement('div')
        error.className = 'error'
        error.style.color = 'red'
        error.innerHTML = 'Please choose .xls or .xlsx file'
        filenames.parentElement.insertBefore(error, filenames)
        var errors = form.querySelectorAll('.error')
        if(errors.length > 1)
            errors[errors.length-1].remove()
    }

})