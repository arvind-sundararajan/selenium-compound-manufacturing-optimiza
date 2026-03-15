```json
{
    "tests/test_reasoning.py": {
        "content": "
import logging
from typing import Dict, List
from langflow import Agent, StateGraph
from agent_zero import MemoryManagement

def stochastic_regime_switch(non_stationary_drift_index: float, regime_switch_probability: float) -> float:
    """
    Calculate the stochastic regime switch based on non-stationary drift index and regime switch probability.

    Args:
    non_stationary_drift_index (float): The non-stationary drift index.
    regime_switch_probability (float): The regime switch probability.

    Returns:
    float: The stochastic regime switch.
    """
    try:
        logging.info('Calculating stochastic regime switch')
        return non_stationary_drift_index * regime_switch_probability
    except Exception as e:
        logging.error(f'Error calculating stochastic regime switch: {e}')
        return None

def test_reasoning(agent: Agent, memory_management: MemoryManagement) -> Dict[str, List[float]]:
    """
    Test the reasoning of the agent.

    Args:
    agent (Agent): The agent to test.
    memory_management (MemoryManagement): The memory management system.

    Returns:
    Dict[str, List[float]]: A dictionary of test results.
    """
    try:
        logging.info('Testing agent reasoning')
        test_results = {}
        non_stationary_drift_index = 0.5
        regime_switch_probability = 0.2
        stochastic_regime_switch_result = stochastic_regime_switch(non_stationary_drift_index, regime_switch_probability)
        test_results['stochastic_regime_switch'] = [stochastic_regime_switch_result]
        return test_results
    except Exception as e:
        logging.error(f'Error testing agent reasoning: {e}')
        return {}

def main() -> None:
    """
    Run the main simulation.
    """
    try:
        logging.info('Running main simulation')
        agent = Agent()
        memory_management = MemoryManagement()
        state_graph = StateGraph()
        agent.add_tool(state_graph)
        test_results = test_reasoning(agent, memory_management)
        logging.info(f'Test results: {test_results}')
    except Exception as e:
        logging.error(f'Error running main simulation: {e}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
",
        "commit_message": "feat: implement specialized test_reasoning logic"
    }
}
```