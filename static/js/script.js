
// Sliding search bar functionality taken from stack overflow, credited in README
//stackoverflow.com/questions/40626695/how-can-i-create-a-search-bar-that-slide-to-the-left-on-clicking-the-label
$("#searchbar .search-label").on("click", function(e){
    e.preventDefault();
    $("#searchbar").toggleClass("collapsed");
  });//click


// Category cards on the home page, thanks to 
// https://codepen.io/nicolaskadis/pen/brQEOd

// <!-- NO JS VERSION: 
// https://codepen.io/nicolaskadis/full/brQEOd/ -->

$(document).ready(function() {
  var front = document.getElementsByClassName("front");
  var back = document.getElementsByClassName("back");

  var highest = 0;
  var absoluteSide = "";

  for (var i = 0; i < front.length; i++) {
    if (front[i].offsetHeight > back[i].offsetHeight) {
      if (front[i].offsetHeight > highest) {
        highest = front[i].offsetHeight;
        absoluteSide = ".front";
      }
    } else if (back[i].offsetHeight > highest) {
      highest = back[i].offsetHeight;
      absoluteSide = ".back";
    }
  }
  $(".front").css("height", highest);
  $(".back").css("height", highest);
  $(absoluteSide).css("position", "absolute");
});

