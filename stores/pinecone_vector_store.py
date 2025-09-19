import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()


def get_vector_store(embeddings: OpenAIEmbeddings) -> PineconeVectorStore:
	"""Returns an instance of the vector store used."""
	return PineconeVectorStore(
		index_name=os.environ["PINECONE_INDEX_NAME"],
		embedding=embeddings
	)