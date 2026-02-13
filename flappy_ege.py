import streamlit as st
import random
import time
import base64

# Sayfa yapılandırması
st.set_page_config(
    page_title="Flappy Ege",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ege'nin base64 resmi
EGE_IMAGE = "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"

# CSS stilleri
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0;
    }
    .stApp {
        max-width: 100%;
    }
    .game-title {
        font-size: 4em;
        font-weight: bold;
        text-align: center;
        color: white;
        text-shadow: 4px 4px 8px rgba(0,0,0,0.5);
        margin: 20px 0;
        animation: glow 2s ease-in-out infinite;
    }
    @keyframes glow {
        0%, 100% { text-shadow: 4px 4px 8px rgba(0,0,0,0.5); }
        50% { text-shadow: 0 0 20px rgba(255,255,255,0.8); }
    }
    .score-display {
        font-size: 2.5em;
        font-weight: bold;
        color: #ffd700;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin: 10px 0;
    }
    .game-over {
        font-size: 3em;
        font-weight: bold;
        color: #ff4444;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    .instructions {
        background: rgba(255,255,255,0.9);
        padding: 20px;
        border-radius: 15px;
        margin: 20px auto;
        max-width: 600px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .high-score {
        font-size: 1.5em;
        color: #ffd700;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    div[data-testid="stButton"] button {
        width: 100%;
        height: 80px;
        font-size: 2em;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border: none;
        border-radius: 15px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    div[data-testid="stButton"] button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
</style>
""", unsafe_allow_html=True)

# Oyun durumu için session state
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'bird_y' not in st.session_state:
    st.session_state.bird_y = 250
if 'bird_velocity' not in st.session_state:
    st.session_state.bird_velocity = 0
if 'pipes' not in st.session_state:
    st.session_state.pipes = []
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'high_score' not in st.session_state:
    st.session_state.high_score = 0
if 'frame_count' not in st.session_state:
    st.session_state.frame_count = 0

# Oyun sabitleri
GRAVITY = 0.6
JUMP_STRENGTH = -10
PIPE_WIDTH = 80
PIPE_GAP = 200
PIPE_SPEED = 3
BIRD_SIZE = 50

def reset_game():
    st.session_state.bird_y = 250
    st.session_state.bird_velocity = 0
    st.session_state.pipes = []
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.game_started = True
    st.session_state.frame_count = 0

def jump():
    if not st.session_state.game_over:
        st.session_state.bird_velocity = JUMP_STRENGTH

def update_game():
    if not st.session_state.game_started or st.session_state.game_over:
        return
    
    # Kuş fiziği
    st.session_state.bird_velocity += GRAVITY
    st.session_state.bird_y += st.session_state.bird_velocity
    
    # Zemin ve tavan kontrolü
    if st.session_state.bird_y < 0:
        st.session_state.bird_y = 0
        st.session_state.bird_velocity = 0
    if st.session_state.bird_y > 550 - BIRD_SIZE:
        st.session_state.game_over = True
        if st.session_state.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.score
    
    # Boru oluşturma
    st.session_state.frame_count += 1
    if st.session_state.frame_count % 90 == 0:
        gap_y = random.randint(100, 350)
        st.session_state.pipes.append({
            'x': 800,
            'gap_y': gap_y,
            'scored': False
        })
    
    # Boruları hareket ettir ve çarpışma kontrolü
    bird_x = 100
    for pipe in st.session_state.pipes[:]:
        pipe['x'] -= PIPE_SPEED
        
        # Skor
        if not pipe['scored'] and pipe['x'] + PIPE_WIDTH < bird_x:
            st.session_state.score += 1
            pipe['scored'] = True
        
        # Çarpışma kontrolü
        if (bird_x + BIRD_SIZE > pipe['x'] and 
            bird_x < pipe['x'] + PIPE_WIDTH):
            if (st.session_state.bird_y < pipe['gap_y'] or 
                st.session_state.bird_y + BIRD_SIZE > pipe['gap_y'] + PIPE_GAP):
                st.session_state.game_over = True
                if st.session_state.score > st.session_state.high_score:
                    st.session_state.high_score = st.session_state.score
        
        # Ekrandan çıkan boruları sil
        if pipe['x'] < -PIPE_WIDTH:
            st.session_state.pipes.remove(pipe)

def render_game():
    # SVG oyun alanı
    svg_parts = [
        f'<svg width="800" height="550" style="background: linear-gradient(180deg, #87CEEB 0%, #E0F6FF 100%); border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.3);">'
    ]
    
    # Borular
    for pipe in st.session_state.pipes:
        # Üst boru
        svg_parts.append(f'''
            <rect x="{pipe['x']}" y="0" width="{PIPE_WIDTH}" height="{pipe['gap_y']}" 
                  fill="#2ECC71" stroke="#27AE60" stroke-width="3" rx="5"/>
            <rect x="{pipe['x']-10}" y="{pipe['gap_y']-30}" width="{PIPE_WIDTH+20}" height="30" 
                  fill="#27AE60" stroke="#1E8449" stroke-width="3" rx="3"/>
        ''')
        # Alt boru
        svg_parts.append(f'''
            <rect x="{pipe['x']}" y="{pipe['gap_y'] + PIPE_GAP}" width="{PIPE_WIDTH}" 
                  height="{550 - pipe['gap_y'] - PIPE_GAP}" 
                  fill="#2ECC71" stroke="#27AE60" stroke-width="3" rx="5"/>
            <rect x="{pipe['x']-10}" y="{pipe['gap_y'] + PIPE_GAP}" width="{PIPE_WIDTH+20}" height="30" 
                  fill="#27AE60" stroke="#1E8449" stroke-width="3" rx="3"/>
        ''')
    
    # Ege'nin kafası (Base64 image olarak)
    rotation = st.session_state.bird_velocity * 3
    rotation = max(-45, min(45, rotation))
    svg_parts.append(f'''
        <image x="{100 - BIRD_SIZE/2}" y="{st.session_state.bird_y}" 
               width="{BIRD_SIZE}" height="{BIRD_SIZE}" 
               href="data:image/png;base64,{EGE_IMAGE}"
               transform="rotate({rotation} {100} {st.session_state.bird_y + BIRD_SIZE/2})"
               style="filter: drop-shadow(3px 3px 5px rgba(0,0,0,0.5));" />
    ''')
    
    # Zemin
    svg_parts.append('''
        <rect x="0" y="530" width="800" height="20" fill="#8B4513"/>
        <rect x="0" y="545" width="800" height="5" fill="#654321"/>
    ''')
    
    svg_parts.append('</svg>')
    
    return ''.join(svg_parts)

# Ana sayfa
st.markdown('<h1 class="game-title">🎮 FLAPPY EGE 🎮</h1>', unsafe_allow_html=True)

# Skor gösterimi
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.markdown(f'<div class="high-score">🏆 En Yüksek: {st.session_state.high_score}</div>', 
                unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="score-display">SKOR: {st.session_state.score}</div>', 
                unsafe_allow_html=True)

# Oyun ekranı
if not st.session_state.game_started:
    st.markdown("""
    <div class="instructions">
        <h2 style="text-align: center; color: #333;">🎯 Nasıl Oynanır?</h2>
        <p style="font-size: 1.2em; text-align: center;">
        ✨ <strong>ZıPLA</strong> butonuna tıklayarak Ege'yi havada tut!<br>
        🚫 Borulara çarpmamaya çalış!<br>
        🏆 Ne kadar çok boru geçersen o kadar yüksek skor!<br>
        💪 Rekorunu kır!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 OYUNA BAŞLA", key="start"):
        reset_game()
        st.rerun()
else:
    # Oyun alanı
    game_container = st.container()
    with game_container:
        if st.session_state.game_over:
            st.markdown('<div class="game-over">💀 OYUN BİTTİ! 💀</div>', 
                       unsafe_allow_html=True)
        
        st.markdown(render_game(), unsafe_allow_html=True)
    
    # Kontrol butonları
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if not st.session_state.game_over:
            if st.button("⬆️ ZIPLA", key="jump"):
                jump()
                update_game()
                st.rerun()
        else:
            if st.button("🔄 YENİDEN BAŞLA", key="restart"):
                reset_game()
                st.rerun()
    
    # Otomatik güncelleme için
    if not st.session_state.game_over:
        time.sleep(0.03)
        update_game()
        st.rerun()

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
    <p style="font-size: 1.2em;">Made with ❤️ | Flappy Ege © 2026</p>
</div>
""", unsafe_allow_html=True)
