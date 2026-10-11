"""Example usage for Agent Swarm Orchestrator."""
from client import AgentSwarmOrchestrator

if __name__ == "__main__":
    res = AgentSwarmOrchestrator.execute_swarm_consensus("Optimize SQL query plan", [
        {"worker_id": "swarm_node_1", "result": "Use composite index on (user_id, created_at)", "confidence": 0.94},
        {"worker_id": "swarm_node_2", "result": "Use full table scan", "confidence": 0.41}
    ])
    print("Consensus Winner:", res["consensus_winner_worker"])
    print("Final Output:", res["consensus_output"])
