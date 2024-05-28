document.getElementById('add_item').addEventListener('click', function() {
    var ulElement = document.querySelector('ul');
    var liElement = document.createElement('li');
    liElement.textContent = 'Item';
    ulElement.appendChild(liElement);
});
