from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        """Summarizes any text concisely."""
        prompt = (
            "You are an AI assistant that summarizes text.\n\n"
            "Please provide a concise summary of the following text:\n\n"
            f"{text}\n\nSummary:"
        )

        summary = self.call_gemini(prompt, model="gemini-pro")
        return summary
