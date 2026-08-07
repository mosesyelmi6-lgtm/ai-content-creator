import os
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Content Creator",
    page_icon="🤖"
)

st.title("🤖 AI Content Creator")
st.write("Create hooks, scripts, captions, titles, hashtags, and calls to action with AI.")

topic = st.text_input(
    "🎯 Content topic",
    placeholder="Example: How to stay disciplined"
)

content_type = st.selectbox(
    "📂 Content type",
    [
        "Motivation",
        "Entertainment",
        "Education",
        "Business",
        "Lifestyle",
        "Storytelling"
    ]
)

platform = st.selectbox(
    "📱 Platform",
    ["TikTok", "Instagram", "YouTube", "Facebook"]
)

if st.button("🚀 Generate Content"):
    if not topic:
        st.warning("Please enter a content topic.")
    else:
        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            st.error("OPENAI_API_KEY has not been configured.")
        else:
            try:
                client = OpenAI(api_key=api_key)

                prompt = f"""
You are an expert social media content creator.

Create original, engaging content for {platform}.

Topic: {topic}
Content type: {content_type}

Provide:

🔥 HOOK
🎬 SCRIPT
📝 CAPTION
📌 TITLE
#️⃣ 10 HASHTAGS
🚀 CALL TO ACTION

Make the content engaging, natural, and suitable for the selected platform.
"""

                with st.spinner("Generating your content..."):
                    response = client.responses.create(
                        model="gpt-5",
                        input=prompt
                    )

                st.success("Content generated!")
                st.markdown(response.output_text)

            except Exception as error:
                st.error(f"Something went wrong: {error}")
