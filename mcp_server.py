"""MCP server for Agent Swarm Orchestrator."""
import sys
import json
from client import AgentSwarmOrchestrator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "aggregate_swarm_consensus",
                "description": "Decomposes goal and selects highest-confidence swarm worker output",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "goal": {"type": "string"},
                        "worker_outputs": {"type": "array"}
                    },
                    "required": ["goal", "worker_outputs"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "aggregate_swarm_consensus":
            args = params.get("arguments", {})
            res = AgentSwarmOrchestrator.execute_swarm_consensus(
                args.get("goal", ""),
                args.get("worker_outputs", [])
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
