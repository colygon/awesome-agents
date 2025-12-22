import streamlit as st
import requests
import pandas as pd
import os
from crew import recommend_emojis, analyze_emoji, analyze_sentiment, find_alternatives

# Original emoji fetching functionality
@st.cache_data(ttl=60 * 60 * 12)
def fetch_emojis():
    resp = requests.get(
        "https://raw.githubusercontent.com/muan/emojilib/refs/tags/v2.4.0/emojis.json"
    )
    json = resp.json()
    codes, _ = zip(*json.items())

    return pd.DataFrame(
        {
            "Emojis": [f":{code}:" for code in ["streamlit", *codes]],
            "Shortcodes": [f"`:{code}:`" for code in ["streamlit", *codes]],
        }
    )


"""
# Streamlit emoji shortcodes with CrewAI

Below are all the emoji shortcodes supported by Streamlit, now enhanced with AI-powered emoji analysis and recommendations!

Shortcodes are a way to enter emojis using pure ASCII. So you can type this `:smile:` to show this
:smile:.

We recommend to use emojis directly as Unicode characters in your Python strings instead of shortcodes.
You can find and copy-paste Unicode emojis from [here](https://getemoji.com).
"""

st.info(
    """
The list of supported shortcodes was updated in Streamlit 1.46.0.
This also broke a few shortcodes which are no longer supported. More
information can be found in [this Github issue](https://github.com/streamlit/streamlit/issues/11845).
    """
)

# Check for API key
has_api_key = bool(os.getenv("OPENAI_API_KEY"))

if not has_api_key:
    st.warning(
        "⚠️ OPENAI_API_KEY not set. CrewAI features are disabled. "
        "Set your API key to enable AI-powered emoji analysis!"
    )

# CrewAI Features Section
st.markdown("---")
st.header("🤖 AI-Powered Emoji Features")

if has_api_key:
    tab1, tab2, tab3, tab4 = st.tabs([
        "💡 Get Recommendations",
        "🔍 Analyze Emoji",
        "❤️ Sentiment Analysis",
        "🔄 Find Alternatives"
    ])

    with tab1:
        st.subheader("Get Emoji Recommendations")
        text_input = st.text_area(
            "Enter your text:",
            placeholder="e.g., I'm so excited about the new project launch!",
            help="Get AI-powered emoji recommendations for your text"
        )
        tone = st.selectbox(
            "Select tone:",
            ["neutral", "happy", "professional", "casual", "excited", "sad", "formal"]
        )

        if st.button("Get Recommendations", key="recommend"):
            if text_input:
                with st.spinner("Analyzing your text and generating recommendations..."):
                    try:
                        result = recommend_emojis(text_input, tone)
                        st.success("Recommendations ready!")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text first.")

    with tab2:
        st.subheader("Analyze an Emoji")
        emoji_to_analyze = st.text_input(
            "Enter an emoji or shortcode:",
            placeholder="e.g., 😊 or :smile:",
            help="Get detailed analysis of an emoji's meaning and usage"
        )

        if st.button("Analyze", key="analyze"):
            if emoji_to_analyze:
                with st.spinner("Analyzing emoji..."):
                    try:
                        result = analyze_emoji(emoji_to_analyze)
                        st.success("Analysis complete!")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter an emoji or shortcode.")

    with tab3:
        st.subheader("Sentiment Analysis")
        text_with_emojis = st.text_area(
            "Enter text with emojis:",
            placeholder="e.g., Great job everyone! 🎉 Really proud of the team 💪",
            help="Analyze the sentiment and emotional tone"
        )

        if st.button("Analyze Sentiment", key="sentiment"):
            if text_with_emojis:
                with st.spinner("Analyzing sentiment..."):
                    try:
                        result = analyze_sentiment(text_with_emojis)
                        st.success("Analysis complete!")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter some text with emojis.")

    with tab4:
        st.subheader("Find Alternative Emojis")
        emoji_for_alt = st.text_input(
            "Enter an emoji:",
            placeholder="e.g., 😊",
            help="Find similar or alternative emojis",
            key="alt_emoji"
        )
        context_alt = st.text_input(
            "Context (optional):",
            placeholder="e.g., professional email",
            help="Provide context for better alternatives"
        )

        if st.button("Find Alternatives", key="alternatives"):
            if emoji_for_alt:
                with st.spinner("Finding alternatives..."):
                    try:
                        result = find_alternatives(emoji_for_alt, context_alt)
                        st.success("Alternatives found!")
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter an emoji.")

else:
    st.info(
        "Set your OPENAI_API_KEY environment variable to unlock AI-powered features:\n"
        "- Get personalized emoji recommendations\n"
        "- Analyze emoji meanings and contexts\n"
        "- Understand sentiment in emoji-enhanced text\n"
        "- Discover alternative emojis"
    )

# Original emoji table
st.markdown("---")
st.header("📋 All Supported Emoji Shortcodes")

emojis = fetch_emojis()
st.table(emojis)

# Footer
st.markdown("---")
st.markdown(
    "*Enhanced with CrewAI multi-agent system for intelligent emoji analysis and recommendations.*"
)
