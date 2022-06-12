var form = document.querySelector('.formWithValidation')
var validateBtn = form.querySelector('.validateBtn')

var filenames = form.querySelector('.filenames')

alert('aaaaaaaaaaaaaaaaaaaaaaa')

form.addEventListener('submit', function (event) {
  event.preventDefault()
  fileType = filenames.value.split(".")
  if (fileType[fileType.length-1] != "xls" || "xlsx")
    console.log('some beatuful text')
    var error = document.createElement('div')
    error.className = 'error'
    error.style.color = 'red'
    error.innerHTML = 'Please choose .xls or .xlsx file'
    filenames.parentElement.insertBefore(error, filenames)

})