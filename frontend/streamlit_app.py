import streamlit as st
import requests
import os
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Lecture Notes",
    page_icon="📚",
    layout="wide"
)

# ---------------- COLOR PALETTE ----------------
# Deep Blue Gradient Palette
GRADIENT_BG = "linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0891B2 100%)"
SIDEBAR_BLUE = "rgba(15, 23, 42, 0.8)"
CARD_BLUE = "rgba(255, 255, 255, 0.07)"
ACCENT_CYAN = "#22D3EE"
TEXT_WHITE = "#F8FAFC"

# ---------------- CSS ENGINE (Gradient & Glass) ----------------
st.markdown(f"""
<style>
    /* Global App Background Gradient */
    .stApp {{
        background: {GRADIENT_BG} !important;
        background-attachment: fixed;
        color: {TEXT_WHITE};
    }}

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {{
        background: {SIDEBAR_BLUE} !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }}

    /* Title & Text visibility */
    h1, h2, h3, p, label, span {{
        color: {TEXT_WHITE} !important;
        font-family: 'Inter', sans-serif;
    }}

    /* Tabs Styling */
    .stTabs [data-baseweb="tab"] {{
        color: rgba(255,255,255,0.6) !important;
    }}
    .stTabs [aria-selected="true"] {{
        color: {ACCENT_CYAN} !important;
        border-bottom-color: {ACCENT_CYAN} !important;
    }}

    /* Transparent Input Boxes */
    .stTextArea textarea {{
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
        backdrop-filter: blur(5px);
    }}

    /* Main Action Button (Glow Effect) */
    .stButton > button {{
        background: linear-gradient(90deg, #0891B2, #22D3EE);
        color: white !important;
        border: none !important;
        font-weight: 700;
        width: 100%;
        padding: 12px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0 4px 15px rgba(8, 145, 178, 0.3);
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(34, 211, 238, 0.5);
    }}

    /* Glass Cards for Results */
    .glass-card {{
        background: {CARD_BLUE};
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 25px;
        margin-top: 20px;
    }}
    
    /* Horizontal Slider Visibility */
    .stSelectSlider span {{
        color: {TEXT_WHITE} !important;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (HISTORY) ----------------
with st.sidebar:
    st.markdown(f"<h2 style='color:{ACCENT_CYAN} !important;'>Recents ></h2>", unsafe_allow_html=True)
    st.markdown("<p style='opacity:0.6;'>Previous Sessions</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    history_path = "backend/data/history.json"
    if os.path.exists(history_path):
        try:
            with open(history_path, "r") as f:
                history = json.load(f)
                for item in reversed(history[-10:]):
                    st.markdown(f"🔹 {item['summary'][:35]}...")
        except:
            st.markdown("Error loading history")
    else:
        st.markdown("<p style='font-style:italic;'>No history found</p>", unsafe_allow_html=True)

# ---------------- MAIN UI ----------------
st.markdown(f"<h1 style='text-align:center;'>📚 AI Lecture <span style='color:{ACCENT_CYAN};'>Navigator</span></h1>", unsafe_allow_html=True)

# Centering the Workspace
_, workspace_col, _ = st.columns([0.2, 1, 0.2])

with workspace_col:
    # 1. Action Tabs (Based on Sketch)
    tabs = st.tabs(["📄 Upload Document", "🎙️ Audio Lecture", "📂 Load Samples"])
    
    with tabs[0]:
        t_file = st.file_uploader("Select .txt file", type=["txt"])
        if t_file:
            st.session_state.text_area = t_file.read().decode("utf-8")

    with tabs[1]:
        a_file = st.file_uploader("Select audio file", type=["mp3", "wav"])

    with tabs[2]:
        if st.button("📂 Load AI Ethics Sample"):
            st.session_state.text_area = "AI Ethics is a system of moral principles and techniques intended to inform the development and responsible use of artificial intelligence technology. As AI becomes more integrated into society, issues such as bias, transparency, and accountability become critical."

    # 2. Depth Slider
    mode = st.select_slider("Summary Depth Level", options=["Short", "Detailed", "Bullet Points"])

    # 3. Main Text Input
    text_val = st.text_area(
        "Type or paste lecture content",
        value=st.session_state.get("text_area", ""),
        height=280,
        placeholder="Paste your transcript here for analysis..."
    )

    # 4. Generate Button
    if st.button("✨ GENERATE SUMMARY"):
        if a_file:
            with st.spinner("AI Transcribing..."):
                resp = requests.post("http://127.0.0.1:8000/audio-to-notes", files={"file": a_file}, params={"mode": mode})
                if resp.status_code == 200:
                    st.session_state.res = resp.json()
                    st.session_state.is_audio = True
        elif text_val:
            with st.spinner("Generating Summary..."):
                resp = requests.post("http://127.0.0.1:8000/summarize", json={"text": text_val, "mode": mode})
                if resp.status_code == 200:
                    st.session_state.res = resp.json()
                    st.session_state.is_audio = False
        else:
            st.error("Please provide text or audio.")

    # 5. Output Section
    if "res" in st.session_state:
        result = st.session_state.res
        
        if st.session_state.get("is_audio"):
            st.markdown("### 📝 Transcript")
            st.info(result['transcript'])

        st.markdown(f"""
            <div class="glass-card">
                <h3 style="color:{ACCENT_CYAN} !important; margin-top:0;">📌 Generated Notes</h3>
                <p style="font-size:16px; line-height:1.7; color:#E2E8F0;">{result['summary']}</p>
                <div style="margin-top:20px; padding-top:15px; border-top:1px solid rgba(255,255,255,0.1);">
                    <span style="background:#0891B2; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:bold;">
                        SENTIMENT: {result['sentiment']['label']} ({result['sentiment']['score']})
                    </span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.download_button("⬇️ Export to TXT", result['summary'], file_name="lecture_notes.txt")

# Footer
st.markdown("<br><p style='text-align:center; opacity:0.5; font-size:12px;'>Lecture-to-Notes Pro v3.0 | 2026 Edition</p>", unsafe_allow_html=True)