var slideIndex = 1;
showSlides(1);
function showSlides(n) {
  var slides = document.getElementsByClassName("mySlides");
  if (n == undefined) {
    n = ++slideIndex;
  }
  if (n > slides.length) {
    slideIndex = 1;
  }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 5000);
}

function notloggedin() {
  alert("Cannot Access! Login to view!");
}
