from typing import Union

from dotenv import load_dotenv
from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_embeddings(embeddings_vendor: str) -> Union[None, Embeddings]:
	"""Returns an instance of embeddings based on the vendor."""
	if (embeddings_vendor == "openai"):
		return OpenAIEmbeddings()
	return None