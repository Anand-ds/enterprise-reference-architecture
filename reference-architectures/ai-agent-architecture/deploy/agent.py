# AWS Agentic AI Enterprise Architecture Demo
from langchain.llms import Bedrock

class ArchitectureAgent:

    def __init__(self):
        self.llm = Bedrock(
            model_id="anthropic.claude-v2"  # Example LLM on AWS Bedrock
        )

    def ask_architecture_question(self, question):
        prompt = f"""
        You are a senior enterprise architect.
        Answer the following enterprise architecture question:

        {question}
        """
        response = self.llm(prompt)
        return response

if __name__ == "__main__":
    agent = ArchitectureAgent()
    question = "What is a recommended AWS microservices architecture for a large enterprise?"
    answer = agent.ask_architecture_question(question)
    print(answer)
