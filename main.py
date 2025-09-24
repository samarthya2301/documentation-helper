from dotenv import load_dotenv
from langchain.tools.render import render_text_description
from langchain_core.output_parsers import StrOutputParser

from embeddings.openai_embeddings import get_embeddings
from llms.openai_llm import get_llm
from prompts.re_act_agent_prompt import get_re_act_agent_prompt
from prompts.re_act_agent_questioning_prompt import \
    get_re_act_agent_questioning_prompt
from stores.pinecone_vector_store import get_vector_store
from tools.tool_validate_user_input import validate_user_input
from util.util_format_log_to_str import format_log_to_str

load_dotenv()


if __name__ == "__main__":

	print("\nInitializing Application ...")

	# Embeddings for Vector Store
	app_embeddings = get_embeddings()
	# Vector Store Instance
	app_vector_store = get_vector_store(embeddings=app_embeddings)
	print("\nVector Store Ready")

	# LLM for Agent
	app_llm = get_llm()
	# Prompt Template for Agent
	app_agent_prompt_template = get_re_act_agent_prompt()
	# Tools for Agent
	app_agent_tools = [validate_user_input]
	# Thought Pad for Agent
	app_agent_thought = []
	# Additional updates in Prompt Template for Agent
	app_agent_prompt = app_agent_prompt_template.partial(
		tools=render_text_description(app_agent_tools),
		tool_names_as_string=", ".join(tool.name for tool in app_agent_tools)
	)
	# ReAct Agent Instance
	app_re_act_agent = (
		{
			"question": lambda x: x["question"],
			"thought": lambda x: format_log_to_str(x["thought"])
		}
		| app_agent_prompt
		| app_llm
		| StrOutputParser()
	)
	print("\nReAct Agent Ready")

	print("\nStarting Q/A Loop", "\n-----------------")


	"""
	Continue here, create agent loop for the below code.
	agent_step is plain 'str'.
	Maybe StrOutputParser is the reason.
	Check why it is failing with ReActSingleInputOutputParser.
	Create loop based on type of agent_step - AgentAction, AgentFinisha.
	"""
	
	print("\nQuestion: ", end="")
	user_question = input()
	question_context = app_vector_store.as_retriever().invoke(input=user_question)
	react_agent_question = get_re_act_agent_questioning_prompt().format(context=question_context, question=user_question)
	agent_step = app_re_act_agent.invoke(
		{
			"question": react_agent_question,
			"thought": app_agent_thought
		}
	)
	print(agent_step)