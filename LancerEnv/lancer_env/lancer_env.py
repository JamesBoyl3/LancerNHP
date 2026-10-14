
from Lancer import Agent, Map

from pettingzoo import AECEnv
from pettingzoo.utils.agent_selector import AgentSelector
import numpy as np

NUM_ACTIONS = 2
NUM_STATS = 5

class LancerEnv(AECEnv):
	"""
	Deafult Lancer Envioment.
	"""
	metadata = {
		"name": "lancer_env_v0"
		}

	def __init__(self, agents: list[Agent], map: Map) -> None:
		"""
		Env args:
			- Agents:- a list of the agents in the current env
			- Map:- a map object of all tiles in the current game
		"""

		self.agents = agents
		self.possible_agents = agents
		self._agent_selector = AgentSelector(self.agents)

		self.map = map
		
		self._action_spaces = {name: spaces.Discrete(NUM_ACTIONS) for agent in self.agents}
		self._observation_spaces = {
			agent: spaces.Box(low=-1, high=100, shape=(len(self.agents),NUM_STATS), dtype=np.float32)
		}


	def observer(self) -> dict:
		...
