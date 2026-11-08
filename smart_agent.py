# smart_agent.py
from google import genai
from google.genai import types
import config
import tools

tools.ensure_workspace()

# 1. Force HTTP/REST to bypass gRPC socket hanging behind VPNs
client = genai.Client(
    api_key=config.API_KEY,
    http_options=types.HttpOptions(api_version="v1beta")
)

def tool_list_files() -> str:
    """Lists all files in the workspace directory."""
    print("  -> [Tool] Listing files...", flush=True)
    return f"Files: {tools.list_workspace_files()}"

def tool_read_file(filename: str) -> str:
    """Reads content from a workspace file."""
    print(f"  -> [Tool] Reading '{filename}'...", flush=True)
    return tools.read_workspace_file(filename)

def tool_write_file(filename: str, content: str) -> str:
    """Writes text content to a workspace file."""
    print(f"  -> [Tool] Writing to '{filename}'...", flush=True)
    return tools.write_workspace_file(filename, content)

# 2. Simple direct chat session
chat = client.chats.create(
    model=config.MODEL_NAME,
    config=types.GenerateContentConfig(
        tools=[tool_list_files, tool_read_file, tool_write_file],
        temperature=0.2,
    )
)

print("=== Smart Autonomous Agent Ready ===")
print("Type 'exit' to quit.\n")

while True:
    user_command = input("\nYou: ").strip()
    if user_command.lower() == "exit":
        break
    if not user_command:
        continue

    print("Agent started thinking...", flush=True)
    
    try:
        response = chat.send_message(user_command)
        print(f"\nAgent:\n{response.text}")
    except Exception as e:
        print(f"\nError occurred: {e}")