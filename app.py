import os
from openai import OpenAI

# Get your API key securely from an environment variable
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    print("❌ OPENAI_API_KEY is not set.")
    print("Add your API key as an environment variable before running the app.")
    exit()

client = OpenAI(api_key=api_key)


def generate_content(topic, content_type):
    prompt = f"""
You are an expert social media content creator.

Create engaging content about:
Topic: {topic}
Content type: {content_type}

Return the following:

🔥 HOOK:
Create a strong attention-grabbing opening.

🎬 SCRIPT:
Write a short, engaging social-media video script.

📝 CAPTION:
Write a compelling caption.

📌 TITLE:
Create a catchy title.

#️⃣ HASHTAGS:
Give 10 relevant hashtags.

🚀 CALL TO ACTION:
Give a strong call to action.

Keep everything original, engaging, and suitable for TikTok.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


print("=" * 50)
print("🤖 AI CONTENT CREATOR")
print("=" * 50)

topic = input("\nEnter your content topic: ")
content_type = input(
    "Enter content type (motivation, entertainment, education, etc.): "
)

print("\n⏳ Generating content...\n")

try:
    content = generate_content(topic, content_type)
    print(content)

except Exception as error:
    print("\n❌ Something went wrong:")
    print(error)
