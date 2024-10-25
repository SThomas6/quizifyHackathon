
// Add a function for each dropbox to show the content of that specific dropbox
// this is done by adding (toggling) the show class to the chosen dropbox
function dropBox1() {
    document.getElementById("categories").classList.toggle("show");
  }

function dropBox2() {
  document.getElementById("difficulties").classList.toggle("show");
}

function dropBox3() {
  document.getElementById("popularities").classList.toggle("show");
}

// Add a function to close any open dropboxes if the user clicks outside of a dropbox
// listen for clicks anywhere on the page
window.onclick = function(event) {
  // Check if the click is outside the dropdowns (not on .dropbtn)
  if (!event.target.matches('.dropbtn')) {
      // Iterate throug dropdown elements and close if they are open
      var dropdowns = document.getElementsByClassName("dropdownContent");
      for (var i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          // If the dropdown is open, close it by removing show
          if (openDropdown.classList.contains('show')) {
              openDropdown.classList.remove('show');
          }
      }
  }
}