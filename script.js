// function for sport

// This is Matt's Way
/*$(function() {

  var $list, $newItemForm;
  $list = $('ul');
  $newItemForm = $('#newItemForm');


  $("#add").click(function(){
        var text = $('#itemField').val();
        $list.append('<li>' + text + '</li>');
        $('#itemField').val('');
    });
});*/

$(function() {
  /*var $newBox_sports document.getElementById("box_sports")*/
  var $list, $newItemForm;
  $list = $('ul');
  $newItemForm = $('#newItemForm');
  $newItemForm.on('submit', function(e) {
    e.preventDefault();
    var text = $('input:text').val();
    $list.append('<li>' + text + '</li>');
    $('#box_sports').scrollTop($('#box_sports')[0].scrollHeight);
    $('input:text').val('');
  });
});


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
