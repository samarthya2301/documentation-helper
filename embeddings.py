from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()


def get_embeddings() -> OpenAIEmbeddings:
	"""Returns an instance of embeddings based on the vendor."""
	return OpenAIEmbeddings()