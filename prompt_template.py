from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

def get_prompt_template() -> PromptTemplate:
	"""Retuns a Prompt Template for LLM Chain"""
	prompt_template_str = """
	Answer any user questions based solely on the context below: \

	<context>
	{context}
	</context>

	If you don't know the answer, just say you don't know. \
	Don't try to make up an answer. \
	Use 10 sentences maximum. Keep the answer as concise as possible. \
	Try to answer with bulleted or numbered lists. \
	If asked to generate a code snippet, generate within the <code></code> tags. \
	At the end of your answer, put 'x-x-x-x-x' new line. \

	<question>
	{question}
	</question>
	"""
	return PromptTemplate.from_template(template=prompt_template_str)