from .agent_base import AgentBase

class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="WriteArticleTool", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, outline=None):
        """Generates a research article based on the given topic and outline."""
        prompt = f"You are an expert academic writer.\n\nWrite a research article on the following topic:\nTopic: {topic}\n\n"
        
        if outline:
            prompt += f"Outline:\n{outline}\n\n"
        
        prompt += "Article:\n"

        # Call Gemini to generate the article
        article = self.call_gemini(prompt, model="gemini-pro")
        return article
