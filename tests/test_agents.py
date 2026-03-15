```json
{
    "tests/test_agents.py": {
        "content": "
import logging
from typing import Dict, List
from langflow import Agent, StateGraph
from agent_zero import MemoryManagement

def create_agent() -> Agent:
    """
    Creates a new agent with a StateGraph and MemoryManagement.
    
    Returns:
    Agent: A new agent instance.
    """
    try:
        logging.info('Creating a new agent')
        agent = Agent()
        agent.state_graph = StateGraph()
        agent.memory_management = MemoryManagement()
        return agent
    except Exception as e:
        logging.error(f'Error creating agent: {e}')
        return None

def add_tools_to_agent(agent: Agent, tools: List[str]) -> None:
    """
    Adds tools to the agent.
    
    Args:
    agent (Agent): The agent to add tools to.
    tools (List[str]): A list of tool names to add.
    """
    try:
        logging.info(f'Adding tools to agent: {tools}')
        for tool in tools:
            agent.add_tool(tool)
    except Exception as e:
        logging.error(f'Error adding tools to agent: {e}')

def simulate_rocket_science(agent: Agent, non_stationary_drift_index: float, stochastic_regime_switch: bool) -> Dict[str, float]:
    """
    Simulates the 'Rocket Science' problem.
    
    Args:
    agent (Agent): The agent to use for simulation.
    non_stationary_drift_index (float): The non-stationary drift index.
    stochastic_regime_switch (bool): Whether to use stochastic regime switch.
    
    Returns:
    Dict[str, float]: A dictionary with simulation results.
    """
    try:
        logging.info('Simulating rocket science')
        results = agent.state_graph.simulate(non_stationary_drift_index, stochastic_regime_switch)
        return results
    except Exception as e:
        logging.error(f'Error simulating rocket science: {e}')
        return {}

def main() -> None:
    """
    Runs a simulation of the 'Rocket Science' problem.
    """
    try:
        logging.info('Running simulation')
        agent = create_agent()
        tools = ['Web Search', 'HTTP', 'Retriever']
        add_tools_to_agent(agent, tools)
        non_stationary_drift_index = 0.5
        stochastic_regime_switch = True
        results = simulate_rocket_science(agent, non_stationary_drift_index, stochastic_regime_switch)
        logging.info(f'Simulation results: {results}')
    except Exception as e:
        logging.error(f'Error running simulation: {e}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
",
        "commit_message": "feat: implement specialized test_agents logic"
    }
}
```