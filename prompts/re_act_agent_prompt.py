from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()


def get_re_act_agent_prompt() -> PromptTemplate:
	"""Retuns a Prompt Template to create a ReAct Agent."""

	re_act_agent_template = """
	Answer the following questions as best you can. You have access to the following tools:

	<tools>
	{tools}
	</tools>

	Use the following format:

	Question: the input question you must answer
	Thought: you should always think about what to do
	Action: the action to take, should be one of [{tool_names_as_string}]
	Action Input: the input to the action
	Observation: the result of the action
	... (this Thought/Action/Action Input/Observation can repeat N times)
	Thought: I now know the final answer
	Final Answer: the final answer to the original input question

	Begin!

	<question>
	{question}
	</question>

	<thought>
	{thought}
	</thought>
	"""

	# use this after the similar documents are fetched - context
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
	return PromptTemplate.from_template(template=re_act_agent_template)