from typing import List, Tuple
from langchain.schema import AgentAction


def format_log_to_str(
		intermediate_steps: List[Tuple[AgentAction, str]],
		observation_prefix: str = "Observation: ",
		llm_prefix: str = "Thought: "
) -> str:
	"""Construct a scratch pad that lets the agent continue it's thought process."""
	thoughts = ""
	for action, observation in intermediate_steps:
		thoughts += action.log
		thoughts += f"\n{observation_prefix}{observation}\n{llm_prefix}"
	return thoughts