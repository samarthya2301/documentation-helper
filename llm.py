from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm() -> ChatOpenAI:
	"""Returns an instance of the model from the required vendor."""
	return ChatOpenAI(model="gpt-4o-mini")