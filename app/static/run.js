var character = document.getElementById("character");
var block = document.getElementById("block");
var changeCharacter = document.getElementById("changecharacter");
var changeBlock = document.getElementById("changeblock");
var changeBackground = document.getElementById("changebackground");
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
    counter = 0;
    block.style.animation = "block 1s infinite linear";
  } else {
    counter++;
    document.getElementById("scoreSpan").innerHTML = Math.floor(counter / 100);
  }
}, 10);

changeCharacter.addEventListener("click", () => {
  if (character.style.backgroundColor == "red") {
    character.style.backgroundColor = "purple";
  }
});
