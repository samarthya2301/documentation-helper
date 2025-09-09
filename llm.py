from typing import Union
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm(model_vendor: str) -> Union[None, ChatOpenAI]:
	"""Returns an instance of the model from the required vendor."""
	if (model_vendor == "openai"):
		return ChatOpenAI(model="gpt-4o-mini")
	return None