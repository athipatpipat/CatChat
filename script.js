var messages = document.getElementById("messages");
var button = document.getElementById("button");
var textbox = document.getElementById("textbox");

button.addEventListener("click", function(){
  var newBox = document.getElementById("box")
  var newMessage = document.createElement("ul");
  newMessage.innerHTML = textbox.value;
  newBox.appendChild(newMessage);
  //message.appendChild(newBox);
  textbox.value = "";
});


// New Chat Window Popup

function openForm() {
  document.getElementById("Sport").style.display = "block";
}

function closeForm() {
  document.getElementById("Sport").style.display = "none";
}
