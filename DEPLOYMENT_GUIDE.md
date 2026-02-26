# Deployment Guide for Caption Generator

## Prerequisites
- GitHub account (free)
- Google API Key (free)
- Choose a deployment platform

## Step 1: Get Your Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key" → "Create API key in new project"
3. Copy your API key and save it securely
4. ⚠️ **Never commit this key to GitHub**

## Step 2: Prepare Your Repository

1. Update `requirements.txt`:
   ```bash
   pip install -r requirements_clean.txt
   ```

2. Ensure `.env` file is in `.gitignore` (✅ Already done)

3. Create `.streamlit/secrets.toml` locally (NOT in repo):
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key"
   ```

## Step 3: Deploy to Streamlit Cloud (RECOMMENDED ⭐)

### Easiest Option - Free & Built for Streamlit

1. **Setup GitHub**
   - Create a new GitHub repository
   - Push your code (ensure `.env` is in `.gitignore`)
   
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/caption-generator.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app" → Select repository & `main.py`
   
3. **Add Secrets**
   - In app settings → "Secrets" → Add:
     ```
     GOOGLE_API_KEY = "your_actual_key"
     ```
   - Deploy! 🚀

## Step 4: Alternative Deployment Options

### Option A: Google Cloud Run (Docker)

1. Create `Dockerfile`:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements_clean.txt
   EXPOSE 8501
   CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. Create `.dockerignore` (same as `.gitignore`)

3. Deploy:
   ```bash
   gcloud auth login
   gcloud builds submit --tag gcr.io/PROJECT_ID/caption-generator
   gcloud run deploy caption-generator --image gcr.io/PROJECT_ID/caption-generator --region us-central1
   ```

### Option B: Heroku (Requires Paid Tier)

1. Create `Procfile`:
   ```
   web: streamlit run main.py --server.port=$PORT
   ```

2. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

## Configuration Changes for Production

The `.streamlit/config.toml` already includes:
- Custom theme (matching your app)
- CORS enabled
- Error details for debugging
- 200MB upload limit (for videos)

## Environment Variables (Streamlit Cloud)

Go to your app's **Settings** → **Secrets** and add:
```toml
GOOGLE_API_KEY = "your_api_key"
```

Streamlit automatically loads these into `os.getenv()`.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| API key not found | Add it to Streamlit Secrets, not `.env` |
| Video upload fails | Check file size (max 200MB) |
| Module not found | Update `requirements_clean.txt` |
| No media display | Ensure PIL/Pillow is installed |

## Important Security Notes

✅ **DO:**
- Add `.env` to `.gitignore`
- Use Streamlit Secrets for API keys
- Keep Google API key private

❌ **DON'T:**
- Commit `.env` file
- Hardcode API keys in code
- Share your secrets

## Testing Before Deployment

```bash
# Test locally
streamlit run main.py

# Check dependencies
pip install -r requirements_clean.txt

# Verify API key works
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('GOOGLE_API_KEY'))"
```

## Support & Next Steps

- Streamlit Docs: https://docs.streamlit.io
- Google Generative AI: https://ai.google.dev
- Deployment FAQs: https://share.streamlit.io/docs/deploy

---
📝 **Last Updated:** February 2026
