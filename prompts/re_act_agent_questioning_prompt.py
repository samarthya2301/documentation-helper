from dotenv import load_dotenv

load_dotenv()


def get_re_act_agent_questioning_prompt() -> str:
	"""Retuns a template for the question to be asked to the agent."""

	return """
	Answer the user question based solely on the context below: \

	<context>
	{context}
	</context>

	If you don't know the answer, just say you don't know. \
	Don't try to make up an answer. \
	Use 7-8 sentences. Keep the answer as concise as possible. \
	Try to answer with bulleted or numbered lists. \
	If asked to generate a code snippet, generate within the 'code' tags. \
	At the end of your answer, put 'x-x-x-x-x' in a new line. \

	<question>
	{question}
	</question>
	"""