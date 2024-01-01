// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

function cancelRegistration() {
    // Add any cancellation logic here
    alert("Registration Cancelled");
}

//-------------js---modal---Success--------------------------
// Đóng modal khi người dùng click bên ngoài modal
window.onclick = function(event) {
  var modal2 = document.getElementById("successModal");
  if (event.target === modal2) {
    modal2.style.display = "none";
  }
}
