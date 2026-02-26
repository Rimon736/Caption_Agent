#!/bin/bash
# Quick deployment setup script

echo "🚀 Caption Generator Deployment Setup"
echo "======================================"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Please install Git first."
    exit 1
fi

echo "✅ Git found"

# Initialize git repo if needed
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    git branch -M main
fi

# Create .env if not exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Edit .env and add your GOOGLE_API_KEY"
fi

# Stage files
echo "📤 Staging files (excluding .env)..."
git add -A
git reset .env

# Show status
echo ""
echo "📊 Repository Status:"
git status

echo ""
echo "📋 Next Steps:"
echo "1. Edit .env with your GOOGLE_API_KEY"
echo "2. Commit changes: git commit -m 'Initial commit'"
echo "3. Add remote: git remote add origin https://github.com/USERNAME/caption-generator.git"
echo "4. Push: git push -u origin main"
echo "5. Deploy on https://share.streamlit.io"
echo ""
echo "ℹ️  For detailed guide, see: DEPLOYMENT_GUIDE.md"
