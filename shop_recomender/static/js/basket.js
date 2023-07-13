
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener('DOMContentLoaded', function() {
  // Get all the "Add to Basket" buttons
  var addToBasketButtons = document.querySelectorAll('.add-to-basket-btn');

  // Attach a click event listener to each button
  addToBasketButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      console.log('Button clicked'); // Add this line for debugging
      
      var productId = this.dataset.productId; // Get the product ID from the data attribute

      // Send an AJAX request to add the product to the basket
      var xhr = new XMLHttpRequest();
      xhr.open('POST', '/add_to_basket/' + productId + '/');
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
      xhr.onload = function() {
        if (xhr.status === 200) {
          // Handle a successful response (product added to the basket)
          var response = JSON.parse(xhr.responseText);
          alert(response.message);
        } else {
          // Handle an error response
          alert('Error: ' + xhr.responseText);
        }
      };
      xhr.send();
    });
  });
});
