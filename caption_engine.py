import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Model
model = genai.GenerativeModel('gemini-2.5-flash') # Or 'gemini-2.0-flash' if available to you

def analyze_media(media_file, mime_type):
    """
    Handles both Images and Videos for caption generation.
    Returns JSON string.
    """
    prompt = """
    You are an expert Social Media Manager. Analyze this media.
    Generate social media content for three platforms.
    Return the output strictly as a JSON object with keys: 'linkedin', 'instagram', 'twitter'.
    
    Format:
    {
      "linkedin": "Professional post text...",
      "instagram": "Visual post text with hashtags...",
      "twitter": "Short punchy text..."
    }
    """

    try:
        if "video" in mime_type:
            # 1. Upload Video to Gemini File API
            print("Uploading video...")
            video_file = genai.upload_file(path=media_file)
            
            # 2. Wait for processing (Crucial step for videos)
            while video_file.state.name == "PROCESSING":
                time.sleep(2)
                video_file = genai.get_file(video_file.name)
                
            if video_file.state.name == "FAILED":
                return "Error: Video processing failed."

            # 3. Generate Content
            response = model.generate_content([video_file, prompt])
            
            # 4. Clean up (Optional: delete file from cloud to save space)
            # genai.delete_file(video_file.name)
            
            return response.text
        else:
            # Handle Image (Pass the PIL object directly)
            response = model.generate_content([prompt, media_file])
            return response.text

    except Exception as e:
        return f"Error: {e}"

def analyze_competitor(user_image, competitor_image):
    """
    Compares two images and predicts viral potential.
    Returns Markdown text.
    """
    prompt = """
    Act as a Senior Social Media Strategist and Visual Brand Consultant.
    
    Analyze Image A (User) and Image B (Competitor).
    
    Provide a strategic comparison report:
    
    1. 🏆 **Viral Prediction**: Which image is more likely to "stop the scroll" and grab traffic? Declare a winner and explain WHY based on visual psychology (contrast, curiosity, human element, saturation).
    2. 📊 **The Gap Analysis**: Compare the two images on Lighting, Composition, and Storytelling. Where does Image A fall short compared to Image B?
    3. 🛠️ **Action Plan**: List 3 specific, actionable edits to make Image A perform like a viral hit (e.g., "Increase contrast by 10%", "Crop to rule of thirds").
    4. 🏷️ **Winning Keywords**: Suggest 5 high-traffic keywords/hashtags that the winning image would rank for.
    """
    
    try:
        # Pass both images to the model
        response = model.generate_content([prompt, "Image A (Mine):", user_image, "Image B (Competitor):", competitor_image])
        return response.text
    except Exception as e:
        return f"Error: {e}"

# # # 2. Ask Google: "What models can I use?"
# # print("My key has access to:")
# # for m in genai.list_models():
# #     # Only show models that generate content (chat/vision models)
# #     if 'generateContent' in m.supported_generation_methods:
# #         print(f"- {m.name}")
# My key has access to:
# - models/gemini-2.5-flash
# - models/gemini-2.5-pro
# - models/gemini-2.0-flash-exp
# - models/gemini-2.0-flash
# - models/gemini-2.0-flash-001
# - models/gemini-2.0-flash-exp-image-generation
# - models/gemini-2.0-flash-lite-001
# - models/gemini-2.0-flash-lite
# - models/gemini-2.0-flash-lite-preview-02-05
# - models/gemini-2.0-flash-lite-preview
# - models/gemini-2.0-pro-exp
# - models/gemini-2.0-pro-exp-02-05
# - models/gemini-exp-1206
# - models/gemini-2.5-flash-preview-tts
# - models/gemini-2.5-pro-preview-tts
# - models/gemma-3-1b-it
# - models/gemma-3-4b-it
# - models/gemma-3-12b-it
# - models/gemma-3-27b-it
# - models/gemma-3n-e4b-it
# - models/gemma-3n-e2b-it
# - models/gemini-flash-latest
# - models/gemini-flash-lite-latest
# - models/gemini-pro-latest
# - models/gemini-2.5-flash-lite
# - models/gemini-2.5-flash-image-preview
# - models/gemini-2.5-flash-image
# - models/gemini-2.5-flash-preview-09-2025
# - models/gemini-2.5-flash-lite-preview-09-2025
# - models/gemini-3-pro-preview
# - models/gemini-3-pro-image-preview
# - models/nano-banana-pro-preview
# - models/gemini-robotics-er-1.5-preview
# - models/gemini-2.5-computer-use-preview-10-2025