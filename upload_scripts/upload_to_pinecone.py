import os
from typing import List, Union

from dotenv import load_dotenv
from langchain_community.document_loaders import (NotebookLoader, TextLoader,
                                                  UnstructuredMarkdownLoader)

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
	print(file_path)
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
	print("\n\nLoading the following files ...")

	for dirpath, dirnames, filenames in os.walk(folder_path):

		for filename in filenames:

			file_path = os.path.join(dirpath, filename)
			loader = get_loader_based_on_extension(file_path)

			if loader:
				documents.extend(loader.load())

	print("\nTotal Files Loaded: ", len(documents))
	return documents


if __name__ == "__main__":

	documents = load_documentation_files()

	# get split documents