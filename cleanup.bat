@echo off
cd /d "e:\Sem4_1\AI_Lab\Caption_Generator_Project"
del requirement.txt requirements_clean.txt
git add -A
git commit -m "Fix: Use clean requirements.txt for Streamlit Cloud"
git push
echo Done!
pause
