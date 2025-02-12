from .agent_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):
        """Generates a structured and well-researched article on the given topic."""
        prompt = (
            "You are an expert academic writer specializing in well-researched, structured, and informative articles.\n\n"
            "### Instructions:\n"
            "- Write a comprehensive research article on the given topic.\n"
            "- Ensure clarity, coherence, and academic rigor.\n"
            "- Structure the article with an **Introduction, Main Body (with subheadings), and Conclusion**.\n"
            "- Use formal academic language and avoid redundancy.\n\n"
            f"### Topic:\n{topic}\n\n"
        )
        
        if outline:
            prompt += f"### Outline:\n{outline}\n\n"

        prompt += "### Research Article:\n"

        # Call Gemini to generate the article
        article = self.call_gemini(prompt, model="gemini-2-pro")
        return article
