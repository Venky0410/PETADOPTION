// home.js

// You can add your JavaScript code here to enhance the functionality of your home page
// For example, you can handle events, make AJAX requests, etc.

// Example: Alert message when clicking on a button
document.addEventListener('DOMContentLoaded', function() {
    // Get the button element
    var button = document.querySelector('.btn-primary');

    // Add a click event listener to the button
    button.addEventListener('click', function(event) {
        // Prevent the default action of the button (e.g., form submission)
        event.preventDefault();

        // Display an alert message
        alert('Button clicked!');
    });
});
