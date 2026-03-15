```json
{
    "agents/agent_factory.py": {
        "content": "
import logging
from typing import Dict, List
from langflow import Agent, StateGraph
from dspy import MemoryManagement

class AgentFactory:
    """
    A factory class for creating specialized agents.
    
    Attributes:
    - non_stationary_drift_index (float): The index of non-stationary drift.
    - stochastic_regime_switch (bool): Whether to use stochastic regime switch.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the AgentFactory.
        
        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift.
        - stochastic_regime_switch (bool): Whether to use stochastic regime switch.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.logger = logging.getLogger(__name__)

    def create_agent(self, agent_config: Dict) -> Agent:
        """
        Creates a new agent based on the provided configuration.
        
        Args:
        - agent_config (Dict): The configuration for the agent.
        
        Returns:
        - Agent: The created agent.
        """
        try:
            agent = Agent()
            agent.tools = self._create_tools(agent_config)
            agent.memory = self._create_memory(agent_config)
            self.logger.info('Agent created successfully')
            return agent
        except Exception as e:
            self.logger.error(f'Error creating agent: {e}')
            raise

    def _create_tools(self, agent_config: Dict) -> List:
        """
        Creates the tools for the agent.
        
        Args:
        - agent_config (Dict): The configuration for the agent.
        
        Returns:
        - List: The list of tools.
        """
        try:
            tools = []
            if 'retrieval' in agent_config:
                tools.append(StateGraph())
            if 'http' in agent_config:
                tools.append(MemoryManagement())
            self.logger.info('Tools created successfully')
            return tools
        except Exception as e:
            self.logger.error(f'Error creating tools: {e}')
            raise

    def _create_memory(self, agent_config: Dict) -> Dict:
        """
        Creates the memory for the agent.
        
        Args:
        - agent_config (Dict): The configuration for the agent.
        
        Returns:
        - Dict: The memory for the agent.
        """
        try:
            memory = {}
            if 'memory' in agent_config:
                memory = agent_config['memory']
            self.logger.info('Memory created successfully')
            return memory
        except Exception as e:
            self.logger.error(f'Error creating memory: {e}')
            raise

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    agent_factory = AgentFactory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    agent_config = {
        'retrieval': True,
        'http': True,
        'memory': {
            'key': 'value'
        }
    }
    agent = agent_factory.create_agent(agent_config)
    print(agent.tools)
    print(agent.memory)
",
        "commit_message": "feat: implement specialized agent_factory logic"
    }
}
```