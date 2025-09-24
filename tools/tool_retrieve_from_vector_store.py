from dotenv import load_dotenv
from langchain.agents import tool
from langchain_pinecone import PineconeVectorStore

load_dotenv()


@tool
def retrieve_from_vector_store(vector_store: PineconeVectorStore, user_input: str) -> list:
	"""
	This method will fetch documents from Pinecone Vector Store, based on the user_input query.
	"""
	return vector_store.as_retriever().invoke(input=user_input)