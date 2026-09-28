import os
from gtts import gTTS

def generate_script(topic):
    print(f"\n==========================================")
    print(f"   GENERATING SCRIPT FOR TOPIC: {topic}")
    print(f"==========================================\n")
    
    script_text = f"Did you know this amazing fact about {topic}? Subscribe for more content!"
    print("Script Text:\n", script_text)
    return script_text

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
