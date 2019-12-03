// Get the modal
var modal = document.getElementById("myModal");
var modall = document.getElementById("myModall");
var modalll = document.getElementById("myModalll");


// Get the button that opens the modal
var btn = document.getElementById("myBtn");
var btnn = document.getElementById("myBtnn");
var btnnn = document.getElementById("myBtnnn");


// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}
btnn.onclick = function() {
  modall.style.display = "block";
}
btnnn.onclick = function() {
  modalll.style.display = "block";
}


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
span.onclick = function() {
  modall.style.display = "none";
}
span.onclick = function() {
  modalll.style.display = "none";
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
window.onclick = function(event) {
  if (event.target == modall) {
    modall.style.display = "none";
  }
}
window.onclick = function(event) {
  if (event.target == modalll) {
    modalll.style.display = "none";
  }
}
var myWindow;
function closeWin() {
  myWindow.close();
}