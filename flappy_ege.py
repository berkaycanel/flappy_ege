import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="Flappy Ege",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def get_image_base64():
    try:
        img_path = Path("IMG_3869.jpg")
        if img_path.exists():
            with open(img_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        return ""
    except:
        return ""

img_base64 = get_image_base64()

game_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>

body {{
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: Arial, sans-serif;
}}

#gameContainer {{
    text-align: center;
    padding: 20px;
}}

canvas {{
    border: 5px solid white;
    border-radius: 15px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    display: block;
    margin: 20px auto;
    background: linear-gradient(180deg, #87CEEB 0%, #E0F6FF 100%);
    cursor: pointer;
    width: min(95vw, 800px);
    height: auto;
}}

#score {{
    font-size: 2.5em;
    color: white;
    font-weight: bold;
}}

#highScore {{
    font-size: 1.2em;
    color: #ffd700;
    font-weight: bold;
}}

.gameOver {{
    color: #ff4444;
    font-size: 3em;
    font-weight: bold;
    animation: pulse 1s infinite;
}}

@keyframes pulse {{
    0%,100% {{ transform: scale(1); }}
    50% {{ transform: scale(1.1); }}
}}

button {{
    font-size: 1.2em;
    padding: 12px 30px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    margin: 10px;
}}

#instructions {{
    color: white;
    margin-top: 10px;
}}

</style>
</head>

<body>
<div id="gameContainer">
    <div id="highScore">🏆 En Yüksek: <span id="highScoreValue">0</span></div>
    <div id="score">SKOR: <span id="scoreValue">0</span></div>
    <div id="gameOverText" style="display:none;" class="gameOver">💀 OYUN BİTTİ 💀</div>
    <canvas id="gameCanvas"></canvas>

    <div id="instructions">
        ⬆️ SPACE / YUKARI OK / TIKLA - Zıpla<br>
        🎮 Yeşil borulardan geç!
    </div>

    <button id="startButton" onclick="startGame()">🚀 BAŞLA</button>
    <button id="restartButton" onclick="restartGame()" style="display:none;">🔄 YENİDEN</button>
</div>

<script>

document.body.style.touchAction = "manipulation";

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

function resizeCanvas() {{
    const isMobile = window.innerWidth < 768;
    if (isMobile) {{
        canvas.width = 360;
        canvas.height = 500;
    }} else {{
        canvas.width = 800;
        canvas.height = 600;
    }}
}}

window.addEventListener("resize", resizeCanvas);
resizeCanvas();

let gameStarted = false;
let gameOver = false;
let score = 0;
let highScore = localStorage.getItem('flappyEgeHighScore') || 0;
document.getElementById('highScoreValue').textContent = highScore;

const bird = {{
    x: 100,
    y: 250,
    width: 50,
    height: 50,
    velocity: 0,
    gravity: 0.6,
    jump: -12,
    image: new Image(),
    imageLoaded: false
}};

const imageData = '{img_base64}';
if (imageData) {{
    bird.image.onload = () => bird.imageLoaded = true;
    bird.image.src = 'data:image/jpeg;base64,' + imageData;
}}

let pipes = [];
const pipeWidth = 80;
let pipeGap = window.innerWidth < 768 ? 230 : 200;
const pipeSpeed = 3;
let frameCount = 0;

document.addEventListener('keydown', (e) => {{
    if ((e.code === 'Space' || e.code === 'ArrowUp') && gameStarted && !gameOver) {{
        e.preventDefault();
        jump();
    }}
}});

canvas.addEventListener('click', () => {{
    if (gameStarted && !gameOver) jump();
}});

canvas.addEventListener('touchstart', (e) => {{
    e.preventDefault();
    if (gameStarted && !gameOver) jump();
}});

function jump() {{
    bird.velocity = bird.jump;
}}

function startGame() {{
    gameStarted = true;
    gameOver = false;
    score = 0;
    bird.y = 250;
    bird.velocity = 0;
    pipes = [];
    frameCount = 0;

    document.getElementById('startButton').style.display = 'none';
    document.getElementById('restartButton').style.display = 'none';
    document.getElementById('gameOverText').style.display = 'none';
    document.getElementById('scoreValue').textContent = score;

    gameLoop();
}}

function restartGame() {{
    startGame();
}}

function createPipe() {{
    const gapY = Math.random() * (canvas.height - pipeGap - 200) + 100;
    pipes.push({{ x: canvas.width, gapY: gapY, scored: false }});
}}

function updateBird() {{
    bird.velocity += bird.gravity;
    bird.y += bird.velocity;

    if (bird.y < 0) {{
        bird.y = 0;
        bird.velocity = 0;
    }}
    if (bird.y + bird.height > canvas.height - 20) {{
        endGame();
    }}
}}

function updatePipes() {{
    frameCount++;
    if (frameCount % 90 === 0) createPipe();

    for (let i = pipes.length - 1; i >= 0; i--) {{
        pipes[i].x -= pipeSpeed;

        if (!pipes[i].scored && pipes[i].x + pipeWidth < bird.x) {{
            score++;
            pipes[i].scored = true;
            document.getElementById('scoreValue').textContent = score;

            if (score > highScore) {{
                highScore = score;
                localStorage.setItem('flappyEgeHighScore', highScore);
                document.getElementById('highScoreValue').textContent = highScore;
            }}
        }}

        if (bird.x + bird.width > pipes[i].x &&
            bird.x < pipes[i].x + pipeWidth) {{
            if (bird.y < pipes[i].gapY ||
                bird.y + bird.height > pipes[i].gapY + pipeGap) {{
                endGame();
            }}
        }}

        if (pipes[i].x + pipeWidth < 0) {{
            pipes.splice(i, 1);
        }}
    }}
}}

function draw() {{
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    pipes.forEach(pipe => {{
        ctx.fillStyle = '#2ECC71';
        ctx.fillRect(pipe.x, 0, pipeWidth, pipe.gapY);
        ctx.fillRect(pipe.x, pipe.gapY + pipeGap, pipeWidth,
                     canvas.height - pipe.gapY - pipeGap);
    }});

    ctx.save();
    const rotation = Math.min(Math.max(bird.velocity * 3, -45), 45);
    ctx.translate(bird.x + bird.width/2, bird.y + bird.height/2);
    ctx.rotate(rotation * Math.PI / 180);

    if (bird.imageLoaded) {{
        ctx.drawImage(bird.image,
            -bird.width/2,
            -bird.height/2,
            bird.width,
            bird.height);
    }} else {{
        ctx.beginPath();
        ctx.arc(0, 0, bird.width/2, 0, Math.PI * 2);
        ctx.fillStyle = '#FFD700';
        ctx.fill();
    }}

    ctx.restore();

    ctx.fillStyle = '#8B4513';
    ctx.fillRect(0, canvas.height - 20, canvas.width, 20);
}}

function endGame() {{
    gameOver = true;
    gameStarted = false;
    document.getElementById('gameOverText').style.display = 'block';
    document.getElementById('restartButton').style.display = 'inline-block';
}}

function gameLoop() {{
    if (!gameOver && gameStarted) {{
        updateBird();
        updatePipes();
        draw();
        requestAnimationFrame(gameLoop);
    }}
}}

draw();

</script>
</body>
</html>
"""

components.html(game_html, height=1000, scrolling=False)

st.markdown("""
<div style="text-align:center; color:white; margin-top:10px;">
Made with ❤️ | Flappy Ege © 2026
</div>
""", unsafe_allow_html=True)
