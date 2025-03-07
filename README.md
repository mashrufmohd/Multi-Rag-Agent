🚀 Multi-Agent RAG Tools
========================

🌟 Project Overview
-------------------

Welcome to **Multi-Agent RAG Tools**, a powerful AI-driven system designed to streamline complex workflows using multiple intelligent agents. Our system efficiently handles:

📌 **Text Summarization** ✍️ – Get concise summaries of any text, saving time and enhancing readability.📌 **Research Article Writing** 📝 – Generate and refine high-quality research articles with AI-driven assistance.📌 **Data Sanitization** 🛡️ – Ensure privacy and compliance by detecting and removing sensitive data.

This project employs **Retrieval-Augmented Generation (RAG)** and **Multi-Agent AI techniques** to divide complex tasks among specialized agents, improving efficiency, accuracy, and scalability.

### Preview: 
![image](https://github.com/user-attachments/assets/41f48b42-4c9a-4e42-b3f9-877f64201e83)

#
📂 Project Structure
--------------------

```
└── mashrufmohd-multi-rag-agent/
    ├── README.md
    ├── app.py
    ├── requirements.txt
    ├── server.py
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
    ├── frontend/
    │   ├── README.md
    │   ├── components.json
    │   ├── eslint.config.mjs
    │   ├── next.config.ts
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── postcss.config.mjs
    │   ├── tailwind.config.ts
    │   ├── tsconfig.json
    │   ├── .gitignore
    │   ├── public/
    │   └── src/
    │       ├── app/
    │       │   ├── globals.css
    │       │   ├── layout.tsx
    │       │   ├── page.tsx
    │       │   ├── sanitize/
    │       │   │   └── page.tsx
    │       │   ├── summarize/
    │       │   │   └── page.tsx
    │       │   └── write_article/
    │       │       └── page.tsx
    │       ├── components/
    │       │   ├── main-nav.tsx
    │       │   ├── theme-provider.tsx
    │       │   └── ui/
    │       │       ├── button.tsx
    │       │       ├── card.tsx
    │       │       ├── dialog.tsx
    │       │       ├── dropdown-menu.tsx
    │       │       ├── form.tsx
    │       │       ├── input.tsx
    │       │       ├── label.tsx
    │       │       ├── select.tsx
    │       │       ├── tabs.tsx
    │       │       ├── textarea.tsx
    │       │       ├── toast.tsx
    │       │       └── toaster.tsx
    │       ├── hooks/
    │       │   └── use-toast.ts
    │       └── lib/
    │           └── utils.ts
    └── utils/
        ├── __init__.py
        └── logger.py
```
#
✨ Features
----------

✅ **Summarize Text** 📚 – Generate concise summaries of any text, making it easier to digest information.

✅ **Write & Refine Research Articles** 🖋️ – AI-powered content generation that enhances writing quality.

✅ **Sanitize Data** 🔒 – Identify and remove sensitive or personally identifiable information for security and compliance.
#
🛠️ Installation Guide
----------------------

🔹 Clone the repository:

```
    git clone https://github.com/Hiteshydv001/Multi-agent-RAG-tools.git  
    cd Multi-agent-RAG-tools  
```

🔹 Install dependencies:

```
   pip install -r requirements.txt   
   ```

🚀 Running the Application
--------------------------

Run the **Streamlit application** with:

`
   streamlit run app.py   
   `

🔹 Open the web interface in your browser and choose a task from the sidebar:

*   📚 **Summarize Text**
*   🖋️ **Write & Refine Research Articles**
*   🔒 **Sanitize Data**
    
#
🤖 Agents
---------

This system consists of multiple AI agents specialized for different tasks:

🔹 **SummarizeTool** 📜 – Extracts key points and condenses lengthy text into readable summaries.

🔹 **WriteArticleTool** ✍️ – Uses AI-driven techniques to generate well-structured research articles.

🔹 **SanitizeDataTool** 🔐 – Cleans data by removing confidential or sensitive information.

🔹 **RefinerAgent** 🛠️ – Enhances clarity, coherence, and overall quality of generated articles.

🔹 **ValidatorAgent** ✅ – Ensures research articles meet quality and relevance criteria.

🔹 **SummarizeValidatorAgent** 🔍 – Checks the accuracy and completeness of text summaries.

🔹 **SanitizeDataValidatorAgent** 🛡️ – Validates the effectiveness of data sanitization techniques.

#

🔗 Connect with Us!
-------------------

* 📌 [**LinkedIn**](https://www.linkedin.com/in/hitesh-kumar-aiml/)🔗
* 📌 [**GitHub**](https://github.com/Hiteshydv001)🔗

🎉 _Happy Coding!_ 🚀



