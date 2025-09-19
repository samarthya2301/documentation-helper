from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough, RunnableSerializable

from embeddings.openai_embeddings import get_embeddings
from llms.openai_llm import get_llm
from prompts.prompt_template import get_prompt_template
from stores.pinecone_vector_store import get_vector_store

load_dotenv()


def app_loop(chain: RunnableSerializable) -> None:

	while (True):

		print("Question: ", end="")
		user_question = input()

		if user_question.lower() == "quit":
			break

		result = chain.invoke(input=user_question)
		print("Answer:\n", result.content, "\n")


if __name__ == "__main__":

	print("\nApplication Initializing!")

	app_llm = get_llm()

	app_embeddings = get_embeddings()

	app_prompt_template = get_prompt_template()

	app_vector_store = get_vector_store(embeddings=app_embeddings)

	print("\nLoading Context!")

	app_chain = (
		{
			"context": app_vector_store.as_retriever(),
			"question": RunnablePassthrough()
		}
		| app_prompt_template
		| app_llm
	)

	print("\nChat Ready. Type 'quit' to exit.\n")

	app_loop(chain=app_chain)

	print("\n\n----- Appliction Quit -----")