```json
{
    "memory/semantic_memory.py": {
        "content": "
import logging
from typing import Dict, List
from langflow import StateGraph, Agent

class SemanticMemory:
    """
    A class representing the semantic memory of the agent.
    
    Attributes:
    non_stationary_drift_index (float): The index of non-stationary drift in the memory.
    stochastic_regime_switch (bool): Whether the regime switch is stochastic or not.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the semantic memory with the given parameters.
        
        Args:
        non_stationary_drift_index (float): The index of non-stationary drift in the memory.
        stochastic_regime_switch (bool): Whether the regime switch is stochastic or not.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_graph = StateGraph()
        logging.info('Semantic memory initialized')

    def update_memory(self, new_info: Dict[str, str]) -> None:
        """
        Updates the semantic memory with new information.
        
        Args:
        new_info (Dict[str, str]): The new information to be added to the memory.
        
        Raises:
        Exception: If the update fails.
        """
        try:
            self.memory_graph.add_nodes(new_info)
            logging.info('Memory updated successfully')
        except Exception as e:
            logging.error(f'Error updating memory: {e}')

    def retrieve_info(self, query: str) -> List[str]:
        """
        Retrieves information from the semantic memory based on the given query.
        
        Args:
        query (str): The query to search for in the memory.
        
        Returns:
        List[str]: A list of relevant information found in the memory.
        
        Raises:
        Exception: If the retrieval fails.
        """
        try:
            results = self.memory_graph.search(query)
            logging.info(f'Retrieved {len(results)} results for query: {query}')
            return results
        except Exception as e:
            logging.error(f'Error retrieving info: {e}')
            return []

    def switch_regime(self) -> None:
        """
        Switches the regime of the semantic memory.
        
        Raises:
        Exception: If the regime switch fails.
        """
        try:
            if self.stochastic_regime_switch:
                # Simulate stochastic regime switch
                import random
                self.non_stationary_drift_index += random.uniform(-1, 1)
            else:
                # Simulate deterministic regime switch
                self.non_stationary_drift_index += 1
            logging.info('Regime switched successfully')
        except Exception as e:
            logging.error(f'Error switching regime: {e}')

if __name__ == '__main__':
    # Create a semantic memory instance
    memory = SemanticMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    
    # Update the memory with new information
    new_info = {'key1': 'value1', 'key2': 'value2'}
    memory.update_memory(new_info)
    
    # Retrieve information from the memory
    query = 'key1'
    results = memory.retrieve_info(query)
    print(f'Results for query \'{query}\': {results}')
    
    # Switch the regime of the memory
    memory.switch_regime()
    print(f'Non-stationary drift index after regime switch: {memory.non_stationary_drift_index}')
",
        "commit_message": "feat: implement specialized semantic_memory logic"
    }
}
```