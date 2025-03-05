<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GitHub README Snake Game</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        #game-container {
            text-align: center;
        }
        #game-board {
            border: 2px solid #333;
            background-color: #fff;
        }
        #score {
            font-size: 24px;
            margin-bottom: 10px;
        }
        #instructions {
            margin-top: 10px;
            color: #666;
        }
    </style>
</head>
<body>
    <div id="game-container">
        <div id="score">Score: 0</div>
        <canvas id="game-board" width="400" height="400"></canvas>
        <div id="instructions">
            Use Arrow Keys to Control the Snake
        </div>
    </div>

    <script>
        const canvas = document.getElementById('game-board');
        const ctx = canvas.getContext('2d');
        const scoreElement = document.getElementById('score');

        // Game settings
        const gridSize = 20;
        const tileCount = canvas.width / gridSize;

        // Snake initial state
        let snake = [
            {x: 10, y: 10},
        ];
        let food = getRandomFood();
        let dx = 1;
        let dy = 0;
        let score = 0;

        function getRandomFood() {
            return {
                x: Math.floor(Math.random() * tileCount),
                y: Math.floor(Math.random() * tileCount)
            };
        }

        function drawGame() {
            clearCanvas();
            moveSnake();
            drawSnake();
            drawFood();
            checkGameOver();
        }

        function clearCanvas() {
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        function drawSnake() {
            ctx.fillStyle = 'green';
            snake.forEach(segment => {
                ctx.fillRect(
                    segment.x * gridSize, 
                    segment.y * gridSize, 
                    gridSize - 2, 
                    gridSize - 2
                );
            });
        }

        function drawFood() {
            ctx.fillStyle = 'red';
            ctx.fillRect(
                food.x * gridSize, 
                food.y * gridSize, 
                gridSize - 2, 
                gridSize - 2
            );
        }

        function moveSnake() {
            const head = {x: snake[0].x + dx, y: snake[0].y + dy};
            snake.unshift(head);

            // Check if snake eats food
            if (head.x === food.x && head.y === food.y) {
                score++;
                scoreElement.textContent = `Score: ${score}`;
                food = getRandomFood();
            } else {
                snake.pop();
            }
        }

        function checkGameOver() {
            const head = snake[0];

            // Wall collision
            if (head.x < 0 || head.x >= tileCount || 
                head.y < 0 || head.y >= tileCount) {
                resetGame();
            }

            // Self collision
            for (let i = 1; i < snake.length; i++) {
                if (head.x === snake[i].x && head.y === snake[i].y) {
                    resetGame();
                }
            }
        }

        function resetGame() {
            snake = [{x: 10, y: 10}];
            food = getRandomFood();
            dx = 1;
            dy = 0;
            score = 0;
            scoreElement.textContent = `Score: ${score}`;
        }

        // Controls
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'ArrowUp':    
                    if (dy === 0) { dx = 0; dy = -1; }
                    break;
                case 'ArrowDown':  
                    if (dy === 0) { dx = 0; dy = 1; }
                    break;
                case 'ArrowLeft':  
                    if (dx === 0) { dx = -1; dy = 0; }
                    break;
                case 'ArrowRight': 
                    if (dx === 0) { dx = 1; dy = 0; }
                    break;
            }
        });

        // Game loop
        setInterval(drawGame, 100);
    </script>
</body>
</html>
