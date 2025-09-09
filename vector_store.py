import os

from dotenv import load_dotenv
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_pinecone import PineconeVectorStore

load_dotenv()


def get_vector_store(embeddings: Embeddings) -> VectorStore:
	"""Returns an instance of the vector store used."""
	return PineconeVectorStore(
		index_name=os.environ["PINECONE_INDEX_NAME"],
		embedding=embeddings
	)