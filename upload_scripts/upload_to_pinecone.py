import os
from typing import List, Union

from dotenv import load_dotenv
from langchain_community.document_loaders import (NotebookLoader, TextLoader,
                                                  UnstructuredMarkdownLoader)
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()


LOADERS_FOR_EXTENSIONS = {
	"md": UnstructuredMarkdownLoader,
	"mdx": UnstructuredMarkdownLoader,
	"ipynb": NotebookLoader,
	"txt": TextLoader,
	"py": TextLoader
}


def get_loader_based_on_extension(file_path: str) -> Union[None, NotebookLoader, TextLoader, UnstructuredMarkdownLoader]:
	"""
	Return a loader for the corresponding file type.
	"""
	extension = file_path.split(".")[-1]
	extension_to_loader_dict = LOADERS_FOR_EXTENSIONS
	loader = extension_to_loader_dict.get(extension)
	return loader(file_path) if loader else None


def load_documentation_files(folder_path="./langchain-docs") -> List:
	"""
	Visits all files in the passed folder & subfolders and loads their extensions.
	Extensions are used to get the corresponding loaders.
	"""
	documents = []
	print("\n\nLoading Documents ...")

	for dirpath, dirnames, filenames in os.walk(folder_path):

		for filename in filenames:

			file_path = os.path.join(dirpath, filename)
			loader = get_loader_based_on_extension(file_path)

			if loader:
				documents.extend(loader.load())

	print("Total Documents Loaded: ", len(documents))
	return documents


def create_document_chunks(splitter: RecursiveCharacterTextSplitter, documents: List) -> List:
	"""
	Convert documents into required chunks, with RecursiveCharacterTextSplitter.
	"""
	print(f"\n\nChunk Size={splitter._chunk_size}, Overlap={splitter._chunk_overlap}, Creating Chunks ...")
	chunks = splitter.split_documents(documents=documents)
	print("Total Chunks Created: ", len(chunks))
	return chunks


def push_data_to_pinecone_vectorstore(embedding: OpenAIEmbeddings, chunks: List):
	"""
	Pushes the data provided to the Vector Store
	"""
	print(f"\n\nPushing data to Vector Store ...")
	PineconeVectorStore.from_documents(embedding=embedding, documents=chunks, index_name=os.environ["PINECONE_INDEX_NAME"])
	print("Pushed Data to Vector Store\n\n")


if __name__ == "__main__":

	documents = load_documentation_files()

	text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
	chunked_documents = create_document_chunks(splitter=text_splitter, documents=documents)

	openai_embeddings = OpenAIEmbeddings()
	push_data_to_pinecone_vectorstore(openai_embeddings, chunked_documents)