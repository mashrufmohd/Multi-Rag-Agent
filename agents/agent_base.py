import google.generativeai as genai
from abc import ABC, abstractmethod
from loguru import logger
import streamlit as st

# Configure Gemini API using Streamlit secrets
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.error("GEMINI_API_KEY is missing! Make sure to set it in Streamlit secrets.")

class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_gemini(self, prompt, model="gemini-pro"):
        """Calls Gemini AI to generate a response based on the given prompt."""
        if not GEMINI_API_KEY:
            raise ValueError(f"[{self.name}] GEMINI_API_KEY is missing. Check Streamlit secrets.")

        retries = 0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending prompt to Gemini: {prompt}")

                # Create a model instance
                gemini_model = genai.GenerativeModel(model)
                response = gemini_model.generate_content(prompt)

                if response and hasattr(response, "text"):
                    reply = response.text
                else:
                    reply = "No response generated."

                if self.verbose:
                    logger.info(f"[{self.name}] Received response: {reply}")
                return reply

            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during Gemini call: {e}. Retry {retries}/{self.max_retries}")

        raise Exception(f"[{self.name}] Failed to get response from Gemini after {self.max_retries} retries.")
