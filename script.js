// Append the text into the box in Sports Chat & Send Text Once Click Enter
//var messages_sports = document.getElementById("messages_sports");
var button_sports = document.getElementById("button_sports");
var textbox_sports = document.getElementById("textbox_sports");

function sendSports(e) {
   if((e && e.keyCode == 13) || e == 0) {
     var newBox_sports = document.getElementById("box_sports")
     var newMessage_sports = document.createElement("ul");
     newMessage_sports.innerHTML = textbox_sports.value;
     newBox_sports.appendChild(newMessage_sports);
     //message.appendChild(newBox);
     textbox_sports.value = "";
   }
}


// Append the text into the box in Academics Chat & Send Text Once Click Enter
//var messages_academics = document.getElementById("messages1");
var button_academics = document.getElementById("button_academics");
var textbox_academics = document.getElementById("textbox_academics");

function sendAcademics(e) {
   if((e && e.keyCode == 13) || e == 0) {
     var newBox_academics = document.getElementById("box_academics")
     var newMessage_academics = document.createElement("ul");
     newMessage_academics.innerHTML = textbox_academics.value;
     newBox_academics.appendChild(newMessage_academics);
     //message.appendChild(newBox);
     textbox_academics.value = "";
   }
}

/*button1.addEventListener("click", function(){
  var newBox1 = document.getElementById("box1")
  var newMessage1 = document.createElement("ul");
  newMessage1.innerHTML = textbox1.value;
  newBox1.appendChild(newMessage1);
  //message.appendChild(newBox);
  textbox1.value = "";
});*/

// Sports Chat Window Popup
function openSports() {
  document.getElementById("Sports").style.display = "block";
  document.getElementById("Academics").style.display = "none";
}
function closeSports() {
  document.getElementById("Sports").style.display = "none";
}

// Academics Chat Window Popup
function openAcademics() {
  document.getElementById("Academics").style.display = "block";
  document.getElementById("Sports").style.display = "none";
}
function closeAcademics() {
  document.getElementById("Academics").style.display = "none";
}
