// var myIndex = 0;
// carousel();

// function carousel() {
//   var x = document.getElementsByClassName("mySlides");
//   for (var i = 0; i < x.length; i++) {
//     x[i].style.display = "none";  
//   }
//   myIndex++;
//   if (myIndex > x.length) {myIndex = 1}   
//   if (myIndex < 1) {myIndex = x.length} 
//   x[myIndex-1].style.display = "block";  
//   setTimeout(carousel, 5000); // Change image every 5 seconds
// }

// function plusDivs(n) {
//     myIndex += n;
//   }
var myIndex = 0;
carousel(1);

function carousel(n) {
    clearInterval(myTimer)
    auto(n);
    function auto(f){
    var x = document.getElementsByClassName("mySlides");
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    myIndex += f;
    if (myIndex > x.length) {myIndex = 1}
    if (myIndex < 1) {myIndex = x.length}
    x[myIndex - 1].style.display = "block"
}
    var myTimer = setInterval(auto(1), 5000);
}