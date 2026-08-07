def generate_content(topic, content_type):
    print("\n🤖 AI CONTENT CREATOR")
    print("=" * 50)
    print(f"🎯 Topic: {topic}")
    print(f"📂 Category: {content_type}")
    print("=" * 50)

    if content_type == "motivation":
        hook = f"🔥 Nobody is coming to save you. Start building your life around {topic}."
        script = (
            f"Stop waiting for the perfect moment. "
            f"If you want to improve your life through {topic}, start today. "
            f"You don't need to be perfect. You just need to be consistent. "
            f"One small step every day can completely change your future."
        )
        caption = f"Your future is built by what you do today. 🔥"
        title = f"Stop Making Excuses About {topic}"
        hashtags = "#motivation #mindset #discipline #success #selfimprovement #fyp"

    elif content_type == "entertainment":
        hook = f"😂 Wait... did you know THIS about {topic}?"
        script = (
            f"Let's be honest about {topic}. "
            f"Sometimes the things we take seriously are actually hilarious. "
            f"Here's something you probably didn't expect. "
            f"Would you have guessed this? 😂"
        )
        caption = f"Tell me you didn't know this! 😂👇"
        title = f"You Won't Believe This About {topic}"
        hashtags = "#entertainment #funny #comedy #viral #trending #fyp"

    elif content_type == "lifestyle":
        hook = f"🎬 Here's how I'm upgrading my lifestyle with {topic}."
        script = (
            f"Your lifestyle is built from your daily habits. "
            f"When you improve {topic}, you can create better routines, "
            f"better experiences, and a better version of yourself. "
            f"Start with one small change today and build from there."
        )
        caption = f"Small lifestyle changes. Big results. 🎬✨"
        title = f"How to Upgrade Your Lifestyle With {topic}"
        hashtags = "#lifestyle #lifestylegoals #selfimprovement #dailyvlog #fyp"

    else:
        print("❌ Invalid category.")
        return

    print(f"\n🔥 HOOK\n{hook}")
    print(f"\n📝 SCRIPT\n{script}")
    print(f"\n💬 CAPTION\n{caption}")
    print(f"\n📌 TITLE\n{title}")
    print(f"\n#️⃣ HASHTAGS\n{hashtags}")
    print("\n✅ Content generated successfully!")


print("\n🚀 WELCOME TO AI CONTENT CREATOR")
print("\nChoose your content category:")
print("1️⃣ Motivation 🔥")
print("2️⃣ Entertainment 😂")
print("3️⃣ Lifestyle 🎬")

choice = input("\nEnter 1, 2, or 3: ")
topic = input("Enter your content topic: ")

categories = {
    "1": "motivation",
    "2": "entertainment",
    "3": "lifestyle"
}

if choice in categories:
    generate_content(topic, categories[choice])
else:
    print("❌ Please choose 1, 2, or 3.")
