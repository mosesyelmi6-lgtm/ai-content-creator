import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_content(topic, content_type):
    prompt = f"""
Create engaging social media content about: {topic}

Content type: {content_type}

Give me:
1. A viral hook
2. A short script
3. A caption
4. A title
5. 10 relevant hashtags
6. A call to action

Make the content engaging, clear, and suitable for TikTok.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


print("🤖 AI CONTENT CREATOR")
print("=" * 40)

topic = input("Enter your content topic: ")
content_type = input("Enter content type (motivation, entertainment, education, etc.): ")

print("\n⏳ Generating your content...\n")

try:
    result = generate_content(topic, content_type)
    print(result)
except Exception as error:
    print("❌ Error:", error)
