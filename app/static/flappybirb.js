const block = document.getElementById("block");
let hole = document.getElementById("hole");
let character = document.getElementById("character");
let jump = 0;
hole.addEventListener("animationiteration", () => {
  let random = -(Math.random() * 200 + 150);
  hole.style.top = random + "px";
});
setInterval(function () {
  let characterTop = parseInt(
    window.getComputedStyle(character).getPropertyValue("top")
  );
  character.style.top = characterTop + 3 + "px";
}, 10);
