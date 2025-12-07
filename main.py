import streamlit as st
from PIL import Image
from caption_engine import analyze_media, analyze_competitor
from keyword_tool import extract_keywords
import json
import tempfile
import os

# Page Config
st.set_page_config(page_title="AI Agent Pro", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] { gap: 10px; border-bottom: 2px solid #f0f2f6; }
    .stTabs [data-baseweb="tab"] { height: 50px; background-color: #ffffff; border-radius: 5px; color: #444; font-weight: 600; padding: 0 20px; transition: all 0.2s; }
    .stTabs [data-baseweb="tab"]:hover { background-color: #f9f9f9; color: #000; }
    .stTabs [aria-selected="true"] { background-color: #2e66ff !important; color: #FFFFFF !important; }
    div.stButton > button { width: 100%; background-color: #2e66ff; color: white; border: none; padding: 12px 20px; border-radius: 8px; font-weight: bold; }
    div.stButton > button:hover { background-color: #1a54e6; }
</style>""", unsafe_allow_html=True)

# Sidebar for Mode Selection
st.sidebar.title("🤖 Agent Settings")
mode = st.sidebar.radio("Select Mode:", ["Content Generator", "Competitor Analysis"])

st.title(f"{mode}")

# ==========================================
# MODE 1: CONTENT GENERATOR (Image & Video)
# ==========================================
if mode == "Content Generator":
    st.markdown("Upload an image or video to generate multi-platform captions.")
    
    # Update uploader to accept MP4
    uploaded_file = st.file_uploader("Upload media...", type=["jpg", "jpeg", "png", "mp4"])

    if uploaded_file is not None:
        file_type = uploaded_file.type
        
        # Display Media
        if "video" in file_type:
            st.video(uploaded_file)
        else:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button('Generate Content'):
            with st.spinner('Agent is watching/analyzing media...'):
                
                # Handling Video vs Image Logic
                if "video" in file_type:
                    # Save video to temp file (Gemini API needs a path, not bytes)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        temp_video_path = tmp_file.name
                    
                    # Call Engine with Path
                    raw_output = analyze_media(temp_video_path, "video")
                    
                    # Cleanup temp file
                    os.remove(temp_video_path)
                else:
                    # Call Engine with PIL Image
                    raw_output = analyze_media(image, "image")

                # --- PARSING JSON (Same as before) ---
                cleaned_output = raw_output.replace("```json", "").replace("```", "").strip()
                try:
                    content_data = json.loads(cleaned_output)
                    linkedin_text = content_data.get("linkedin", "N/A")
                    instagram_text = content_data.get("instagram", "N/A")
                    twitter_text = content_data.get("twitter", "N/A")
                    keywords = extract_keywords(linkedin_text)

                    st.write("---")
                    st.subheader("🚀 Generated Content")
                    tab1, tab2, tab3 = st.tabs(["💼 LinkedIn", "📸 Instagram", "🐦 Twitter/X"])

                    with tab1: st.text_area("LinkedIn:", value=linkedin_text, height=250)
                    with tab2: st.text_area("Instagram:", value=instagram_text, height=250)
                    with tab3: st.text_area("Twitter:", value=twitter_text, height=150)

                    st.subheader("🏷️ Keywords")
                    st.write(", ".join(keywords))

                except Exception as e:
                    st.error("Error parsing response.")
                    st.write(raw_output)

# ==========================================
# MODE 2: COMPETITOR ANALYSIS
# ==========================================
elif mode == "Competitor Analysis":
    st.markdown("Compare your image with a viral competitor post to get strategic advice.")
    
    col1, col2 = st.columns(2)
    with col1:
        my_file = st.file_uploader("Your Image", type=["jpg", "png"], key="img1")
        if my_file: st.image(my_file, use_column_width=True)
            
    with col2:
        comp_file = st.file_uploader("Competitor Image", type=["jpg", "png"], key="img2")
        if comp_file: st.image(comp_file, use_column_width=True)

    if my_file and comp_file:
        if st.button("Analyze & Compare"):
            with st.spinner("Agent is comparing visuals..."):
                img1 = Image.open(my_file)
                img2 = Image.open(comp_file)
                
                # Call Comparison Engine
                analysis = analyze_competitor(img1, img2)
                
                st.write("---")
                st.subheader("💡 Strategic Analysis")
                st.markdown(analysis)