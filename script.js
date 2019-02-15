// Append the text into the box in Sports Chat
var messages_sports = document.getElementById("messages_sports");
var button_sports = document.getElementById("button_sports");
var textbox_sports = document.getElementById("textbox_sports");

button_sports.addEventListener("click", function(){
  var newBox_sports = document.getElementById("box_sports")
  var newMessage_sports = document.createElement("ul");
  newMessage_sports.innerHTML = textbox_sports.value;
  newBox_sports.appendChild(newMessage_sports);
  //message.appendChild(newBox);
  textbox_sports.value = "";
});

// Append the text into the box in Academics Char

var messages1 = document.getElementById("messages1");
var button1 = document.getElementById("button1");
var textbox1 = document.getElementById("textbox1");

button1.addEventListener("click", function(){
  var newBox1 = document.getElementById("box1")
  var newMessage1 = document.createElement("ul");
  newMessage1.innerHTML = textbox1.value;
  newBox1.appendChild(newMessage1);
  //message.appendChild(newBox);
  textbox1.value = "";
});


// Sports Chat Window Popup
function openSports() {
  document.getElementById("Sports").style.display = "block";
}
function closeSports() {
  document.getElementById("Sports").style.display = "none";
}

// Academics Chat Window Popup
function openAcademics() {
  document.getElementById("Academics").style.display = "block";
}
function closeAcademics() {
  document.getElementById("Academics").style.display = "none";
}
