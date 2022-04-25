
// Sliding search bar functionality taken from stack overflow, credited in README
//stackoverflow.com/questions/40626695/how-can-i-create-a-search-bar-that-slide-to-the-left-on-clicking-the-label
$("#searchbar .search-label").on("click", function(e){
    e.preventDefault();
    $("#searchbar").toggleClass("collapsed");
  });//click