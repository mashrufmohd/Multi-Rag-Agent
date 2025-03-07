from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        """Refines a research article for clarity, coherence, and academic quality."""
        prompt = (
            "You are a professional research editor. Your task is to refine and enhance research articles "
            "for improved clarity, coherence, and academic rigor. Ensure the language is fluent, the arguments "
            "are well-structured, and the overall readability is optimized.\n\n"
            "### Original Research Article Draft:\n"
            f"{draft}\n\n"
            "### Refined Article (Well-structured, Concise, and Academic):"
        )

        refined_article = self.call_gemini(prompt, model="gemini-1.5-flash")
        return refined_article
