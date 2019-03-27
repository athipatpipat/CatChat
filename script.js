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

$(function SportsFunction() {
  var $listSports, $newItemFormSports;
  $listSports = $('#message_sports');
  $newItemFormSports = $('#newItemFormSports');
  $newItemFormSports.on('submit', function(e) {
    e.preventDefault();
    var textSports = $('#newTextSports').val();
    $listSports.append('<li>' + textSports + '</li>');
    console.log(textSports);
    $('#box_sports').scrollTop($('#box_sports')[0].scrollHeight);
    $('#newTextSports').val('');
  });
});

$(function AcademicsFunction() {
  var $listAcademics, $newItemFormAcademics;
  $listAcademics = $('#message_academics');
  $newItemFormAcademics = $('#newItemFormAcademics');
  $newItemFormAcademics.on('submit', function(e) {
    e.preventDefault();
    var textAcademics = $('#newTextAcademics').val();
    console.log(textAcademics);
    $listAcademics.append('<li>' + textAcademics + '</li>');
    $('#box_academics').scrollTop($('#box_academics')[0].scrollHeight);
    $('#newTextAcademics').val('');
  });
});

// changes color of the buttons
var buttons = $('button');
buttons.click(function() {
  buttons.css('background-color', 'snow');
  $(this).css('background-color', 'pink');
});

// Append the text into the box in Academics Chat & Send Text Once Click Enter

// Sports Chat Window Popup
function openSports() {
  document.getElementById("Sports").style.display = "block";
  document.getElementById("Academics").style.display = "none";
}

// Academics Chat Window Popup
function openAcademics() {
  document.getElementById("Academics").style.display = "block";
  document.getElementById("Sports").style.display = "none";
}

sports-botton.addEventListener('click', changeColor, false)
