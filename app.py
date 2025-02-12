import streamlit as st
from agents import AgentManager
import os

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

    # Fetch environment variables using st.secrets
    api_key = st.secrets["GEMINI_API_KEY"]  # Example of fetching a secret from Streamlit Secrets

    # Project explanation with emojis
    st.markdown("""
    # Multi-Agent AI System with Gemini 🤖✨

    This project showcases a multi-agent AI system designed to perform tasks like:
    - **Text Summarization** ✍️
    - **Research Article Writing** 📝
    - **Data Sanitization** 🛡️

    Powered by **Gemini**, this system enhances productivity and creativity by providing AI workflows for diverse use cases.
    """)

    # Add social media links (LinkedIn & GitHub)
    st.markdown("""
    ## Connect with ME 🤝:
    - [LinkedIn](https://www.linkedin.com/in/hitesh-kumar-aiml/) 🔗
    - [GitHub](https://github.com/Hiteshydv001) 🔗
    """)

    # Sidebar with task selection
    st.sidebar.title("Select Task")
    task = st.sidebar.selectbox("Choose a task:", [
        "Summarize Text 📚",
        "Write and Refine Research Article 🖋️",
        "Sanitize Data 🔒"
    ])

    agent_manager = AgentManager(max_retries=2, verbose=True)

    if task == "Summarize Text 📚":
        summarize_section(agent_manager)
    elif task == "Write and Refine Research Article 🖋️":
        write_and_refine_article_section(agent_manager)
    elif task == "Sanitize Data 🔒":
        sanitize_data_section(agent_manager)

# Function to handle Summarize Text task
def summarize_section(agent_manager):
    st.header("Summarize Text 📚")
    text = st.text_area("Enter text to summarize:", height=200)
    
    if st.button("Summarize"):
        if text:
            try:
                main_agent = agent_manager.get_agent("summarize")
                validator_agent = agent_manager.get_agent("summarize_validator")
                
                with st.spinner("Summarizing..."):
                    summary = main_agent.execute(f"Summarize the following text:\n{text}")
                    st.subheader("Summary:")
                    st.write(summary)

                with st.spinner("Validating summary..."):
                    validation = validator_agent.execute(text, summary)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception:
                st.error("Cannot answer this one.")
        else:
            st.warning("Please enter some text to summarize.")

# Function to handle Write and Refine Research Article task
def write_and_refine_article_section(agent_manager):
    st.header("Write and Refine Research Article 🖋️")
    topic = st.text_input("Enter the topic for the research article:")
    outline = st.text_area("Enter an outline (optional):", height=150)
    
    if st.button("Write and Refine Article"):
        if topic:
            try:
                writer_agent = agent_manager.get_agent("write_article")
                refiner_agent = agent_manager.get_agent("refiner")
                validator_agent = agent_manager.get_agent("validator")

                with st.spinner("Writing article..."):
                    draft = writer_agent.execute(f"Write a detailed research article about {topic}. Outline: {outline}")
                    st.subheader("Draft Article:")
                    st.write(draft)

                with st.spinner("Refining article..."):
                    refined_article = refiner_agent.execute(f"Improve the following research article:\n{draft}")
                    st.subheader("Refined Article:")
                    st.write(refined_article)

                with st.spinner("Validating article..."):
                    validation = validator_agent.execute(draft, refined_article)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception:
                st.error("Cannot answer this one.")
        else:
            st.warning("Please enter a topic for the research article.")

# Function to handle Sanitize Data task
def sanitize_data_section(agent_manager):
    st.header("Sanitize Data 🔒")
    raw_data = st.text_area("Enter data to sanitize:", height=200)
    
    if st.button("Sanitize Data"):
        if raw_data:
            try:
                main_agent = agent_manager.get_agent("sanitize_data")
                validator_agent = agent_manager.get_agent("sanitize_data_validator")

                with st.spinner("Sanitizing data..."):
                    sanitized_data = main_agent.execute(f"Remove all sensitive data from the following:\n{raw_data}")
                    st.subheader("Sanitized Data:")
                    st.write(sanitized_data)

                with st.spinner("Validating sanitized data..."):
                    validation = validator_agent.execute(raw_data, sanitized_data)
                    st.subheader("Validation:")
                    st.write(validation)
            except Exception:
                st.error("Cannot answer this one.")
        else:
            st.warning("Please enter data to sanitize.")

if __name__ == "__main__":
    main()
