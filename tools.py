# tools.py
import os

WORKSPACE_DIR = "workspace"

def ensure_workspace():
    if not os.path.exists(WORKSPACE_DIR):
        os.makedirs(WORKSPACE_DIR)

def read_workspace_file(filename: str) -> str:
    """Reads content from a file inside workspace folder."""
    path = os.path.join(WORKSPACE_DIR, filename)
    if not os.path.exists(path):
        return f"Error: File '{filename}' does not exist in workspace."
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_workspace_file(filename: str, content: str) -> str:
    """Writes content to a file inside workspace folder."""
    ensure_workspace()
    path = os.path.join(WORKSPACE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Success: Content saved to {filename}"
def list_workspace_files() -> list:
    """Returns a list of all filenames currently available in the workspace."""
    ensure_workspace()
    return [f for f in os.listdir(WORKSPACE_DIR) if os.path.isfile(os.path.join(WORKSPACE_DIR, f))]