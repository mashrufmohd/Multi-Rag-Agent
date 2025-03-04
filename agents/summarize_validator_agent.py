from .agent_base import AgentBase

class SummarizeValidatorAgent(AgentBase):  # <-- Correct class name
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SummarizeValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        """Validates and refines a summary of the given text."""
        prompt = (
            "You are an expert summarization validator AI. Your task is to check if the summary accurately "
            "captures the key points without missing important details.\n\n"
            "### Instructions:\n"
            "- Ensure the summary is accurate and concise.\n"
            "- Identify any missing key points or distortions.\n\n"
            f"### Summary to Validate:\n{text}\n\n"
            "### Validation:"
        )

        validation = self.call_gemini(prompt, model="gemini-1.5-flash")
        return validation
