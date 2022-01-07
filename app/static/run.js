var character = document.getElementById("character");
var block = document.getElementById("block");
var changeCharacter = document.getElementById("changecharacter");
var changeBackground = document.getElementById("changebackground");
var game = document.getElementsByClassName("game")[0];
var counter = 0;

function jump() {
  if (character.classList == "animate") {
    return;
  }
  character.classList.add("animate");
  setTimeout(function () {
    character.classList.remove("animate");
  }, 300);
}

document.addEventListener("keypress", main);
function main() {
  document.removeEventListener("keypress", main);
  document.getElementById("block").classList.add("active");

  var checkDead = setInterval(function () {
    let characterTop = parseInt(
      window.getComputedStyle(character).getPropertyValue("top")
    );
    let blockLeft = parseInt(
      window.getComputedStyle(block).getPropertyValue("left")
    );
    if (blockLeft < 20 && blockLeft > -20 && characterTop >= 400) {
      block.style.animation = "none";
      alert("Game Over. score: " + Math.floor(counter / 100));
      clearInterval(checkDead);
    } else {
      counter++;
      document.getElementById("scoreSpan").innerHTML = Math.floor(
        counter / 100
      );
    }
  }, 10);
}

// changeCharacter.addEventListener("click", () => {
//   if (character.style.backgroundColor == "red") {
//     character.style.backgroundColor = "purple";
//   }
// });

var characterColors = [
  "white",
  "red",
  "blue",
  "purple",
  "black",
  "green",
  "yellow",
];
var i = 0;
changeCharacter.addEventListener("click", changechar);
function changechar() {
  i += 1;
  if (i > characterColors.length - 1) {
    i = 0;
  }
  character.style.backgroundColor = characterColors[i];
}

var x = 0;
changeBackground.addEventListener("click", changeback);
function changeback() {
  x += 1;
  if (x > characterColors.length - 1) {
    x = 0;
  }
  game.style.backgroundColor = characterColors[x];
}
