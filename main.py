import os

def generate_script(topic):
    print(f"--- Generating Script for Topic: {topic} ---")
    
    # Yahan AI Script generation logic aayega
    script_prompt = f"""
    Create a 2-minute YouTube Shorts script on the topic: {topic}.
    Include:
    1. Attention-grabbing Hook (0-5s)
    2. Main Points
    3. Call to Action (Subscribe)
    """
    
    print("\n[SUCCESS] Script outline created successfully!")
    return script_prompt

if __name__ == "__main__":
    video_topic = "Top 5 Space Secrets"
    script = generate_script(video_topic)
