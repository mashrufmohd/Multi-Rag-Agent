from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        """Refines a research article for clarity, coherence, and academic quality."""
        prompt = (
            "You are an expert editor who refines and enhances research articles for clarity, coherence, "
            "and academic quality.\n\n"
            "Please refine the following research article draft to improve its language, coherence, "
            "and overall quality:\n\n"
            f"{draft}\n\nRefined Article:"
        )
        
        refined_article = self.call_gemini(prompt, model="gemini-pro")
        return refined_article
