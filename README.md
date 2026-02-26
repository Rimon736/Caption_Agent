# 🎬 Caption Generator - AI Agent Pro

A Streamlit web app that uses Google's Gemini AI to generate multi-platform social media captions from images and videos.

## Features

✨ **Multi-Platform Captions**
- LinkedIn (professional)
- Instagram (visual with hashtags)
- Twitter (short & punchy)

📹 **Media Support**
- Images (JPG, PNG, JPEG)
- Videos (MP4)

🤖 **AI-Powered Analysis**
- Google Gemini 2.5 Flash API
- Competitor analysis
- Keyword extraction

## 🚀 Quick Start

### Local Development

1. **Clone repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/caption-generator.git
   cd caption-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements_clean.txt
   ```

3. **Set environment variable**
   ```bash
   # Create .env file
   echo GOOGLE_API_KEY=your_api_key_here > .env
   ```

   Get your free API key: https://makersuite.google.com/app/apikey

4. **Run locally**
   ```bash
   streamlit run main.py
   ```

   Opens automatically at `http://localhost:8501`

## 🌐 Deploy Online

### Option 1: Streamlit Cloud (Recommended) ⭐
**Easiest - Free - Zero config**

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Add `GOOGLE_API_KEY` in app secrets
5. Done! 🚀

**Full guide:** See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

### Option 2: Google Cloud Run
**More scalable - Requires Docker**

See Docker setup in [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

### Option 3: Other Platforms
- Heroku, AWS, Azure, Render, Railway
- See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for details

## 📁 Project Structure

```
caption-generator/
├── main.py                    # Streamlit UI
├── caption_engine.py          # Gemini API integration
├── keyword_tool.py            # YAKE keyword extractor
├── requirements_clean.txt     # Dependencies (use this for deploy)
├── .env.example               # Example env variables
├── .gitignore                 # Git ignore patterns
├── .streamlit/
│   └── config.toml            # Streamlit config
└── DEPLOYMENT_GUIDE.md        # Full deployment guide
```

## 🔧 Configuration

### Streamlit Config
Edit `.streamlit/config.toml` for:
- Theme customization
- Server settings
- Upload limits

### API Selection
In `caption_engine.py`, switch models:
```python
model = genai.GenerativeModel('gemini-2.5-flash')
# or
model = genai.GenerativeModel('gemini-2.0-flash')
```

## 📊 Modes

### Mode 1: Content Generator
- Upload media (image/video)
- Get instant captions for 3 platforms
- Extract keywords

### Mode 2: Competitor Analysis
- Analyze competitor content
- Get insights & recommendations

## 🔐 Security

- Never commit `.env` file
- Use Streamlit Secrets for production
- API keys stored server-side only
- Videos processed but not stored

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.40.0 | Web framework |
| google-generativeai | 0.7.1 | Gemini API |
| Pillow | 10.2.0 | Image processing |
| yake | 0.4.8 | Keyword extraction |
| python-dotenv | 1.0.1 | .env management |

## 🆘 Troubleshooting

**Video won't upload?**
- Max size: 200MB (check config.toml)
- Format: MP4 recommended
- Wait for processing to complete

**API key error?**
- Verify key is valid at: https://makersuite.google.com/app/apikey
- For Streamlit Cloud: Add to app Secrets, not .env

**Module not found?**
- `pip install -r requirements_clean.txt`
- Restart kernel if using notebook

## 📚 Resources

- [Streamlit Docs](https://docs.streamlit.io)
- [Google Generative AI](https://ai.google.dev)
- [Streamlit Cloud Deploy](https://share.streamlit.io/docs)

## 📝 License

This project is open source and available under the MIT License.

---

**Ready to deploy?** → Follow [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
