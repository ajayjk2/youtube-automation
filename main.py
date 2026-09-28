import os
import google.generativeai as genai
from gtts import gTTS

# GitHub Secrets se API Key fetch kar rahe hain
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def generate_script(topic):
    print(f"\n==========================================")
    print(f"   GENERATING SCRIPT FOR TOPIC: {topic}")
    print(f"==========================================\n")
    
    if not GEMINI_API_KEY:
        print("[WARNING] GEMINI_API_KEY not found! Using fallback script.")
        return f"Did you know this amazing fact about {topic}? Subscribe for more!"

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Write a catchy 30-second YouTube Shorts script about {topic}. Keep it engaging and concise without screen directions."
        
        response = model.generate_content(prompt)
        script_text = response.text
        print("Generated Script:\n", script_text)
        return script_text
    except Exception as e:
        print(f"[ERROR] Failed to generate script with Gemini: {e}")
        return f"Did you know this amazing fact about {topic}? Subscribe for more!"

def generate_voiceover(script_text):
    print("\n--- Generating AI Voiceover ---")
    try:
        tts = gTTS(text=script_text, lang='en')
        tts.save("voiceover.mp3")
        print("[SUCCESS] Voiceover saved as 'voiceover.mp3'!")
    except Exception as e:
        print(f"[ERROR] Audio generation failed: {e}")

if __name__ == "__main__":
    video_topic = "Top 5 Space Secrets"
    script = generate_script(video_topic)
    generate_voiceover(script)
