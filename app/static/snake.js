const board_border = "black";
const board_background = "white";
const snake_col = "purple";

let snake = [
  { x: 200, y: 200 },
  { x: 180, y: 200 },
  { x: 160, y: 200 },
  { x: 140, y: 200 },
  { x: 120, y: 200 },
];

let score = 0;
// True if changing direction
let changing_direction = false;
// Horizontal velocity
let food_x;
let food_y;
let dx = 20;
// Vertical velocity
let dy = 0;

// Get the canvas element
const snakeboard = document.getElementById("snakeboard");
// Return a two dimensional drawing context
const snakeboard_ctx = snakeboard.getContext("2d");
// Start game

document.addEventListener("keydown", change_direction);
clear_board();
gen_food();
drawFood();
drawSnake();
document.addEventListener("keypress", main);
// main function called repeatedly to keep the game running
function main() {
  document.removeEventListener("keypress", main);
  document.getElementById("start_message").innerHTML = "";
  if (has_game_ended()) return;

  changing_direction = false;
  setTimeout(function onTick() {
    clear_board();
    drawFood();
    move_snake();
    drawSnake();
    // Repeat
    main();
  }, 150);
}

// draw a border around the canvas
function clear_board() {
  //  Select the colour to fill the drawing
  snakeboard_ctx.fillStyle = board_background;
  //  Select the colour for the border of the canvas
  snakeboard_ctx.strokestyle = board_border;
  // Draw a "filled" rectangle to cover the entire canvas
  snakeboard_ctx.fillRect(0, 0, snakeboard.width, snakeboard.height);
  // Draw a "border" around the entire canvas
  snakeboard_ctx.strokeRect(0, 0, snakeboard.width, snakeboard.height);
}

// Draw the snake on the canvas
function drawSnake() {
  // Draw each part
  snake.forEach(drawSnakePart);
}

function drawFood() {
  snakeboard_ctx.fillStyle = "red";
  snakeboard_ctx.strokestyle = "black";
  snakeboard_ctx.beginPath();
  snakeboard_ctx.arc(food_x + 10, food_y + 10, 9, 0, 2 * Math.PI, false);
  snakeboard_ctx.stroke();
  snakeboard_ctx.fill();
}

// Draw one snake part
function drawSnakePart(snakePart) {
  // Set the colour of the snake part
  snakeboard_ctx.fillStyle = snake_col;
  // Set the border colour of the snake part
  snakeboard_ctx.strokestyle = snake_border;
  // Draw a "filled" rectangle to represent the snake part at the coordinates
  // the part is located
  snakeboard_ctx.fillRect(snakePart.x, snakePart.y, 20, 20);
  // Draw a border around the snake part
  // snakeboard_ctx.strokeRect(snakePart.x, snakePart.y, 20, 20);
}

function has_game_ended() {
  for (let i = 4; i < snake.length; i++) {
    if (snake[i].x === snake[0].x && snake[i].y === snake[0].y) return true;
  }
  const hitLeftWall = snake[0].x < 0;
  const hitRightWall = snake[0].x > snakeboard.width - 10;
  const hitTopWall = snake[0].y < 0;
  const hitBottomWall = snake[0].y > snakeboard.height - 10;
  return hitLeftWall || hitRightWall || hitTopWall || hitBottomWall;
}

function random_food(min, max) {
  return Math.round((Math.random() * (max - min) + min) / 20) * 20;
}

function gen_food() {
  var audio = new Audio("audio/apple.mp4");
  audio.play();

  // Generate a random number the food x-coordinate
  food_x = random_food(0, snakeboard.width - 20);
  // Generate a random number for the food y-coordinate
  food_y = random_food(0, snakeboard.height - 20);
  // if the new food location is where the snake currently is, generate a new food location
  snake.forEach(function has_snake_eaten_food(part) {
    const has_eaten = part.x == food_x && part.y == food_y;
    if (has_eaten) gen_food();
  });
}

function change_direction(event) {
  const LEFT_KEY = 37;
  const RIGHT_KEY = 39;
  const UP_KEY = 38;
  const DOWN_KEY = 40;

  // Prevent the snake from reversing

  if (changing_direction) return;
  changing_direction = true;
  const keyPressed = event.keyCode;
  const goingUp = dy === -20;
  const goingDown = dy === 20;
  const goingRight = dx === 20;
  const goingLeft = dx === -20;
  if (keyPressed === LEFT_KEY && !goingRight) {
    dx = -20;
    dy = 0;
  }
  if (keyPressed === UP_KEY && !goingDown) {
    dx = 0;
    dy = -20;
  }
  if (keyPressed === RIGHT_KEY && !goingLeft) {
    dx = 20;
    dy = 0;
  }
  if (keyPressed === DOWN_KEY && !goingUp) {
    dx = 0;
    dy = 20;
  }
}

function move_snake() {
  // Create the new Snake's head
  const head = { x: snake[0].x + dx, y: snake[0].y + dy };
  // Add the new head to the beginning of snake body
  snake.unshift(head);
  const has_eaten_food = snake[0].x === food_x && snake[0].y === food_y;
  if (has_eaten_food) {
    // Increase score
    score += 10;
    // Display score on screen
    document.getElementById("score").innerHTML = "Score: " + score;
    // Generate new food location
    gen_food();
  } else {
    // Remove the last part of snake body
    snake.pop();
  }
}