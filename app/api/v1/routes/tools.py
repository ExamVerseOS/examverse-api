from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_tools():
    return [
        {"name": "explain_topic"},
        {"name": "generate_quiz"},
        {"name": "search"},
        {"name": "create_plan"}
    ]

@router.post("/execute")
def execute_tool(payload: dict):
    tool = payload.get("tool")

    return {
        "tool": tool,
        "output": "Tool execution placeholder"
    }