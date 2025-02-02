
# Multi-Agent RAG Tools

## Project Overview

This project aims to demonstrate a **Multi-Agent AI System** that performs tasks related to:

- **Text Summarization** ✍️
- **Research Article Writing** 📝
- **Data Sanitization** 🛡️

Each agent is responsible for a specific task, ensuring that the multi-agent system efficiently handles complex workflows in areas like summarizing text, generating articles, and sanitizing data.

![image](https://github.com/user-attachments/assets/41f48b42-4c9a-4e42-b3f9-877f64201e83)


## Project Structure

```
hiteshydv001-multi-agent-rag-tools/
├── README.md
├── app.py
├── requirements.txt
├── agents/
│   ├── __init__.py
│   ├── agent_base.py
│   ├── refiner_agent.py
│   ├── sanitize_data_tool.py
│   ├── sanitize_data_validator_agent.py
│   ├── summarize_tool.py
│   ├── summarize_validator_agent.py
│   ├── validator_agent.py
│   ├── write_article_tool.py
│   └── write_article_validator_agent.py
└── utils/
    ├── __init__.py
    └── logger.py
```

## Features

- **Summarize Text**: Summarize any provided text efficiently.
- **Write and Refine Research Articles**: Automatically generate and refine research articles.
- **Sanitize Data**: Clean and sanitize sensitive data for privacy.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Hiteshydv001/Multi-agent-RAG-tools.git
    cd Multi-agent-RAG-tools
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. To run the Streamlit application, execute the following command:

    ```bash
    streamlit run app.py
    ```

2. Open the web interface in your browser and select a task from the sidebar:
    - **Summarize Text 📚**
    - **Write and Refine Research Article 🖋️**
    - **Sanitize Data 🔒**

## Agents

The system is composed of the following agents:

1. **SummarizeTool**: Summarizes text efficiently.
2. **WriteArticleTool**: Generates research articles.
3. **SanitizeDataTool**: Sanitizes sensitive data.
4. **RefinerAgent**: Refines and improves research articles for clarity and quality.
5. **ValidatorAgent**: Validates the quality and relevance of research articles.
6. **SummarizeValidatorAgent**: Validates the quality and accuracy of text summaries.
7. **SanitizeDataValidatorAgent**: Ensures the sanitization of sensitive data is successful.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect with Me

- [LinkedIn](https://www.linkedin.com/in/hitesh-kumar-aiml/) 🔗
- [GitHub](https://github.com/Hiteshydv001) 🔗
