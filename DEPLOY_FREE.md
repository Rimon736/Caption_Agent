# 🚀 Deploy FREE to Streamlit Cloud (5 minutes)

## Step 1: Get Your Free Google API Key (2 min)

1. Go to: https://makersuite.google.com/app/apikey
2. Click **"Create API Key"** → **"Create API key in new project"**
3. Copy the key and save it somewhere safe
4. ✅ Keep this key secret - don't share it!

---

## Step 2: Create GitHub Repository (2 min)

1. Go to: https://github.com/new
2. Create a new repository:
   - **Name:** `caption-generator` (or any name you like)
   - **Description:** "AI-powered social media caption generator"
   - **Public** (Streamlit Cloud requires public repo for free tier)
   - Click **"Create repository"**

3. In your project folder, run:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/caption-generator.git
   git push -u origin main
   ```

---

## Step 3: Deploy on Streamlit Cloud (1 min) ⭐

1. Go to: https://share.streamlit.io
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in:
   - **Repository:** `YOUR_USERNAME/caption-generator`
   - **Branch:** `main`
   - **Main file path:** `main.py`
5. Click **"Deploy!"** button

Streamlit will automatically deploy! Wait 2-3 minutes... ⏳

---

## Step 4: Add Your API Key (30 sec) 🔑

While it's deploying:

1. In your app dashboard, click **"⚙️ Settings"** (top right)
2. Go to **"Secrets"** tab
3. Paste this in:
   ```
   GOOGLE_API_KEY = "your_api_key_here"
   ```
   (Replace with your actual API key from Step 1)
4. Click **"Save"**
5. Streamlit automatically restarts with your secret ✅

---

## Done! 🎉

Your app is now live at:
```
https://YOUR_USERNAME-caption-generator.streamlit.app
```

### Share it with friends! 🌐
- Copy the URL from your app
- Works on any device (mobile, tablet, desktop)
- No installation needed

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | Files pushed to GitHub? Check `main.py` exists |
| "API key error" | Added to **Secrets**, not `.env`? |
| App won't deploy | Check if repo is **PUBLIC** |
| Deployment stuck? | Refresh page, wait 5 minutes |

---

## Keep Your App Updated

After making changes:
```powershell
git add .
git commit -m "Update features"
git push
```

Streamlit automatically redeploys! 🚀

---

## Important Notes

✅ **DO:**
- Keep your Google API key secret (already done - it's in Secrets)
- Push code to GitHub
- Use `requirements_clean.txt`

❌ **DON'T:**
- Commit `.env` file to GitHub
- Hardcode your API key in code
- Share your Secrets with anyone

---

**Your app is now live on the internet!** 🌍

Upload a photo or video and generate captions from anywhere in the world.

Need help? Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for more platforms.
