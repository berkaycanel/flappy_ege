import streamlit as st
import streamlit.components.v1 as components

# Sayfa yapılandırması
st.set_page_config(
    page_title="Flappy Ege",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# HTML ve JavaScript ile tam oyun
game_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: Arial, sans-serif;
        }
        #gameContainer {
            text-align: center;
        }
        canvas {
            border: 5px solid white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            display: block;
            margin: 20px auto;
            background: linear-gradient(180deg, #87CEEB 0%, #E0F6FF 100%);
        }
        #score {
            font-size: 3em;
            color: white;
            font-weight: bold;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            margin: 20px 0;
        }
        #highScore {
            font-size: 1.5em;
            color: #ffd700;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        #instructions {
            color: white;
            font-size: 1.3em;
            margin: 20px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .gameOver {
            color: #ff4444;
            font-size: 4em;
            font-weight: bold;
            text-shadow: 4px 4px 8px rgba(0,0,0,0.7);
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }
        button {
            font-size: 1.5em;
            padding: 15px 40px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            margin: 10px;
        }
        button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        }
    </style>
</head>
<body>
    <div id="gameContainer">
        <div id="highScore">🏆 En Yüksek: <span id="highScoreValue">0</span></div>
        <div id="score">SKOR: <span id="scoreValue">0</span></div>
        <div id="gameOverText" style="display:none;" class="gameOver">💀 OYUN BİTTİ! 💀</div>
        <canvas id="gameCanvas" width="800" height="600"></canvas>
        <div id="instructions">
            ⬆️ SPACE, YUKARI OK veya TIKLA - Zıpla<br>
            🎮 Yeşil borulardan geç!
        </div>
        <button id="startButton" onclick="startGame()">🚀 OYUNA BAŞLA</button>
        <button id="restartButton" onclick="restartGame()" style="display:none;">🔄 YENİDEN BAŞLA</button>
    </div>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        // Oyun değişkenleri
        let gameStarted = false;
        let gameOver = false;
        let score = 0;
        let highScore = localStorage.getItem('flappyEgeHighScore') || 0;
        document.getElementById('highScoreValue').textContent = highScore;
        
        // Kuş
        const bird = {
            x: 100,
            y: 250,
            width: 50,
            height: 50,
            velocity: 0,
            gravity: 0.6,
            jump: -12,
            image: new Image()
        };
        
        // Ege'nin resmini yükle
        bird.image.src = 'IMG_3869.jpg';
        
        // Borular
        let pipes = [];
        const pipeWidth = 80;
        const pipeGap = 200;
        const pipeSpeed = 3;
        let frameCount = 0;
        
        // Kontroller
        document.addEventListener('keydown', (e) => {
            if ((e.code === 'Space' || e.code === 'ArrowUp') && gameStarted && !gameOver) {
                jump();
            }
        });
        
        canvas.addEventListener('click', () => {
            if (gameStarted && !gameOver) {
                jump();
            }
        });
        
        function jump() {
            bird.velocity = bird.jump;
        }
        
        function startGame() {
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
        }
        
        function restartGame() {
            startGame();
        }
        
        function createPipe() {
            const gapY = Math.random() * (canvas.height - pipeGap - 200) + 100;
            pipes.push({
                x: canvas.width,
                gapY: gapY,
                scored: false
            });
        }
        
        function updateBird() {
            bird.velocity += bird.gravity;
            bird.y += bird.velocity;
            
            // Zemin ve tavan kontrolü
            if (bird.y < 0) {
                bird.y = 0;
                bird.velocity = 0;
            }
            if (bird.y + bird.height > canvas.height - 20) {
                endGame();
            }
        }
        
        function updatePipes() {
            // Yeni boru oluştur
            frameCount++;
            if (frameCount % 90 === 0) {
                createPipe();
            }
            
            // Boruları hareket ettir
            for (let i = pipes.length - 1; i >= 0; i--) {
                pipes[i].x -= pipeSpeed;
                
                // Skor
                if (!pipes[i].scored && pipes[i].x + pipeWidth < bird.x) {
                    score++;
                    pipes[i].scored = true;
                    document.getElementById('scoreValue').textContent = score;
                    
                    if (score > highScore) {
                        highScore = score;
                        localStorage.setItem('flappyEgeHighScore', highScore);
                        document.getElementById('highScoreValue').textContent = highScore;
                    }
                }
                
                // Çarpışma kontrolü
                if (bird.x + bird.width > pipes[i].x && 
                    bird.x < pipes[i].x + pipeWidth) {
                    if (bird.y < pipes[i].gapY || 
                        bird.y + bird.height > pipes[i].gapY + pipeGap) {
                        endGame();
                    }
                }
                
                // Ekrandan çıkan boruları sil
                if (pipes[i].x + pipeWidth < 0) {
                    pipes.splice(i, 1);
                }
            }
        }
        
        function draw() {
            // Temizle
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Borular
            pipes.forEach(pipe => {
                // Üst boru
                ctx.fillStyle = '#2ECC71';
                ctx.fillRect(pipe.x, 0, pipeWidth, pipe.gapY);
                ctx.strokeStyle = '#27AE60';
                ctx.lineWidth = 3;
                ctx.strokeRect(pipe.x, 0, pipeWidth, pipe.gapY);
                
                // Üst boru başlığı
                ctx.fillStyle = '#27AE60';
                ctx.fillRect(pipe.x - 10, pipe.gapY - 30, pipeWidth + 20, 30);
                ctx.strokeRect(pipe.x - 10, pipe.gapY - 30, pipeWidth + 20, 30);
                
                // Alt boru
                ctx.fillStyle = '#2ECC71';
                ctx.fillRect(pipe.x, pipe.gapY + pipeGap, pipeWidth, canvas.height - pipe.gapY - pipeGap);
                ctx.strokeRect(pipe.x, pipe.gapY + pipeGap, pipeWidth, canvas.height - pipe.gapY - pipeGap);
                
                // Alt boru başlığı
                ctx.fillStyle = '#27AE60';
                ctx.fillRect(pipe.x - 10, pipe.gapY + pipeGap, pipeWidth + 20, 30);
                ctx.strokeRect(pipe.x - 10, pipe.gapY + pipeGap, pipeWidth + 20, 30);
            });
            
            // Kuş (Ege)
            ctx.save();
            const rotation = Math.min(Math.max(bird.velocity * 3, -45), 45);
            ctx.translate(bird.x + bird.width/2, bird.y + bird.height/2);
            ctx.rotate(rotation * Math.PI / 180);
            ctx.drawImage(bird.image, -bird.width/2, -bird.height/2, bird.width, bird.height);
            ctx.restore();
            
            // Zemin
            ctx.fillStyle = '#8B4513';
            ctx.fillRect(0, canvas.height - 20, canvas.width, 20);
            ctx.fillStyle = '#654321';
            ctx.fillRect(0, canvas.height - 5, canvas.width, 5);
        }
        
        function endGame() {
            gameOver = true;
            gameStarted = false;
            document.getElementById('gameOverText').style.display = 'block';
            document.getElementById('restartButton').style.display = 'inline-block';
        }
        
        function gameLoop() {
            if (!gameOver && gameStarted) {
                updateBird();
                updatePipes();
                draw();
                requestAnimationFrame(gameLoop);
            }
        }
        
        // İlk çizim
        draw();
    </script>
</body>
</html>
"""

# Oyunu göster
components.html(game_html, height=900, scrolling=False)

st.markdown("""
<div style="text-align: center; margin-top: 20px; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
    <p style="font-size: 1.2em;">Made with ❤️ | Flappy Ege © 2026</p>
</div>
""", unsafe_allow_html=True)
