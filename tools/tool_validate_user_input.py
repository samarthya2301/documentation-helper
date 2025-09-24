from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()


@tool
def validate_user_input(user_input: str) -> bool:
	"""
	This method will validate the user input.
	If the user types 'quit' or 'exit' in any case, the method returns False.
	Otherwise, the method returns True.
	"""
	user_input = user_input.lower()
	if user_input == "quit" or user_input == "exit":
		return False
	return True