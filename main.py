from dotenv import load_dotenv

from embeddings import get_embeddings
from llm import get_llm
from prompt_template import get_prompt_template
from vector_store import get_vector_store

load_dotenv()


if __name__ == "__main__":

	vendor = "openai"

	app_llm = get_llm(vendor)
	# null checks are required where None is returned


	app_embeddings = get_embeddings(vendor)

	app_prompt_template = get_prompt_template()

	app_vector_store = get_vector_store(embeddings=app_embeddings)

	app_chain = (
		{
			"context": vec,
			"question": ""
		}
		| app_prompt_template
	)