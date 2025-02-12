from .agent_base import AgentBase

class ValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="ValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):
        """Validates the quality and accuracy of a research article."""
        prompt = (
            "You are an AI assistant that validates research articles for accuracy, completeness, and adherence to academic standards.\n\n"
            "Given the topic and the research article below, assess whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Topic: {topic}\n\n"
            f"Article:\n{article}\n\n"
            "Validation:"
        )

        # Call Gemini to validate the article
        validation = self.call_gemini(prompt, model="gemini-2-pro")
        return validation
