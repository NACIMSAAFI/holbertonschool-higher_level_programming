document.getElementById('toggle_header').addEventListener('click', function() {
    var headerElement = document.querySelector('header');
    if (headerElement.classList.contains('green')) {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    } else {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    }
});
