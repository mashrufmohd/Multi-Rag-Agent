import streamlit as st
from agents import AgentManager
import os
from loguru import logger

# Add custom styles to enhance UI
def add_styles():
    st.markdown("""
    <style>
    body {
        background-image: linear-gradient(90deg, #020024 0%, #090979 35%, #00d4ff 100%);
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: rgba(0, 0, 0, 0.7);
    }
    .stButton>button {
        background-color: #ff007f !important;
        color: white !important;
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        border: none;
    }
    .stTextArea>textarea, .stTextInput>input {
        background-color: rgba(255, 255, 255, 0.8);
        color: black;
    }
    h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Main function to run the application
def main():
    st.set_page_config(page_title="Multi-Agent AI System", layout="wide")
    add_styles()

    # Fetch API Key from Streamlit secrets
    api_key = st.secrets.get("GEMINI_API_KEY", None)
    if not api_key:
        st.error("GEMINI API Key is missing! Please configure it in Streamlit secrets.")
        return

    # Project Explanation
    st.markdown("""
    # Multi-Agent AI System with Gemini 🤖✨

    This project features a **multi-agent AI system** designed to perform tasks such as:
    - **Text Summarization** ✍️
    - **Research Article Writing & Refinement** 📝
    - **Data Sanitization** 🛡️

    Powered by **Gemini**, it enhances productivity and automates complex AI workflows.
    """)

    # Social Media Links
    st.markdown("""
    ## Connect with Project Maintainers 🤝:
    - [LinkedIn - Hitesh Kumar](https://www.linkedin.com/in/hitesh-kumar-aiml/) 🔗
    - [GitHub - Hitesh Kumar](https://github.com/Hiteshydv001) 🔗
    - [LinkedIn - Mohd Mashruf](https://www.linkedin.com/in/mohd-mashruf/) 🔗
    - [GitHub - Mohd Mashruf](https://github.com/mashrufmohd) 🔗
    """)

    # Sidebar Task Selection
    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox("Choose a task:", [
        "Summarize Text 📚",
        "Write and Refine Research Article 🖋️",
        "Sanitize Data 🔒"
    ])

    # Initialize AgentManager
    try:
        agent_manager = AgentManager(max_retries=2, verbose=True)
    except Exception as e:
        st.error(f"Error initializing AgentManager: {e}")
        logger.error(f"AgentManager Initialization Error: {e}")
        return

    # Route to respective sections
    if task == "Summarize Text 📚":
        summarize_section(agent_manager)
    elif task == "Write and Refine Research Article 🖋️":
        write_and_refine_article_section(agent_manager)
    elif task == "Sanitize Data 🔒":
        sanitize_data_section(agent_manager)

# Summarization Section
def summarize_section(agent_manager):
    st.header("Summarize Text 📚")
    text = st.text_area("Enter text to summarize:", height=200)
    
    if st.button("Summarize"):
        if text.strip():
            try:
                summarizer = agent_manager.get_agent("summarize")
                validator = agent_manager.get_agent("summarize_validator")

                with st.spinner("Summarizing..."):
                    summary = summarizer.execute(text)
                    st.subheader("Summary:")
                    st.write(summary)

                with st.spinner("Validating summary..."):
                    validation = validator.execute(text, summary)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception as e:
                st.error("Failed to generate summary. Please try again.")
                logger.error(f"Summarization Error: {e}")
        else:
            st.warning("Please enter some text to summarize.")

# Research Article Section
def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article 🖋️")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)
    
    if st.button("Write and Refine Article"):
        if topic.strip():
            try:
                writer = agent_manager.get_agent("write_article")
                refiner = agent_manager.get_agent("refiner")
                validator = agent_manager.get_agent("validator")

                with st.spinner("Writing article..."):
                    draft = writer.execute(topic, outline)
                    st.subheader("Draft Article:")
                    st.write(draft)

                with st.spinner("Refining article..."):
                    refined_article = refiner.execute(draft)
                    st.subheader("Refined Article:")
                    st.write(refined_article)

                with st.spinner("Validating article..."):
                    validation = validator.execute(topic, refined_article)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception as e:
                st.error("Failed to process the article. Please try again.")
                logger.error(f"Article Processing Error: {e}")
        else:
            st.warning("Please enter a topic for the research article.")

# Data Sanitization Section
def sanitize_data_section(agent_manager):
    st.header("Sanitize Data 🔒")
    raw_data = st.text_area("Enter data to sanitize:", height=200)
    
    if st.button("Sanitize Data"):
        if raw_data.strip():
            try:
                sanitizer = agent_manager.get_agent("sanitize_data")
                validator = agent_manager.get_agent("sanitize_data_validator")

                with st.spinner("Sanitizing data..."):
                    sanitized_data = sanitizer.execute(raw_data)
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)

                with st.spinner("Validating sanitized data..."):
                    validation = validator.execute(raw_data, sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception as e:
                st.error("Failed to sanitize data. Please try again.")
                logger.error(f"Data Sanitization Error: {e}")
        else:
            st.warning("Please enter data to sanitize.")

if __name__ == "__main__":
    main()
