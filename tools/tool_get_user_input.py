from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()


@tool
def get_user_input() -> str:
	"""
	This method will get the user's input directly from the terminal.
	"""
	return input("Question: ")