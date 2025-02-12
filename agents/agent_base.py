import google.generativeai as genai
from abc import ABC, abstractmethod
from loguru import logger
import streamlit as st
import time

# Configure Gemini API using Streamlit secrets
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.error("GEMINI_API_KEY is missing! Make sure to set it in Streamlit secrets.")

class AgentBase(ABC):
    def __init__(self, name, max_retries=3, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_gemini(self, prompt, model="gemini-2-pro"):
        """Calls Gemini AI to generate a response based on the given prompt."""
        if not GEMINI_API_KEY:
            logger.error(f"[{self.name}] GEMINI_API_KEY is missing. Check Streamlit secrets.")
            raise ValueError("GEMINI_API_KEY is missing.")
        
        summary = self.call_gemini(prompt, model="gemini-2-pro")

        if not summary:
            print("API Response: No response received from Gemini API")
            return "Error: Gemini API did not return a summary. Please check logs."

        retries = 0
        while retries < self.max_retries:
            try:
                start_time = time.time()  # Start response time tracking
                
                if self.verbose:
                    logger.info(f"[{self.name}] Sending prompt to Gemini: {prompt}")

                # Create a model instance
                gemini_model = genai.GenerativeModel(model)
                response = gemini_model.generate_content(prompt)

                response_time = round(time.time() - start_time, 2)  # Calculate execution time

                if response and hasattr(response, "text"):
                    reply = response.text
                else:
                    reply = "No response generated."

                if self.verbose:
                    logger.info(f"[{self.name}] Response received in {response_time}s: {reply}")

                return reply

            except (ConnectionError, TimeoutError) as net_err:
                logger.warning(f"[{self.name}] Network error: {net_err}. Retrying {retries + 1}/{self.max_retries}...")
            except Exception as e:
                logger.error(f"[{self.name}] Unexpected error: {e}. Retrying {retries + 1}/{self.max_retries}...")
            
            retries += 1

        logger.critical(f"[{self.name}] Failed to get response from Gemini after {self.max_retries} retries.")
        raise RuntimeError(f"Agent {self.name} failed to get a valid response after {self.max_retries} attempts.")
