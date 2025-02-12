from .agent_base import AgentBase

class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SanitizeDataValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_data, sanitized_data):
        """Validates that sensitive information has been properly removed from the sanitized data."""
        prompt = (
            "You are a data security auditor. Your task is to validate whether sensitive information has been completely removed from the sanitized data.\n\n"
            "### Instructions:\n"
            "1. Compare the sanitized data with the original data.\n"
            "2. Identify any remaining sensitive information in the sanitized data.\n"
            "3. Provide a rating on a scale of 1 to 5 (5 = Completely Sanitized, 1 = Poorly Sanitized).\n"
            "4. Suggest improvements if any sensitive information is still present.\n\n"
            f"### Original Data:\n{original_data}\n\n"
            f"### Sanitized Data:\n{sanitized_data}\n\n"
            "### Validation Report:\n"
            "- Remaining Sensitive Information (if any):\n"
            "- Sanitization Rating (1-5):\n"
            "- Suggested Improvements:"
        )

        validation = self.call_gemini(prompt, model="gemini-2-pro")
        return validation
