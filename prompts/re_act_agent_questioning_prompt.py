from dotenv import load_dotenv

load_dotenv()


def get_re_act_agent_questioning_prompt() -> str:
	"""Retuns a template for the question to be asked to the agent."""

	return """
	Answer the user question based solely on the context below: \

	<context>
	{context}
	</context>

	<question>
	{question}
	</question>
	"""