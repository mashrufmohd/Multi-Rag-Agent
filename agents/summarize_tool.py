from .agent_base import AgentBase

class SummarizeTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=verbose)

    def execute(self, text):
        """Generates a concise and structured summary of the given text."""
        prompt = (
            "You are an expert summarization AI. Your task is to generate a concise and informative summary "
            "while preserving the key points and main ideas.\n\n"
            "### Instructions:\n"
            "- Keep the summary clear, structured, and to the point.\n"
            "- Avoid redundancy and unnecessary details.\n"
            "- Maintain the original meaning and important insights.\n\n"
            f"### Original Text:\n{text}\n\n"
            "### Summary:"
        )

        summary = self.call_gemini(prompt, model="gemini-1.5-flash")
        return summary
