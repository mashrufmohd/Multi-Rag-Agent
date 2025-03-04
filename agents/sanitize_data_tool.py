from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, data):
        """Sanitizes data by removing sensitive information such as PII (Personally Identifiable Information)."""
        prompt = (
            "You are an AI security assistant specializing in data sanitization. "
            "Your task is to remove all sensitive information, including personally identifiable information (PII), "
            "financial details, and confidential content while preserving the data's meaning and readability.\n\n"
            "### Original Data:\n"
            f"{data}\n\n"
            "### Sanitized Data (No PII, Confidential, or Sensitive Info):"
        )

        sanitized_data = self.call_gemini(prompt, model="gemini-1.5-flash")
        return sanitized_data
